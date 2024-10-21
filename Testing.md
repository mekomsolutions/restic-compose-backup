## To test
Run:

```./start-live-system.sh```
This will start the example live system;
Wait for > 5 for the first backup to happen. You can confirm by running

`docker logs -f live-system-backup-1`

You should see logs similar to:

```
crond 4.5 dillon's cron daemon, started with loglevel notice
2024-10-21 03:50:01,338 - INFO: Starting backup container
2024-10-21 03:50:01,647 - INFO: Backup process container: compassionate_ganguly
2024-10-21 03:50:01,848 - INFO: 2024-10-21 03:50:01,848 - INFO: Status for compose project 'live-system'
2024-10-21 03:50:01,848 - INFO: 2024-10-21 03:50:01,848 - INFO: Repository: '/restic_data'
2024-10-21 03:50:01,849 - INFO: 2024-10-21 03:50:01,848 - INFO: Backup currently running?: True
2024-10-21 03:50:01,849 - INFO: 2024-10-21 03:50:01,848 - INFO: Include project name in backup path?: False
2024-10-21 03:50:01,849 - INFO: 2024-10-21 03:50:01,848 - INFO: Checking docker availability
2024-10-21 03:50:01,882 - INFO: 2024-10-21 03:50:01,881 - ERROR: ---------- stderr ----------
2024-10-21 03:50:01,883 - INFO: 2024-10-21 03:50:01,881 - ERROR: Fatal: repository does not exist: unable to open config file: stat /restic_data/config: no such file or directory
2024-10-21 03:50:01,883 - INFO: 2024-10-21 03:50:01,882 - ERROR: Is there a repository at the following location?
2024-10-21 03:50:01,883 - INFO: 2024-10-21 03:50:01,882 - ERROR: /restic_data
2024-10-21 03:50:01,883 - INFO: 2024-10-21 03:50:01,882 - ERROR: ----------------------------
2024-10-21 03:50:01,884 - INFO: 2024-10-21 03:50:01,882 - INFO: Could not get repository info. Attempting to initialize it.
2024-10-21 03:50:03,933 - INFO: 2024-10-21 03:50:03,933 - INFO: Successfully initialized repository: /restic_data
2024-10-21 03:50:03,933 - INFO: 2024-10-21 03:50:03,933 - INFO: ------------------------- Detected Config -------------------------
2024-10-21 03:50:03,934 - INFO: 2024-10-21 03:50:03,933 - INFO: service: postgres
2024-10-21 03:50:03,934 - INFO: 2024-10-21 03:50:03,934 - INFO: Container NAME live-system-postgres-1
2024-10-21 03:50:03,940 - INFO: 2024-10-21 03:50:03,939 - INFO: Container NAME live-system-postgres-1
2024-10-21 03:50:03,940 - INFO: 2024-10-21 03:50:03,940 - INFO:  - postgres (is_ready=True) -> /backup/databases/postgres/test-postgres.sql
2024-10-21 03:50:03,940 - INFO: 2024-10-21 03:50:03,940 - INFO: service: mariadb
2024-10-21 03:50:03,941 - INFO: 2024-10-21 03:50:03,940 - INFO: Container NAME live-system-mariadb-1
2024-10-21 03:50:03,948 - INFO: 2024-10-21 03:50:03,948 - INFO:  - mariadb (is_ready=True) -> /backup/databases/mariadb/all_databases.sql
2024-10-21 03:50:03,948 - INFO: 2024-10-21 03:50:03,948 - INFO: service: web
2024-10-21 03:50:03,949 - INFO: 2024-10-21 03:50:03,948 - INFO:  - volume: /workspace/restic-compose-backup/src/tests -> /backup/volumes/web/srv/tests
2024-10-21 03:50:03,949 - INFO: 2024-10-21 03:50:03,948 - INFO: -------------------------------------------------------------------
2024-10-21 03:50:03,949 - INFO: 2024-10-21 03:50:03,948 - INFO: Backing up databases
2024-10-21 03:50:03,949 - INFO: 2024-10-21 03:50:03,948 - INFO: Backing up postgres in service postgres
2024-10-21 03:50:03,950 - INFO: 2024-10-21 03:50:03,948 - INFO: Container NAME live-system-postgres-1
2024-10-21 03:50:03,950 - INFO: 2024-10-21 03:50:03,948 - INFO: Container NAME live-system-postgres-1
2024-10-21 03:50:03,950 - INFO: 2024-10-21 03:50:03,948 - INFO: Backing PostgresContainer container postgres /backup/databases/postgres/test-postgres.sql
2024-10-21 03:50:03,950 - INFO: 2024-10-21 03:50:03,948 - INFO: Container NAME live-system-postgres-1
2024-10-21 03:50:03,951 - INFO: 2024-10-21 03:50:03,949 - INFO: Container NAME live-system-postgres-1
2024-10-21 03:50:03,951 - INFO: 2024-10-21 03:50:03,949 - INFO: Container NAME live-system-postgres-1
2024-10-21 03:50:04,145 - INFO: 2024-10-21 03:50:04,144 - INFO: Database backup exit code: =======> 0
2024-10-21 03:50:04,145 - INFO: 2024-10-21 03:50:04,145 - INFO: Exit code: 0
2024-10-21 03:50:04,146 - INFO: 2024-10-21 03:50:04,145 - INFO: Backing up mariadb in service mariadb
2024-10-21 03:50:04,146 - INFO: 2024-10-21 03:50:04,145 - INFO: Container NAME live-system-mariadb-1
2024-10-21 03:50:04,146 - INFO: 2024-10-21 03:50:04,145 - INFO: Container NAME live-system-mariadb-1
2024-10-21 03:50:04,348 - INFO: 2024-10-21 03:50:04,347 - INFO: Database backup exit code: =======> 0
2024-10-21 03:50:04,348 - INFO: 2024-10-21 03:50:04,347 - INFO: Exit code: 0
2024-10-21 03:50:04,348 - INFO: 2024-10-21 03:50:04,347 - INFO: Backup files from ===> /backup/
2024-10-21 03:50:05,112 - INFO: 2024-10-21 03:50:05,111 - INFO: Forget outdated snapshots
2024-10-21 03:50:05,821 - INFO: 2024-10-21 03:50:05,821 - INFO: Prune stale data freeing storage space
2024-10-21 03:50:06,456 - INFO: 2024-10-21 03:50:06,455 - INFO: Checking the repository for errors
2024-10-21 03:50:07,070 - INFO: 2024-10-21 03:50:07,070 - INFO: Backup completed
2024-10-21 03:50:07,193 - INFO: Backup container exit code: 0
```

