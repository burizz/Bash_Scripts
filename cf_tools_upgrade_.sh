#!/bin/bash

# The script checks if a newer version of each CF tools is available, if it is, update it.

UPDT_DIR="<Update Directory>"
BACKUP_DATE=$(date +"%Y%m%d%H")
CFOPS_INSTALL_PATH="<path>"
CFOPS_PLUGIN_DIR="<path>"
CF_OPS_BINARY="<path>"
UAAC_INSTALL_PATH="<path>"
CF_CLI_BINARY="/usr/bin/cf"

#### CF-CLI Update #### 
# Install is done via the source tar instaed of the rpm, because the RPM download links for cf_cli on Github are dynamically determined during downloaded and fetched from some random Amazon AWS URL.
# The Source tar just contains the binary to be replaced in /usr/bin/cf

if [ -e $UPDT_DIR/cf-cli* ]
then
    CURRENT_CF_CLI_VER=$($CF_CLI_BINARY -v | cut -d ' ' -f3 | cut -d "+" -f 1)
    cp $CF_CLI_BINARY $CF_CLI_BINARY"_backup_"$BACKUP_DATE"_version_"$CURRENT_CF_CLI_VER && rm -f $CF_CLI_BINARY
    cp $UPDT_DIR/cf-cli* $CF_CLI_BINARY && chmod +x $CF_CLI_BINARY
    echo "CF-CLI updated to -" $($CF_CLI_BINARY -v)
fi

#### UAAC Update ####

if [ -e $UPDT_DIR/cf_uaac_gem_cache_* ]
then
    tar xvf $UPDT_DIR/cf_uaac_gem_cache_*.tar.gz -C $UAAC_INSTALL_PATH --strip-components=1
    cd $UAAC_INSTALL_PATH/cache/
    # For Verbosity use - gem install --local *.gem --verbose
    gem install --local *.gem
    echo "UAAC Updated to -" $(/usr/bin/uaac -v)
    rm -rf $UAAC_INSTALL_PATH/cache/
fi


#### CFOPS Update ####

if [ -e $UPDT_DIR/cfops_binary* ]
then
    cp $CFOPS_INSTALL_PATH/cfops $CFOPS_INSTALL_PATH/cfops_backup_$BACKUP_DATE && rm -f $CFOPS_INSTALL_PATH/cfops
    cp $UPDT_DIR/cfops_binary* $CFOPS_INSTALL_PATH/cfops && chmod +x $CFOPS_INSTALL_PATH/cfops
    cp $CFOPS_INSTALL_PATH/cfops $CF_OPS_BINARY
    echo "CFOPS updated to -" $($CFOPS_INSTALL_PATH/cfops version)
fi

## CFOPS Plugins Update ##

# MySQL Plugin
if [ -e $UPDT_DIR/cfops-mysql-plugin_binaries* ]
then
    cp $CFOPS_PLUGIN_DIR/cfops-mysql-plugin $CFOPS_PLUGIN_DIR/cfops-mysql-plugin_backup_$BACKUP_DATE
    tar xvf $UPDT_DIR/cfops-mysql-plugin_binaries* -C $UPDT_DIR/
    cp $UPDT_DIR/pipeline/output/builds/linux64/cfops-mysql-plugin* $CFOPS_PLUGIN_DIR/cfops-mysql-plugin
    rm -rf $UPDT_DIR/pipeline
fi

# NFS Plugin
if [ -e $UPDT_DIR/cfops-nfs-plugin_binaries* ]
then
    cp $CFOPS_PLUGIN_DIR/cfops-nfs-plugin $CFOPS_PLUGIN_DIR/cfops-nfs-plugin_backup_$BACKUP_DATE
    tar xvf $UPDT_DIR/cfops-nfs-plugin_binaries* -C $UPDT_DIR/
    cp $UPDT_DIR/pipeline/output/builds/linux64/cfops-nfs-plugin* $CFOPS_PLUGIN_DIR/cfops-nfs-plugin
    rm -rf $UPDT_DIR/pipeline
fi

# RabbitMQ Plugin
if [ -e $UPDT_DIR/cfops-rabbit-mq-plugin-binaries* ]
then
    cp $CFOPS_PLUGIN_DIR/cfops-rabbitmq-plugin $CFOPS_PLUGIN_DIR/cfops-rabbitmq-plugin_backup_$BACKUP_DATE
    tar xvf $UPDT_DIR/cfops-rabbit-mq-plugin-binaries* -C $UPDT_DIR/
    cp $UPDT_DIR/pipeline/output/linux64/cfops-rabbitmq-plugin* $CFOPS_PLUGIN_DIR/cfops-rabbitmq-plugin
    rm -rf $UPDT_DIR/pipeline
fi

# Redis Plugin
if [ -e $UPDT_DIR/cfops-redis-plugin_binaries* ]
then
    cp $CFOPS_PLUGIN_DIR/cfops-redis-plugin $CFOPS_PLUGIN_DIR/cfops-redis-plugin_backup_$BACKUP_DATE
    tar xvf $UPDT_DIR/cfops-redis-plugin_binaries* -C $UPDT_DIR/
    cp $UPDT_DIR/pipeline/output/builds/linux64/cfops-redis-plugin* $CFOPS_PLUGIN_DIR/cfops-redis-plugin
    rm -rf $UPDT_DIR/pipeline
fi

# Cleanup update_dir after the updates have finished
rm -f $UPDT_DIR/*
