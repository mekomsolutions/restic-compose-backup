from pathlib import Path
import logging

from restic_compose_backup.containers import Container
from restic_compose_backup.config import config, Config
from restic_compose_backup import (
    commands,
    restic,
)
from restic_compose_backup import utils
logger = logging.getLogger(__name__)


class MariadbContainer(Container):
    container_type = 'mariadb'

    def get_credentials(self) -> dict:
        """dict: get credentials for the service"""
        return {
            'host': self.name,
            'username': 'root',
            'password': self.get_config_env('MYSQL_ROOT_PASSWORD'),
            'port': "3306",
        }

    def ping(self) -> bool:
        """Check the availability of the service"""
        creds = self.get_credentials()

        with utils.environment('MYSQL_PWD', creds['password']):
            return commands.ping_mariadb(
                creds['host'],
                creds['port'],
                creds['username'],
            )

    def dump_command(self) -> list:
        """list: create a dump command restic and use to send data through stdin"""
        creds = self.get_credentials()
        return [
            "mysqldump",
            f"--host={creds['host']}",
            f"--port={creds['port']}",
            f"--user={creds['username']}",
            f"--pa={creds['username']}",
            "--all-databases",
            "--no-tablespaces"
        ]


    def dump_command_str(self) -> str:
        """list: create a dump command restic and use to send data through stdin"""
        creds = self.get_credentials()
        return f"mysqldump --host={creds['host']} --port={creds['port']} --user={creds['username']} --all-databases --no-tablespaces -r {self.backup_destination_path()}"

    def restore_command_str(self) -> str:
        """list: create a restore command to restore database dump from restic"""
        config = Config()
        creds = self.get_credentials()
        return f"restic -r {config.repository} dump latest {self.backup_destination_path()} | mysql --host={creds['host']} --port={creds['port']} --user={creds['username']}"

    def dump_db(self):
        config = Config()
        creds = self.get_credentials()
        with utils.environment('MYSQL_PWD', creds['password']):   
            return restic.backup_db_file(
                self.backup_destination_path(),
                self.dump_command_str(),
            )

    def restore_db(self):
        config = Config()
        creds = self.get_credentials()
        with utils.environment('MYSQL_PWD', creds['password']):   
            return restic.restore_db_file(
                self.backup_destination_path(),
                self.restore_command_str(),
            )

    def backup_destination_path(self) -> str:
        destination = Path("/backup/databases")

        if utils.is_true(config.include_project_name):
            project_name = self.project_name
            if project_name != "":
                destination /= project_name

        destination /= self.service_name
        destination /= "all_databases.sql"

        return destination


class MysqlContainer(Container):
    container_type = 'mysql'

    def get_credentials(self) -> dict:
        """dict: get credentials for the service"""
        return {
            'host': self.name,
            'username': 'root',
            'password': self.get_config_env('MYSQL_ROOT_PASSWORD'),
            'port': "3306",
        }

    def ping(self) -> bool:
        """Check the availability of the service"""
        creds = self.get_credentials()
        logger.info('Backing MariaDB container %s %s', self.service_name,self.backup_destination_path())
        with utils.environment('MYSQL_PWD', creds['password']):
            return commands.ping_mysql(
                creds['host'],
                creds['port'],
                creds['username'],
            )

    def dump_command(self) -> list:
        """list: create a dump command restic and use to send data through stdin"""
        creds = self.get_credentials()
        return [
            "mysqldump",
            f"--host={creds['host']}",
            f"--port={creds['port']}",
            f"--user={creds['username']}",
            "--all-databases",
            "--no-tablespaces"
        ]

    def dump_command_str(self) -> str:
        """list: create a dump command restic and use to send data through stdin"""
        creds = self.get_credentials()
        return f"mysqldump --host={creds['host']} --port={creds['port']} --user={creds['username']} --all-databases --no-tablespaces -r {self.backup_destination_path()}"
    
    def restore_command_str(self) -> str:
        """list: create a restore command to restore database dump from restic"""
        config = Config()
        creds = self.get_credentials()
        return f"restic -r {config.repository} dump latest {self.backup_destination_path()} | mysql --host={creds['host']} --port={creds['port']} --user={creds['username']}"

    def dump_db(self):
        config = Config()
        creds = self.get_credentials()
        logger.info('Backing MySQL container %s %s', self.service_name,self.backup_destination_path())
        with utils.environment('MYSQL_PWD', creds['password']):
            return restic.backup_db_file(
                self.backup_destination_path(),
                self.dump_command_str(),
            )

    def restore_db(self):
        config = Config()
        creds = self.get_credentials()
        with utils.environment('MYSQL_PWD', creds['password']):   
            return restic.restore_db_file(
                self.backup_destination_path(),
                self.restore_command_str(),
            )

    def backup_destination_path(self) -> str:
        destination = Path("/backup/databases")

        if utils.is_true(config.include_project_name):
            project_name = self.project_name
            if project_name != "":
                destination /= project_name

        destination /= self.service_name
        destination /= "all_databases.sql"

        return destination


class PostgresContainer(Container):
    container_type = 'postgres'

    def get_credentials(self) -> dict:
        """dict: get credentials for the service"""
        return {
            'host': self.name,
            'username': self.get_config_env('POSTGRES_USER'),
            'password': self.get_config_env('POSTGRES_PASSWORD'),
            'port': "5432",
            'database': self.get_config_env('POSTGRES_DB'),
        }

    def ping(self) -> bool:
        """Check the availability of the service"""
        creds = self.get_credentials()
        return commands.ping_postgres(
            creds['host'],
            creds['port'],
            creds['username'],
            creds['password'],
        )

    def dump_command(self) -> list:
        """list: create a dump command restic and use to send data through stdin"""
        # NOTE: Backs up a single database from POSTGRES_DB env var
        creds = self.get_credentials()
        return [
            "pg_dumpall",
            f"--host={creds['host']}",
            f"--port={creds['port']}",
            f"--username={creds['username']}"
        ]
    
    def dump_command_str(self) -> str:
        """list: create a dump command restic and use to send data through stdin"""
        # NOTE: Backs up a single database from POSTGRES_DB env var
        creds = self.get_credentials()
        return f"pg_dumpall --host={creds['host']} --port={creds['port']} --username={creds['username']} > {self.backup_destination_path()}"

    def restore_command_str(self) -> str:
        """list: create a restore command to restore database dump from restic"""
        config = Config()
        creds = self.get_credentials()
        return f"restic -r {config.repository} dump latest {self.backup_destination_path()} | psql --host={creds['host']} --port={creds['port']} --username={creds['username']} --dbname=postgres"

    def dump_db(self):
        config = Config()
        creds = self.get_credentials()
        logger.info('Backing PostgresContainer container %s %s', self.service_name,self.backup_destination_path())
        with utils.environment('PGPASSWORD', creds['password']):
            return restic.backup_db_file(
                self.backup_destination_path(),
                self.dump_command_str(),
            )

    def restore_db(self):
        config = Config()
        creds = self.get_credentials()
        with utils.environment('PGPASSWORD', creds['password']):   
            return restic.restore_db_file(
                self.backup_destination_path(),
                self.restore_command_str(),
            )

    def backup_destination_path(self) -> str:
        destination = Path("/backup/databases")

        if utils.is_true(config.include_project_name):
            project_name = self.project_name
            if project_name != "":
                destination /= project_name

        destination /= self.service_name
        destination /= f"{self.get_credentials()['database']}.sql"

        return destination
