#!/bin/bash

# Set timestamp to be used for directory name
BACKUP_DATE=$(date +"%Y%m%d%H")

# Path where backups will be stored.
BACKUPDIR="/srv/jas/data/backup"

# Path to cfops cmd binary
BACKUP_TOOL_PATH="/srv/jas/app/cfops"

# Path to log of the Backup process
BACKUP_LOG_PATH="/srv/jas/logs/backup"

# Name of backup_log
BACKUP_LOG_FILE="backup_log_$BACKUP_DATE.out"

echo "#######################################################" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
echo "#              BEGINNING BACKUP PROCESS               #" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
echo "#######################################################" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

# Go into Cfops app Dir, because otherwise it does not find its plugins
cd $BACKUP_TOOL_PATH

# Backup each tile and send STDOUT, STDERR to log files as well as a bunch of echo's that log when each process is started and finished if successful.
echo "Backing up - ops-manager tile" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
$BACKUP_TOOL_PATH/cfops backup --tile ops-manager --destination $BACKUPDIR/backup_$BACKUP_DATE/ 2>&1 | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE && echo "ops-manager backed up successfully" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

echo "Backing up - elastic-runtime tile" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
$BACKUP_TOOL_PATH/cfops backup --tile elastic-runtime -d $BACKUPDIR/backup_$BACKUP_DATE/ 2>&1 | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE && echo "elastic-runtime backed up successfully" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

echo "Backing up - mysql-tile tile" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
$BACKUP_TOOL_PATH/cfops backup --tile mysql-tile -d $BACKUPDIR/backup_$BACKUP_DATE/ 2>&1 | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE && echo "mysql-tile backed up successfully" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

echo "Backing up - rabbitmq tile" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
$BACKUP_TOOL_PATH/cfops backup --tile rabbitmq -d $BACKUPDIR/backup_$BACKUP_DATE/ 2>&1 | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE && echo "rabbitmq backed up successfully" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

echo "Backing up - redis-tile tile" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
$BACKUP_TOOL_PATH/cfops backup --tile redis-tile -d $BACKUPDIR/backup_$BACKUP_DATE/ 2>&1 | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE && echo "redis-tile backed up successfully" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

# Appended for readability of the log file
echo "#######################################################" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

# Archive and compress the backup and remove the folder
echo "Archiving Backup folder - $BACKUPDIR/backup_$BACKUP_DATE/" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
tar czvf $BACKUPDIR/backup_$BACKUP_DATE.tar.gz $BACKUPDIR/backup_$BACKUP_DATE/ && rm -rf $BACKUPDIR/backup_$BACKUP_DATE/ && echo "Successfully created backup archive - $BACKUPDIR/backup_$BACKUP_DATE.tar.gz" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

# Remove older backup archives
echo "Removing oldest backup" - `find $BACKUPDIR -name "backup_*" -type f -mtime +14` | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
find $BACKUPDIR -name "backup_*" -type f -mtime +13 -delete && echo "Oldest backup removed successfully" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

# Remove older backup log files
echo "Removing oldest log file" - `find $BACKUP_LOG_PATH -name "backup_log*" -type f -mtime +15` | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
find $BACKUP_LOG_PATH -name "backup_log*" -type f -mtime +14 -delete && echo "Oldest backup logfile removed successfully" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE

echo "#######################################################" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
echo "#                  BACKUP FINISHED                    #" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
echo "#######################################################" | tee -a $BACKUP_LOG_PATH/$BACKUP_LOG_FILE
