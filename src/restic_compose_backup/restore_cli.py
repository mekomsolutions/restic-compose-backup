import argparse
import os
import logging

from restic_compose_backup import (
    alerts,
    restore_runner,
    log,
    restic,
)
from restic_compose_backup.config import Config
from restic_compose_backup.containers import RunningContainers
from restic_compose_backup import cron, utils

logger = logging.getLogger(__name__)


def main():
    """Restore CLI entrypoint"""
    args = parse_args()
    config = Config()
    log.setup(level=args.log_level or config.log_level)
    containers = RunningContainers()

    # Ensure log level is propagated to parent container if overridden
    if args.log_level:
        containers.this_container.set_config_env('LOG_LEVEL', args.log_level)

    if args.action == 'status':
        status(config, containers)

    elif args.action == 'restore':
        restore(config, containers)

    elif args.action == 'start-restore-process':
        start_restore_process(config, containers)

    elif args.action == 'alert':
        alert(config, containers)

    elif args.action == "dump-env":
        dump_env()

    elif args.action == 'version':
        import restic_compose_backup
        print(restic_compose_backup.__version__)

    # Random test stuff here
    elif args.action == "test":
        nodes = utils.get_swarm_nodes()
        print("Swarm nodes:")
        for node in nodes:
            addr = node.attrs['Status']['Addr']
            state = node.attrs['Status']['State']
            print(' - {} {} {}'.format(node.id, addr, state))


def status(config, containers):
    """Outputs the restore config for the compose setup"""
    logger.info("Status for compose project '%s'", containers.project_name)
    logger.info("Repository: '%s'", config.repository)
    logger.info("Restore currently running?: %s", containers.restore_process_running)
    logger.info("Include project name in restore path?: %s", utils.is_true(config.include_project_name))
    logger.debug("Exclude bind mounts from backups?: %s", utils.is_true(config.exclude_bind_mounts))
    logger.info("Checking docker availability")

    utils.list_containers()

    if containers.stale_restore_process_containers:
        utils.remove_containers(containers.stale_restore_process_containers)

    # Check if repository is initialized with restic snapshots
    if not restic.is_initialized(config.repository):
        logger.info("Could not get repository info. Attempting to initialize it.")
        result = restic.init_repo(config.repository)
        if result == 0:
            logger.info("Successfully initialized repository: %s", config.repository)
        else:
            logger.error("Failed to initialize repository")

    logger.info("%s Detected Config %s", "-" * 25, "-" * 25)

    # Start making snapshots
    backup_containers = containers.containers_for_backup()
    for container in backup_containers:
        logger.info('service: %s', container.service_name)

        if container.database_backup_enabled:
            instance = container.instance
            ping = instance.ping()
            logger.info(
                ' - %s (is_ready=%s) -> %s',
                instance.container_type,
                ping == 0,
                instance.backup_destination_path(),
            )
            if ping != 0:
                logger.error("Database '%s' in service %s cannot be reached",
                             instance.container_type, container.service_name)

    if len(backup_containers) == 0:
        logger.info("No containers in the project has 'restic-compose-backup.*' label")

    logger.info("-" * 67)


