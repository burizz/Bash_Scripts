#!/bin/bash

# This script copies the latest available cf tools archives and copies them to PCF servers for update.

# Server where latest cf tools archives are automatically downloaded
SRC_SERVER="sndcapcf0050"

# Dir on download server where latest cf tools are available
SRC_DIR="/srv/jas/data/download/latest_cf_tools"

# Location on hopping server to store cf tools archives for copying to scripting hosts
TMP_DWNLD_DIR="/export/home/b/byakimo/cf_tools"

# Destination servers to copy to - can add to server list by appending hostnames to the array
DEST_SRV=(sndcmpcf0000 sndcmpcf0010)

# Destination directory within destination server to copy to
DEST_DIR="/srv/jas/data/download/for_update"

# Copy latest cf tools archives from download server to hopping server
cop $SRC_SERVER:$SRC_DIR/cf* $TMP_DWNLD_DIR/ &> /dev/null

# Check if no files were downloaded in temp dir
if [ "$(ls -A $TMP_DWNLD_DIR)" ]; then
     echo "Latest CF Tools are being copied to PCF servers"
	 
	 # Copy from hopping to destination servers
     for srv_name in "${DEST_SRV[@]}"
     do
         cop $TMP_DWNLD_DIR/cf* $srv_name:$DEST_DIR/ &> /dev/null 
     done
	 
else
    echo "There are no new versions to be copied to PCF servers"
fi

# Cleanup all temp download dir after files are copied
rm -f $TMP_DWNLD_DIR/cf* &> /dev/null
