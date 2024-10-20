## To test
Run:

```./start-live-system.sh```
This will start the example live system;
Wait for > 5 for the first backup to happen. You can confirm by running

`docker logs -f live-system-backup-1`

You should see logs similar to:

```
2024-10-20 19:00:01,945 - INFO: Starting backup container
2024-10-20 19:00:02,140 - INFO: Backup process container: modest_mcnulty
2024-10-20 19:00:02,357 - INFO: 2024-10-20 19:00:02,357 - INFO: Status for compose project 'live-system'
2024-10-20 19:00:02,358 - INFO: 2024-10-20 19:00:02,357 - INFO: Repository: '/restic_data'
2024-10-20 19:00:02,358 - INFO: 2024-10-20 19:00:02,357 - INFO: Backup currently running?: True
2024-10-20 19:00:02,358 - INFO: 2024-10-20 19:00:02,357 - INFO: Include project name in backup path?: False
2024-10-20 19:00:02,358 - INFO: 2024-10-20 19:00:02,357 - INFO: Checking docker availability
2024-10-20 19:00:02,393 - INFO: 2024-10-20 19:00:02,392 - ERROR: ---------- stderr ----------
2024-10-20 19:00:02,393 - INFO: 2024-10-20 19:00:02,392 - ERROR: Fatal: repository does not exist: unable to open config file: stat /restic_data/config: no such file or directory
2024-10-20 19:00:02,393 - INFO: 2024-10-20 19:00:02,392 - ERROR: Is there a repository at the following location?
2024-10-20 19:00:02,393 - INFO: 2024-10-20 19:00:02,392 - ERROR: /restic_data
2024-10-20 19:00:02,393 - INFO: 2024-10-20 19:00:02,392 - ERROR: ----------------------------
2024-10-20 19:00:02,394 - INFO: 2024-10-20 19:00:02,392 - INFO: Could not get repository info. Attempting to initialize it.
2024-10-20 19:00:04,965 - INFO: 2024-10-20 19:00:04,964 - INFO: Successfully initialized repository: /restic_data
2024-10-20 19:00:04,965 - INFO: 2024-10-20 19:00:04,965 - INFO: ------------------------- Detected Config -------------------------
2024-10-20 19:00:04,966 - INFO: 2024-10-20 19:00:04,965 - INFO: service: mysql5
2024-10-20 19:00:04,966 - INFO: 2024-10-20 19:00:04,965 - INFO: Container NAME live-system-mysql5-1
2024-10-20 19:00:04,966 - INFO: 2024-10-20 19:00:04,965 - INFO: Backing MariaDB container mysql5 /backup/databases/mysql5/all_databases.sql
2024-10-20 19:00:05,004 - INFO: 2024-10-20 19:00:05,003 - INFO:  - mysql (is_ready=True) -> /backup/databases/mysql5/all_databases.sql
2024-10-20 19:00:05,004 - INFO: 2024-10-20 19:00:05,003 - INFO: service: web
2024-10-20 19:00:05,004 - INFO: 2024-10-20 19:00:05,004 - INFO:  - volume: /workspace/restic-compose-backup/src/tests -> /backup/volumes/web/srv/tests
2024-10-20 19:00:05,005 - INFO: 2024-10-20 19:00:05,004 - INFO: service: mariadb
2024-10-20 19:00:05,005 - INFO: 2024-10-20 19:00:05,004 - INFO: Container NAME live-system-mariadb-1
2024-10-20 19:00:05,009 - INFO: 2024-10-20 19:00:05,009 - INFO:  - mariadb (is_ready=True) -> /backup/databases/mariadb/all_databases.sql
2024-10-20 19:00:05,009 - INFO: 2024-10-20 19:00:05,009 - INFO: service: postgres
2024-10-20 19:00:05,009 - INFO: 2024-10-20 19:00:05,009 - INFO: Container NAME live-system-postgres-1
2024-10-20 19:00:05,014 - INFO: 2024-10-20 19:00:05,014 - INFO: Container NAME live-system-postgres-1
2024-10-20 19:00:05,015 - INFO: 2024-10-20 19:00:05,014 - INFO:  - postgres (is_ready=True) -> /backup/databases/postgres/test-postgres.sql
2024-10-20 19:00:05,015 - INFO: 2024-10-20 19:00:05,014 - INFO: service: mysql8
2024-10-20 19:00:05,015 - INFO: 2024-10-20 19:00:05,014 - INFO: Container NAME live-system-mysql8-1
2024-10-20 19:00:05,016 - INFO: 2024-10-20 19:00:05,014 - INFO: Backing MariaDB container mysql8 /backup/databases/mysql8/all_databases.sql
2024-10-20 19:00:05,046 - INFO: 2024-10-20 19:00:05,045 - INFO:  - mysql (is_ready=True) -> /backup/databases/mysql8/all_databases.sql
2024-10-20 19:00:05,046 - INFO: 2024-10-20 19:00:05,045 - INFO: -------------------------------------------------------------------
2024-10-20 19:00:05,046 - INFO: 2024-10-20 19:00:05,045 - INFO: Backing up databases
2024-10-20 19:00:05,047 - INFO: 2024-10-20 19:00:05,046 - INFO: Backing up mysql in service mysql5
2024-10-20 19:00:05,047 - INFO: 2024-10-20 19:00:05,046 - INFO: Container NAME live-system-mysql5-1
2024-10-20 19:00:05,047 - INFO: 2024-10-20 19:00:05,046 - INFO: Backing MySQL container mysql5 /backup/databases/mysql5/all_databases.sql
2024-10-20 19:00:05,047 - INFO: 2024-10-20 19:00:05,046 - INFO: Container NAME live-system-mysql5-1
2024-10-20 19:00:05,091 - INFO: 2024-10-20 19:00:05,091 - INFO: Database backup exit code: =======> 0
2024-10-20 19:00:05,092 - INFO: 2024-10-20 19:00:05,091 - INFO: Exit code: 0
2024-10-20 19:00:05,092 - INFO: 2024-10-20 19:00:05,091 - INFO: Backing up mariadb in service mariadb
2024-10-20 19:00:05,092 - INFO: 2024-10-20 19:00:05,091 - INFO: Container NAME live-system-mariadb-1
2024-10-20 19:00:05,092 - INFO: 2024-10-20 19:00:05,091 - INFO: Container NAME live-system-mariadb-1
2024-10-20 19:00:05,102 - INFO: 2024-10-20 19:00:05,102 - INFO: Database backup exit code: =======> 0
2024-10-20 19:00:05,103 - INFO: 2024-10-20 19:00:05,102 - INFO: Exit code: 0
2024-10-20 19:00:05,103 - INFO: 2024-10-20 19:00:05,102 - INFO: Backing up postgres in service postgres
2024-10-20 19:00:05,103 - INFO: 2024-10-20 19:00:05,102 - INFO: Container NAME live-system-postgres-1
2024-10-20 19:00:05,104 - INFO: 2024-10-20 19:00:05,102 - INFO: Container NAME live-system-postgres-1
2024-10-20 19:00:05,104 - INFO: 2024-10-20 19:00:05,102 - INFO: Backing PostgresContainer container postgres /backup/databases/postgres/test-postgres.sql
2024-10-20 19:00:05,104 - INFO: 2024-10-20 19:00:05,102 - INFO: Container NAME live-system-postgres-1
2024-10-20 19:00:05,104 - INFO: 2024-10-20 19:00:05,102 - INFO: Container NAME live-system-postgres-1
2024-10-20 19:00:05,105 - INFO: 2024-10-20 19:00:05,102 - INFO: Container NAME live-system-postgres-1
2024-10-20 19:00:05,296 - INFO: 2024-10-20 19:00:05,295 - INFO: Database backup exit code: =======> 0
2024-10-20 19:00:05,296 - INFO: 2024-10-20 19:00:05,295 - INFO: Exit code: 0
2024-10-20 19:00:05,296 - INFO: 2024-10-20 19:00:05,295 - INFO: Backing up mysql in service mysql8
2024-10-20 19:00:05,297 - INFO: 2024-10-20 19:00:05,296 - INFO: Container NAME live-system-mysql8-1
2024-10-20 19:00:05,297 - INFO: 2024-10-20 19:00:05,296 - INFO: Backing MySQL container mysql8 /backup/databases/mysql8/all_databases.sql
2024-10-20 19:00:05,297 - INFO: 2024-10-20 19:00:05,296 - INFO: Container NAME live-system-mysql8-1
2024-10-20 19:00:05,335 - INFO: 2024-10-20 19:00:05,334 - INFO: Database backup exit code: =======> 0
2024-10-20 19:00:05,335 - INFO: 2024-10-20 19:00:05,334 - INFO: Exit code: 0
2024-10-20 19:00:05,335 - INFO: 2024-10-20 19:00:05,334 - INFO: Backup files from ===> /backup/
2024-10-20 19:00:06,068 - INFO: 2024-10-20 19:00:06,067 - INFO: Forget outdated snapshots
2024-10-20 19:00:06,770 - INFO: 2024-10-20 19:00:06,770 - INFO: Prune stale data freeing storage space
2024-10-20 19:00:07,488 - INFO: 2024-10-20 19:00:07,487 - INFO: Checking the repository for errors
2024-10-20 19:00:08,204 - INFO: 2024-10-20 19:00:08,203 - INFO: Backup completed
2024-10-20 19:00:08,275 - INFO: Backup container exit code: 0
```

