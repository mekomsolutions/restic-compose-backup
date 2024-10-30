"""
Restic commands
"""
import logging
import subprocess
from pathlib import Path
from typing import List, Tuple
from subprocess import Popen, PIPE
import shutil
from restic_compose_backup import commands
from restic_compose_backup.config import config, Config

logger = logging.getLogger(__name__)


def init_repo(repository: str):
    """
    Attempt to initialize the repository.
    Doing this after the repository is initialized
    """
    return commands.run(restic(repository, [
        "init",
    ]))


def backup_files(repository: str, source='/backup/volumes'):
    return commands.run(restic(repository, [
        "--verbose",
        "backup",
        source,
    ]))

def restore_files(repository: str, target='/restored_data',mounts={}):
    config = Config()
    restic_exit_code = commands.run(restic(repository, [
        "--verbose",
        "restore",
        config.restic_restore_snapshot,
        "--target",
        target
    ]))
    
    if (restic_exit_code == 0):
        for source in mounts.values():
            shutil.copytree(f"/restored_data{source['bind']}", source['bind'] , dirs_exist_ok=True)
    return restic_exit_code

def backup_db_file(filename: str, backup_command: str):
    """
    Stage db backup to disk and then backup from disk to restic to get around restic's lack of commulative snapshots
    """
    mkdir_process = subprocess.run(f'mkdir -p {Path(filename).parent}', shell=True)
    backup_process = subprocess.run(backup_command, shell=True)

    # Ensure both processes exited with code 0
    # mkdir_exit,backup_exit =  mkdir_process.poll(), backup_process.poll()
    exit_code = 0 if (mkdir_process.returncode == 0 and backup_process.returncode == 0) else 1

    logger.info('Database backup exit code: =======> %s', exit_code)

    # if stdout:
    #     commands.log_std('stdout', sys.stdout, logging.DEBUG if exit_code == 0 else logging.ERROR)

    # if stderr:
    #     commands.log_std('stderr', sys.stderr, logging.ERROR)

    return exit_code
def restore_db_file(filename: str, restore_command: str):
    """
    Restore database from backup
    """
    restore_process = subprocess.run(restore_command, shell=True)

    exit_code = 0 if (restore_process.returncode == 0) else 1

    logger.info('Database Restore exit code: =======> %s', exit_code)
    return exit_code


def backup_from_stdin(repository: str, filename: str, source_command: List[str]):
    """
    Backs up from stdin running the source_command passed in.
    It will appear in restic with the filename (including path) passed in.
    """
    parameter_list = ['backup',
        '--stdin-filename',
        filename,
        '--stdin-from-command','--']
        
    parameter_list.extend(source_command)
    dest_command = restic(repository, parameter_list)
    dest_process = Popen(dest_command, stdout=PIPE, stderr=PIPE)
    stdout, stderr = dest_process.communicate()
    # Ensure both processes exited with code 0
    dest_exit = dest_process.poll()
    exit_code = 0 if (dest_exit == 0) else 1

    logger.debug('Backup from stdin exit code: =======> %s', exit_code)

    if stdout:
        commands.log_std('stdout', stdout, logging.DEBUG if exit_code == 0 else logging.ERROR)

    if stderr:
        commands.log_std('stderr', stderr, logging.ERROR)

    return exit_code


def snapshots(repository: str, last=True) -> Tuple[str, str]:
    """Returns the stdout and stderr info"""
    args = ["snapshots"]
    if last:
        args.append('--latest')
        args.append('1')
    return commands.run_capture_std(restic(repository, args))


def is_initialized(repository: str) -> bool:
    """
    Checks if a repository is initialized using snapshots command.
    Note that this cannot separate between uninitalized repo
    and other errors, but this method is reccomended by the restic
    community.
    """
    return commands.run(restic(repository, ["snapshots", '--latest','1'])) == 0


def forget(repository: str, daily: str, weekly: str, monthly: str, yearly: str):
    return commands.run(restic(repository, [
        'forget',
        '--group-by',
        'paths',
        '--keep-daily',
        daily,
        '--keep-weekly',
        weekly,
        '--keep-monthly',
        monthly,
        '--keep-yearly',
        yearly,
    ]))


def prune(repository: str):
    return commands.run(restic(repository, [
        'prune',
    ]))


def check(repository: str):
    return commands.run(restic(repository, [
        "check",
        # "--with-cache",
    ]))


def restic(repository: str, args: List[str]):
    """Generate restic command"""
    return [
        "restic",
        "-r",
        repository,
    ] + args