def restore(config, containers):
    """Request a restore to start"""
    # Make sure we don't spawn multiple restore processes
    logger.info(f"Running:====> {containers.restore_process_running}\n")
    if containers.restore_process_running:
        alerts.send(
            subject="Restore process container already running",
            body=(
                "A restore process container is already running. \n"
                f"Id: {containers.restore_process_container.id}\n"
                f"Name: {containers.restore_process_container.name}\n"
            ),
            alert_type='ERROR',
        )
        logger.info(f"Id: {containers.restore_process_container.id}\n")
        logger.info(f"Name: {containers.restore_process_container.name}\n")
        # raise RuntimeError("Restore process already running")
    # Map all volumes from the Restore container into the Restore process container
    volumes = containers.this_container.volumes

    # Map volumes from other containers we are backing up
    mounts = containers.generate_backup_mounts('/backup/volumes')
    volumes.update(mounts)

    logger.debug('Starting Restore container with image %s', containers.this_container.image)
    try:
        result = restore_runner.run(
            image=containers.this_container.image,
            command='restic-compose-restore start-restore-process',
            volumes=volumes,
            environment=containers.this_container.environment,
            source_container_id=containers.this_container.id,
            labels={
                containers.restore_process_label: 'True',
                "com.docker.compose.project": containers.project_name,
            },
        )
    except Exception as ex:
        logger.info(ex)
        logger.exception(ex)
        alerts.send(
            subject="Exception during Restore",
            body=str(ex),
            alert_type='ERROR',
        )
        return

    logger.info('Restore container exit code: %s', result)

    # Alert the user if something went wrong
    if result != 0:
        alerts.send(
            subject="Restore process exited with non-zero code",
            body=open('restore.log').read(),
            alert_type='ERROR',
        )


def start_restore_process(config, containers):
    """The actual restore process running inside the spawned container"""
    if not utils.is_true(os.environ.get('RESTORE_PROCESS_CONTAINER')):
        logger.error(
            "Cannot run restore process in this container. Use restore command instead. "
            "This will spawn a new container with the necessary mounts."
        )
        alerts.send(
            subject="Cannot run restore process in this container",
            body=(
                "Cannot run restore process in this container. Use restore command instead. "
                "This will spawn a new container with the necessary mounts."
            )
        )
        exit(1)

    status(config, containers)
    errors = False

    # Restore databases
    logger.info('Restoring databases')
    for container in containers.containers_for_backup():
        if container.database_backup_enabled:
            try:
                instance = container.instance
                logger.info('Restoring up %s in service %s', instance.container_type, instance.service_name)
                result = instance.restore_db()
                logger.info('Exit code: %s', result)
                if result != 0:
                    logger.error('Restore command exited with non-zero code: %s', result)
                    errors = True
            except Exception as ex:
                logger.exception(ex)
                errors = True
    
    if errors:
        logger.error('Exit code: %s', errors)
        exit(1)
    backup_db_result = restic.restore_files(config.repository, target='/restored_data/')
    logger.info('Restore completed')


def cleanup(config, containers):
    """Run forget / prune to minimize storage space"""
    logger.info('Forget outdated snapshots')
    forget_result = restic.forget(
        config.repository,
        config.keep_daily,
        config.keep_weekly,
        config.keep_monthly,
        config.keep_yearly,
    )
    logger.info('Prune stale data freeing storage space')
    prune_result = restic.prune(config.repository)
    return forget_result and prune_result


def snapshots(config, containers):
    """Display restic snapshots"""
    stdout, stderr = restic.snapshots(config.repository, last=True)
    for line in stdout.decode().split('\n'):
        print(line)


def alert(config, containers):
    """Test alerts"""
    logger.info("Testing alerts")
    alerts.send(
        subject="{}: Test Alert".format(containers.project_name),
        body="Test message",
    )


def crontab(config):
    """Generate the crontab"""
    print(cron.generate_crontab(config))


def dump_env():
    """Dump all environment variables to a script that can be sourced from cron"""
    print("#!/bin/bash")
    print("# This file was generated by restic-compose-backup")
    for key, value in os.environ.items():
        print("export {}='{}'".format(key, value))


def parse_args():
    parser = argparse.ArgumentParser(prog='restic_compose_backup')
    parser.add_argument(
        'action',
        choices=[
            'status',
            'restore',
            'start-restore-process',
            'alert',
            'version',
            'dump-env',
            'test',
        ],
    )
    parser.add_argument(
        '--log-level',
        default=None,
        choices=list(log.LOG_LEVELS.keys()),
        help="Log level"
    )
    return parser.parse_args()


if __name__ == '__main__':
    main()