Check the databases

```docker exec -it live-system-mysql8-1  bash```

```mysql -uroot -pmy-secret-pw```

```show databases;```

```
+--------------------+
| Database           |
+--------------------+
| classicmodels      |
| information_schema |
| mydb-8             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)
```


Stop the live system to avoid conflicts as the backup service may try to backup the restored system (The backup and restore services are not intended to run on the same system)

```./stop-live-system.sh```

Run the restore 

```./restore-backup.sh```

Check the restore logs

```docker logs -f restore-test-restore-1```

You should see logs similar to:

```
2024-10-20 19:06:24,027 - INFO: Running:====> False

2024-10-20 19:06:24,027 - INFO: Starting Restore container
2024-10-20 19:06:24,238 - INFO: Restore process container: competent_perlman
2024-10-20 19:06:24,449 - INFO: 2024-10-20 19:06:24,448 - INFO: Status for compose project 'restore-test'
2024-10-20 19:06:24,449 - INFO: 2024-10-20 19:06:24,448 - INFO: Repository: '/restic_data'
2024-10-20 19:06:24,449 - INFO: 2024-10-20 19:06:24,448 - INFO: Restore currently running?: True
2024-10-20 19:06:24,449 - INFO: 2024-10-20 19:06:24,448 - INFO: Include project name in restore path?: False
2024-10-20 19:06:24,450 - INFO: 2024-10-20 19:06:24,448 - INFO: Checking docker availability
2024-10-20 19:06:25,169 - INFO: 2024-10-20 19:06:25,168 - INFO: ------------------------- Detected Config -------------------------
2024-10-20 19:06:25,169 - INFO: 2024-10-20 19:06:25,168 - INFO: service: postgres
2024-10-20 19:06:25,169 - INFO: 2024-10-20 19:06:25,169 - INFO: Container NAME restore-test-postgres-1
2024-10-20 19:06:25,174 - INFO: 2024-10-20 19:06:25,174 - INFO: Container NAME restore-test-postgres-1
2024-10-20 19:06:25,175 - INFO: 2024-10-20 19:06:25,174 - INFO:  - postgres (is_ready=True) -> /backup/databases/postgres/test-postgres.sql
2024-10-20 19:06:25,175 - INFO: 2024-10-20 19:06:25,174 - INFO: service: mariadb
2024-10-20 19:06:25,175 - INFO: 2024-10-20 19:06:25,174 - INFO: Container NAME restore-test-mariadb-1
2024-10-20 19:06:25,179 - INFO: 2024-10-20 19:06:25,179 - INFO:  - mariadb (is_ready=True) -> /backup/databases/mariadb/all_databases.sql
2024-10-20 19:06:25,179 - INFO: 2024-10-20 19:06:25,179 - INFO: service: mysql5
2024-10-20 19:06:25,179 - INFO: 2024-10-20 19:06:25,179 - INFO: Container NAME restore-test-mysql5-1
2024-10-20 19:06:25,180 - INFO: 2024-10-20 19:06:25,179 - INFO: Backing MariaDB container mysql5 /backup/databases/mysql5/all_databases.sql
2024-10-20 19:06:25,216 - INFO: 2024-10-20 19:06:25,215 - INFO:  - mysql (is_ready=True) -> /backup/databases/mysql5/all_databases.sql
2024-10-20 19:06:25,216 - INFO: 2024-10-20 19:06:25,215 - INFO: service: web
2024-10-20 19:06:25,216 - INFO: 2024-10-20 19:06:25,215 - INFO: service: mysql8
2024-10-20 19:06:25,216 - INFO: 2024-10-20 19:06:25,215 - INFO: Container NAME restore-test-mysql8-1
2024-10-20 19:06:25,217 - INFO: 2024-10-20 19:06:25,215 - INFO: Backing MariaDB container mysql8 /backup/databases/mysql8/all_databases.sql
2024-10-20 19:06:25,248 - INFO: 2024-10-20 19:06:25,247 - INFO:  - mysql (is_ready=True) -> /backup/databases/mysql8/all_databases.sql
2024-10-20 19:06:25,248 - INFO: 2024-10-20 19:06:25,247 - INFO: -------------------------------------------------------------------
2024-10-20 19:06:25,248 - INFO: 2024-10-20 19:06:25,247 - INFO: Restoring databases
2024-10-20 19:06:25,249 - INFO: 2024-10-20 19:06:25,247 - INFO: Restoring up postgres in service postgres
2024-10-20 19:06:25,249 - INFO: 2024-10-20 19:06:25,247 - INFO: Container NAME restore-test-postgres-1
2024-10-20 19:06:25,249 - INFO: 2024-10-20 19:06:25,248 - INFO: Container NAME restore-test-postgres-1
2024-10-20 19:06:25,249 - INFO: 2024-10-20 19:06:25,248 - INFO: Container NAME restore-test-postgres-1
2024-10-20 19:06:25,250 - INFO: 2024-10-20 19:06:25,248 - INFO: Container NAME restore-test-postgres-1
2024-10-20 19:06:25,250 - INFO: 2024-10-20 19:06:25,248 - INFO: Database restore_command: =======> restic -r /restic_data dump latest /backup/databases/postgres/test-postgres.sql | psql --host=restore-test-postgres-1 --port=5432 --username=pguser --dbname=postgres
2024-10-20 19:06:25,955 - INFO: SET
2024-10-20 19:06:25,956 - INFO: SET
2024-10-20 19:06:25,956 - INFO: SET
2024-10-20 19:06:25,956 - INFO: ERROR:  role "pguser" already exists
2024-10-20 19:06:25,957 - INFO: ALTER ROLE
2024-10-20 19:06:25,964 - INFO: You are now connected to database "template1" as user "pguser".
2024-10-20 19:06:25,965 - INFO: SET
2024-10-20 19:06:25,965 - INFO: SET
2024-10-20 19:06:25,965 - INFO: SET
2024-10-20 19:06:25,965 - INFO: SET
2024-10-20 19:06:25,965 - INFO: SET
2024-10-20 19:06:25,966 - INFO:  set_config
2024-10-20 19:06:25,966 - INFO: ------------
2024-10-20 19:06:25,966 - INFO: 
2024-10-20 19:06:25,966 - INFO: (1 row)
2024-10-20 19:06:25,966 - INFO: 
2024-10-20 19:06:25,966 - INFO: SET
2024-10-20 19:06:25,967 - INFO: SET
2024-10-20 19:06:25,967 - INFO: SET
2024-10-20 19:06:25,967 - INFO: SET
2024-10-20 19:06:25,967 - INFO: ALTER SCHEMA
2024-10-20 19:06:25,967 - INFO: REVOKE
2024-10-20 19:06:25,968 - INFO: GRANT
2024-10-20 19:06:25,971 - INFO: You are now connected to database "postgres" as user "pguser".
2024-10-20 19:06:25,971 - INFO: SET
2024-10-20 19:06:25,972 - INFO: SET
2024-10-20 19:06:25,972 - INFO: SET
2024-10-20 19:06:25,972 - INFO: SET
2024-10-20 19:06:25,972 - INFO: SET
2024-10-20 19:06:25,973 - INFO:  set_config
2024-10-20 19:06:25,973 - INFO: ------------
2024-10-20 19:06:25,973 - INFO: 
2024-10-20 19:06:25,973 - INFO: (1 row)
2024-10-20 19:06:25,973 - INFO: 
2024-10-20 19:06:25,973 - INFO: SET
2024-10-20 19:06:25,973 - INFO: SET
2024-10-20 19:06:25,973 - INFO: SET
2024-10-20 19:06:25,973 - INFO: SET
2024-10-20 19:06:25,973 - INFO: ALTER SCHEMA
2024-10-20 19:06:25,974 - INFO: REVOKE
2024-10-20 19:06:25,975 - INFO: GRANT
2024-10-20 19:06:25,975 - INFO: SET
2024-10-20 19:06:25,975 - INFO: SET
2024-10-20 19:06:25,975 - INFO: SET
2024-10-20 19:06:25,975 - INFO: SET
2024-10-20 19:06:25,975 - INFO: SET
2024-10-20 19:06:25,975 - INFO:  set_config
2024-10-20 19:06:25,975 - INFO: ------------
2024-10-20 19:06:25,976 - INFO: 
2024-10-20 19:06:25,976 - INFO: (1 row)
2024-10-20 19:06:25,976 - INFO: 
2024-10-20 19:06:25,976 - INFO: SET
2024-10-20 19:06:25,976 - INFO: SET
2024-10-20 19:06:25,976 - INFO: SET
2024-10-20 19:06:25,976 - INFO: SET
2024-10-20 19:06:25,976 - INFO: ERROR:  option "locale_provider" not recognized
2024-10-20 19:06:25,977 - INFO: LINE 1: ...gres" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PRO...
2024-10-20 19:06:25,977 - INFO:                                                              ^
2024-10-20 19:06:25,977 - INFO: ALTER DATABASE
2024-10-20 19:06:25,983 - INFO: You are now connected to database "test-postgres" as user "pguser".
2024-10-20 19:06:25,983 - INFO: SET
2024-10-20 19:06:25,983 - INFO: SET
2024-10-20 19:06:25,983 - INFO: SET
2024-10-20 19:06:25,983 - INFO: SET
2024-10-20 19:06:25,984 - INFO: SET
2024-10-20 19:06:25,984 - INFO:  set_config
2024-10-20 19:06:25,984 - INFO: ------------
2024-10-20 19:06:25,984 - INFO: 
2024-10-20 19:06:25,984 - INFO: (1 row)
2024-10-20 19:06:25,984 - INFO: 
2024-10-20 19:06:25,985 - INFO: SET
2024-10-20 19:06:25,985 - INFO: SET
2024-10-20 19:06:25,985 - INFO: SET
2024-10-20 19:06:25,985 - INFO: SET
2024-10-20 19:06:25,985 - INFO: CREATE SCHEMA
2024-10-20 19:06:25,986 - INFO: ALTER SCHEMA
2024-10-20 19:06:25,986 - INFO: ALTER SCHEMA
2024-10-20 19:06:25,987 - INFO: CREATE TYPE
2024-10-20 19:06:25,987 - INFO: ALTER TYPE
2024-10-20 19:06:25,987 - INFO: SET
2024-10-20 19:06:25,988 - INFO: SET
2024-10-20 19:06:25,989 - INFO: CREATE TABLE
2024-10-20 19:06:25,989 - INFO: ALTER TABLE
2024-10-20 19:06:25,990 - INFO: CREATE TABLE
2024-10-20 19:06:25,991 - INFO: ALTER TABLE
2024-10-20 19:06:25,991 - INFO: CREATE TABLE
2024-10-20 19:06:25,992 - INFO: ALTER TABLE
2024-10-20 19:06:25,992 - INFO: CREATE TABLE
2024-10-20 19:06:25,993 - INFO: ALTER TABLE
2024-10-20 19:06:25,994 - INFO: CREATE SEQUENCE
2024-10-20 19:06:25,994 - INFO: ALTER SEQUENCE
2024-10-20 19:06:25,995 - INFO: ALTER SEQUENCE
2024-10-20 19:06:25,996 - INFO: CREATE TABLE
2024-10-20 19:06:25,996 - INFO: ALTER TABLE
2024-10-20 19:06:25,997 - INFO: CREATE TABLE
2024-10-20 19:06:25,997 - INFO: ALTER TABLE
2024-10-20 19:06:25,998 - INFO: ALTER TABLE
2024-10-20 19:06:25,999 - INFO: COPY 0
2024-10-20 19:06:25,999 - INFO: COPY 0
2024-10-20 19:06:25,999 - INFO: COPY 0
2024-10-20 19:06:25,999 - INFO: COPY 0
2024-10-20 19:06:25,999 - INFO: COPY 0
2024-10-20 19:06:26,000 - INFO: COPY 0
2024-10-20 19:06:26,000 - INFO:  setval
2024-10-20 19:06:26,000 - INFO: --------
2024-10-20 19:06:26,000 - INFO:       1
2024-10-20 19:06:26,000 - INFO: (1 row)
2024-10-20 19:06:26,000 - INFO: 
2024-10-20 19:06:26,003 - INFO: ALTER TABLE
2024-10-20 19:06:26,004 - INFO: ALTER TABLE
2024-10-20 19:06:26,005 - INFO: ALTER TABLE
2024-10-20 19:06:26,006 - INFO: ALTER TABLE
2024-10-20 19:06:26,008 - INFO: ALTER TABLE
2024-10-20 19:06:26,009 - INFO: ALTER TABLE
2024-10-20 19:06:26,011 - INFO: CREATE INDEX
2024-10-20 19:06:26,012 - INFO: CREATE INDEX
2024-10-20 19:06:26,013 - INFO: CREATE INDEX
2024-10-20 19:06:26,015 - INFO: ALTER TABLE
2024-10-20 19:06:26,016 - INFO: ALTER TABLE
2024-10-20 19:06:26,017 - INFO: ALTER TABLE
2024-10-20 19:06:26,018 - INFO: ALTER TABLE
2024-10-20 19:06:26,019 - INFO: ALTER TABLE
2024-10-20 19:06:26,020 - INFO: ALTER TABLE
2024-10-20 19:06:26,020 - INFO: REVOKE
2024-10-20 19:06:26,020 - INFO: GRANT
2024-10-20 19:06:26,022 - INFO: 2024-10-20 19:06:26,021 - INFO: Database Restore exit code: =======> 0
2024-10-20 19:06:26,022 - INFO: 2024-10-20 19:06:26,022 - INFO: Exit code: 0
2024-10-20 19:06:26,022 - INFO: 2024-10-20 19:06:26,022 - INFO: Restoring up mariadb in service mariadb
2024-10-20 19:06:26,022 - INFO: 2024-10-20 19:06:26,022 - INFO: Container NAME restore-test-mariadb-1
2024-10-20 19:06:26,023 - INFO: 2024-10-20 19:06:26,022 - INFO: Container NAME restore-test-mariadb-1
2024-10-20 19:06:26,023 - INFO: 2024-10-20 19:06:26,022 - INFO: Database restore_command: =======> restic -r /restic_data dump latest /backup/databases/mariadb/all_databases.sql | mysql --host=restore-test-mariadb-1 --port=3306 --user=myuser
2024-10-20 19:06:26,720 - INFO: 2024-10-20 19:06:26,719 - INFO: Database Restore exit code: =======> 0
2024-10-20 19:06:26,720 - INFO: 2024-10-20 19:06:26,719 - INFO: Exit code: 0
2024-10-20 19:06:26,720 - INFO: 2024-10-20 19:06:26,719 - INFO: Restoring up mysql in service mysql5
2024-10-20 19:06:26,720 - INFO: 2024-10-20 19:06:26,719 - INFO: Container NAME restore-test-mysql5-1
2024-10-20 19:06:26,720 - INFO: 2024-10-20 19:06:26,719 - INFO: Container NAME restore-test-mysql5-1
2024-10-20 19:06:26,720 - INFO: 2024-10-20 19:06:26,719 - INFO: Database restore_command: =======> restic -r /restic_data dump latest /backup/databases/mysql5/all_databases.sql | mysql --host=restore-test-mysql5-1 --port=3306 --user=myuser
2024-10-20 19:06:27,424 - INFO: 2024-10-20 19:06:27,423 - INFO: Database Restore exit code: =======> 0
2024-10-20 19:06:27,424 - INFO: 2024-10-20 19:06:27,423 - INFO: Exit code: 0
2024-10-20 19:06:27,424 - INFO: 2024-10-20 19:06:27,423 - INFO: Restoring up mysql in service mysql8
2024-10-20 19:06:27,424 - INFO: 2024-10-20 19:06:27,423 - INFO: Container NAME restore-test-mysql8-1
2024-10-20 19:06:27,424 - INFO: 2024-10-20 19:06:27,424 - INFO: Container NAME restore-test-mysql8-1
2024-10-20 19:06:27,425 - INFO: 2024-10-20 19:06:27,424 - INFO: Database restore_command: =======> restic -r /restic_data dump latest /backup/databases/mysql8/all_databases.sql | mysql --host=restore-test-mysql8-1 --port=3306 --user=myuser
2024-10-20 19:06:28,157 - INFO: 2024-10-20 19:06:28,157 - INFO: Database Restore exit code: =======> 0
2024-10-20 19:06:28,157 - INFO: 2024-10-20 19:06:28,157 - INFO: Exit code: 0
2024-10-20 19:06:28,158 - INFO: 2024-10-20 19:06:28,157 - INFO: Restoring files to ===> /restored_data/
2024-10-20 19:06:28,864 - INFO: 2024-10-20 19:06:28,864 - INFO: Restore completed
2024-10-20 19:06:28,943 - INFO: Restore container exit code: 0
```
 You can now check the databases for restored data for example 

```docker exec -it restore-test-mysql8-1 bash``

```mysql -uroot -pmy-secret-pw```

```show databases;```

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mydb-8             |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

```

Stop backup system

```./stop-backup-system.sh```

## Clean up

Remove Restored data:

```sudo rm -rf /workspace/restic-compose-backup/restored_data/backup```

Remove Backup Repo

```sudo rm -rf /workspace/restic-compose-backup/restic_data/{data,index,keys,locks,snapshots,config}```