Check the databases

```docker exec -it live-system-mariadb-1  bash```

```mysql -uroot -pmy-secret-pw```

```show databases;```

```
+--------------------+
| Database           |
+--------------------+
| classicmodels      |
| information_schema |
| mydb-mariadb       |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.001 sec)
```


Stop the live system to avoid conflicts as the backup service may try to backup the restored system (The backup and restore services are not intended to run on the same system)

```./stop-live-system.sh```

Run the restore 

```./restore-backup.sh```

Check the restore logs

```docker logs -f restore-test-restore-1```

You should see logs similar to:

```
2024-10-21 03:58:19,579 - INFO: Running:====> False

2024-10-21 03:58:19,579 - INFO: Starting Restore container
2024-10-21 03:58:19,864 - INFO: Restore process container: charming_cohen
2024-10-21 03:58:20,074 - INFO: 2024-10-21 03:58:20,073 - INFO: Status for compose project 'restore-test'
2024-10-21 03:58:20,074 - INFO: 2024-10-21 03:58:20,073 - INFO: Repository: '/restic_data'
2024-10-21 03:58:20,074 - INFO: 2024-10-21 03:58:20,073 - INFO: Restore currently running?: True
2024-10-21 03:58:20,074 - INFO: 2024-10-21 03:58:20,074 - INFO: Include project name in restore path?: False
2024-10-21 03:58:20,075 - INFO: 2024-10-21 03:58:20,074 - INFO: Checking docker availability
2024-10-21 03:58:20,698 - INFO: 2024-10-21 03:58:20,697 - INFO: ------------------------- Detected Config -------------------------
2024-10-21 03:58:20,698 - INFO: 2024-10-21 03:58:20,697 - INFO: service: web
2024-10-21 03:58:20,698 - INFO: 2024-10-21 03:58:20,697 - INFO: service: postgres
2024-10-21 03:58:20,698 - INFO: 2024-10-21 03:58:20,698 - INFO: Container NAME restore-test-postgres-1
2024-10-21 03:58:20,704 - INFO: 2024-10-21 03:58:20,703 - INFO: Container NAME restore-test-postgres-1
2024-10-21 03:58:20,704 - INFO: 2024-10-21 03:58:20,703 - INFO:  - postgres (is_ready=True) -> /backup/databases/postgres/test-postgres.sql
2024-10-21 03:58:20,704 - INFO: 2024-10-21 03:58:20,703 - INFO: service: mariadb
2024-10-21 03:58:20,704 - INFO: 2024-10-21 03:58:20,703 - INFO: Container NAME restore-test-mariadb-1
2024-10-21 03:58:20,709 - INFO: 2024-10-21 03:58:20,708 - INFO:  - mariadb (is_ready=True) -> /backup/databases/mariadb/all_databases.sql
2024-10-21 03:58:20,709 - INFO: 2024-10-21 03:58:20,708 - INFO: -------------------------------------------------------------------
2024-10-21 03:58:20,709 - INFO: 2024-10-21 03:58:20,708 - INFO: Restoring databases
2024-10-21 03:58:20,710 - INFO: 2024-10-21 03:58:20,709 - INFO: Restoring up postgres in service postgres
2024-10-21 03:58:20,710 - INFO: 2024-10-21 03:58:20,709 - INFO: Container NAME restore-test-postgres-1
2024-10-21 03:58:20,710 - INFO: 2024-10-21 03:58:20,709 - INFO: Container NAME restore-test-postgres-1
2024-10-21 03:58:20,710 - INFO: 2024-10-21 03:58:20,709 - INFO: Container NAME restore-test-postgres-1
2024-10-21 03:58:20,710 - INFO: 2024-10-21 03:58:20,709 - INFO: Container NAME restore-test-postgres-1
2024-10-21 03:58:20,711 - INFO: 2024-10-21 03:58:20,709 - INFO: Database restore_command: =======> restic -r /restic_data dump latest /backup/databases/postgres/test-postgres.sql | psql --host=restore-test-postgres-1 --port=5432 --username=pguser --dbname=postgres
2024-10-21 03:58:21,321 - INFO: SET
2024-10-21 03:58:21,321 - INFO: SET
2024-10-21 03:58:21,321 - INFO: SET
2024-10-21 03:58:21,322 - INFO: ERROR:  role "pguser" already exists
2024-10-21 03:58:21,322 - INFO: ALTER ROLE
2024-10-21 03:58:21,332 - INFO: You are now connected to database "template1" as user "pguser".
2024-10-21 03:58:21,332 - INFO: SET
2024-10-21 03:58:21,332 - INFO: SET
2024-10-21 03:58:21,332 - INFO: SET
2024-10-21 03:58:21,332 - INFO: SET
2024-10-21 03:58:21,332 - INFO: SET
2024-10-21 03:58:21,333 - INFO:  set_config
2024-10-21 03:58:21,333 - INFO: ------------
2024-10-21 03:58:21,333 - INFO: 
2024-10-21 03:58:21,333 - INFO: (1 row)
2024-10-21 03:58:21,333 - INFO: 
2024-10-21 03:58:21,334 - INFO: SET
2024-10-21 03:58:21,334 - INFO: SET
2024-10-21 03:58:21,334 - INFO: SET
2024-10-21 03:58:21,334 - INFO: SET
2024-10-21 03:58:21,334 - INFO: ALTER SCHEMA
2024-10-21 03:58:21,334 - INFO: REVOKE
2024-10-21 03:58:21,335 - INFO: GRANT
2024-10-21 03:58:21,338 - INFO: You are now connected to database "postgres" as user "pguser".
2024-10-21 03:58:21,338 - INFO: SET
2024-10-21 03:58:21,338 - INFO: SET
2024-10-21 03:58:21,338 - INFO: SET
2024-10-21 03:58:21,339 - INFO: SET
2024-10-21 03:58:21,339 - INFO: SET
2024-10-21 03:58:21,340 - INFO:  set_config
2024-10-21 03:58:21,340 - INFO: ------------
2024-10-21 03:58:21,340 - INFO: 
2024-10-21 03:58:21,340 - INFO: (1 row)
2024-10-21 03:58:21,340 - INFO: 
2024-10-21 03:58:21,340 - INFO: SET
2024-10-21 03:58:21,340 - INFO: SET
2024-10-21 03:58:21,340 - INFO: SET
2024-10-21 03:58:21,340 - INFO: SET
2024-10-21 03:58:21,340 - INFO: ALTER SCHEMA
2024-10-21 03:58:21,341 - INFO: REVOKE
2024-10-21 03:58:21,341 - INFO: GRANT
2024-10-21 03:58:21,342 - INFO: SET
2024-10-21 03:58:21,342 - INFO: SET
2024-10-21 03:58:21,342 - INFO: SET
2024-10-21 03:58:21,342 - INFO: SET
2024-10-21 03:58:21,342 - INFO: SET
2024-10-21 03:58:21,342 - INFO:  set_config
2024-10-21 03:58:21,342 - INFO: ------------
2024-10-21 03:58:21,342 - INFO: 
2024-10-21 03:58:21,342 - INFO: (1 row)
2024-10-21 03:58:21,342 - INFO: 
2024-10-21 03:58:21,343 - INFO: SET
2024-10-21 03:58:21,343 - INFO: SET
2024-10-21 03:58:21,343 - INFO: SET
2024-10-21 03:58:21,343 - INFO: SET
2024-10-21 03:58:21,343 - INFO: ERROR:  option "locale_provider" not recognized
2024-10-21 03:58:21,343 - INFO: LINE 1: ...gres" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PRO...
2024-10-21 03:58:21,343 - INFO:                                                              ^
2024-10-21 03:58:21,343 - INFO: ALTER DATABASE
2024-10-21 03:58:21,350 - INFO: You are now connected to database "test-postgres" as user "pguser".
2024-10-21 03:58:21,350 - INFO: SET
2024-10-21 03:58:21,350 - INFO: SET
2024-10-21 03:58:21,350 - INFO: SET
2024-10-21 03:58:21,350 - INFO: SET
2024-10-21 03:58:21,351 - INFO: SET
2024-10-21 03:58:21,351 - INFO:  set_config
2024-10-21 03:58:21,351 - INFO: ------------
2024-10-21 03:58:21,351 - INFO: 
2024-10-21 03:58:21,351 - INFO: (1 row)
2024-10-21 03:58:21,352 - INFO: 
2024-10-21 03:58:21,352 - INFO: SET
2024-10-21 03:58:21,352 - INFO: SET
2024-10-21 03:58:21,352 - INFO: SET
2024-10-21 03:58:21,352 - INFO: SET
2024-10-21 03:58:21,352 - INFO: CREATE SCHEMA
2024-10-21 03:58:21,353 - INFO: ALTER SCHEMA
2024-10-21 03:58:21,353 - INFO: ALTER SCHEMA
2024-10-21 03:58:21,354 - INFO: CREATE TYPE
2024-10-21 03:58:21,354 - INFO: ALTER TYPE
2024-10-21 03:58:21,354 - INFO: SET
2024-10-21 03:58:21,354 - INFO: SET
2024-10-21 03:58:21,355 - INFO: CREATE TABLE
2024-10-21 03:58:21,356 - INFO: ALTER TABLE
2024-10-21 03:58:21,357 - INFO: CREATE TABLE
2024-10-21 03:58:21,357 - INFO: ALTER TABLE
2024-10-21 03:58:21,358 - INFO: CREATE TABLE
2024-10-21 03:58:21,358 - INFO: ALTER TABLE
2024-10-21 03:58:21,359 - INFO: CREATE TABLE
2024-10-21 03:58:21,359 - INFO: ALTER TABLE
2024-10-21 03:58:21,360 - INFO: CREATE SEQUENCE
2024-10-21 03:58:21,360 - INFO: ALTER SEQUENCE
2024-10-21 03:58:21,361 - INFO: ALTER SEQUENCE
2024-10-21 03:58:21,361 - INFO: CREATE TABLE
2024-10-21 03:58:21,362 - INFO: ALTER TABLE
2024-10-21 03:58:21,362 - INFO: CREATE TABLE
2024-10-21 03:58:21,363 - INFO: ALTER TABLE
2024-10-21 03:58:21,364 - INFO: ALTER TABLE
2024-10-21 03:58:21,364 - INFO: COPY 0
2024-10-21 03:58:21,364 - INFO: COPY 0
2024-10-21 03:58:21,364 - INFO: COPY 0
2024-10-21 03:58:21,364 - INFO: COPY 0
2024-10-21 03:58:21,365 - INFO: COPY 0
2024-10-21 03:58:21,365 - INFO: COPY 0
2024-10-21 03:58:21,365 - INFO:  setval
2024-10-21 03:58:21,365 - INFO: --------
2024-10-21 03:58:21,365 - INFO:       1
2024-10-21 03:58:21,365 - INFO: (1 row)
2024-10-21 03:58:21,365 - INFO: 
2024-10-21 03:58:21,367 - INFO: ALTER TABLE
2024-10-21 03:58:21,368 - INFO: ALTER TABLE
2024-10-21 03:58:21,370 - INFO: ALTER TABLE
2024-10-21 03:58:21,371 - INFO: ALTER TABLE
2024-10-21 03:58:21,372 - INFO: ALTER TABLE
2024-10-21 03:58:21,374 - INFO: ALTER TABLE
2024-10-21 03:58:21,375 - INFO: CREATE INDEX
2024-10-21 03:58:21,376 - INFO: CREATE INDEX
2024-10-21 03:58:21,377 - INFO: CREATE INDEX
2024-10-21 03:58:21,379 - INFO: ALTER TABLE
2024-10-21 03:58:21,381 - INFO: ALTER TABLE
2024-10-21 03:58:21,382 - INFO: ALTER TABLE
2024-10-21 03:58:21,383 - INFO: ALTER TABLE
2024-10-21 03:58:21,384 - INFO: ALTER TABLE
2024-10-21 03:58:21,385 - INFO: ALTER TABLE
2024-10-21 03:58:21,385 - INFO: REVOKE
2024-10-21 03:58:21,386 - INFO: GRANT
2024-10-21 03:58:21,388 - INFO: 2024-10-21 03:58:21,387 - INFO: Database Restore exit code: =======> 0
2024-10-21 03:58:21,388 - INFO: 2024-10-21 03:58:21,387 - INFO: Exit code: 0
2024-10-21 03:58:21,388 - INFO: 2024-10-21 03:58:21,388 - INFO: Restoring up mariadb in service mariadb
2024-10-21 03:58:21,388 - INFO: 2024-10-21 03:58:21,388 - INFO: Container NAME restore-test-mariadb-1
2024-10-21 03:58:21,389 - INFO: 2024-10-21 03:58:21,388 - INFO: Container NAME restore-test-mariadb-1
2024-10-21 03:58:21,389 - INFO: 2024-10-21 03:58:21,388 - INFO: Database restore_command: =======> restic -r /restic_data dump latest /backup/databases/mariadb/all_databases.sql | mysql --host=restore-test-mariadb-1 --port=3306 --user=root
2024-10-21 03:58:22,817 - INFO: 2024-10-21 03:58:22,816 - INFO: Database Restore exit code: =======> 0
2024-10-21 03:58:22,817 - INFO: 2024-10-21 03:58:22,817 - INFO: Exit code: 0
2024-10-21 03:58:22,817 - INFO: 2024-10-21 03:58:22,817 - INFO: Restoring files to ===> /restored_data/
2024-10-21 03:58:23,462 - INFO: 2024-10-21 03:58:23,461 - INFO: Restore completed
2024-10-21 03:58:23,541 - INFO: Restore container exit code: 0
```
 You can now check the databases for restored data, for example 

```docker exec -it restore-test-mariadb-1 bash``

```mysql -uroot -pmy-secret-pw```

```show databases;```

```
+--------------------+
| Database           |
+--------------------+
| classicmodels      |
| information_schema |
| mydb-mariadb       |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.001 sec)

```

Stop backup system

```./stop-backup-system.sh```

## Clean up

Remove Restored data:

```sudo rm -rf /workspace/restic-compose-backup/restored_data/backup```

Remove Backup Repo

```sudo rm -rf /workspace/restic-compose-backup/restic_data/{data,index,keys,locks,snapshots,config}```


