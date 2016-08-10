#!/bin/bash

# This script checks the latest available versions of all cf_tools and updates the ones that have newer versions
# It depends on the following
#
# * curl
# * tar

# Directory to store all downloaded files
DWNLD_DIR="/srv/jas/data/download"

# Directory to temporarily store only the tools that have a newer version
LTS_VERS_DIR="/srv/jas/data/download/latest_cf_tools"

# Get latest available versions of each component -----------------------------------------------------------------------------------------------------------------------------------#

# cf_uaac
cf_uaac_version=$(curl -k -L https://api.github.com/repos/cloudfoundry/cf-uaac/releases/latest | grep tag_name | cut -d":" -f2 | tr -d '", ')

# cf_cli
cf_cli_version=$(curl -k -L https://api.github.com/repos/cloudfoundry/cli/releases/latest | grep tag_name | cut -d":" -f2 | tr -d '", ')

# cfops_binary
cfops_version=$(curl -k -L https://api.github.com/repos/pivotalservices/cfops/releases/latest | grep tag_name | cut -d":" -f2 | tr -d '", ')

# cfops-nfs-plugin
cfops_nfs_plugin_version=$(curl -k -L https://api.github.com/repos/pivotalservices/cfops-nfs-plugin/releases/latest | grep tag_name | cut -d":" -f2 | tr -d '", ')

# rabbit-mq-plugin
rabbit_mq_plugin_version=$(curl -k -L https://api.github.com/repos/pivotalservices/cfops-rabbitmq-plugin/releases/latest | grep tag_name | cut -d":" -f2 | tr -d '", ')

# redis-plugin
redis_plugin_version=$(curl -k -L https://api.github.com/repos/pivotalservices/cfops-redis-plugin/releases/latest | grep tag_name | cut -d":" -f2 | tr -d '", ')

# mysql-plugin
mysql_plugin_version=$(curl -k -L https://api.github.com/repos/pivotalservices/cfops-mysql-plugin/releases/latest | grep tag_name | cut -d":" -f2 | tr -d '", ')

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Cleanup dir with latest cf tools from the previous download before starting the new downloads
rm -f $LTS_VERS_DIR/cf*

### CF UAAC ###

# Check if newest version of cf_uaac is already downloaded, if not, download it.
if [ ! -f $DWNLD_DIR/cf-uaac-$cf_uaac_version.tar.gz ]; then \
curl -k -L -o $DWNLD_DIR/cf-uaac-$cf_uaac_version.tar.gz $(curl -k -L https://api.github.com/repos/cloudfoundry/cf-uaac/releases/latest | grep "tarball_url" |grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*") && \
cp $DWNLD_DIR/cf-uaac-$cf_uaac_version.tar.gz $LTS_VERS_DIR \
; fi

### CF CLI ###

# Check if newest version of cf_cli is already downloaded, if not, download it.
if [ ! -f $DWNLD_DIR/cf-cli-$cf_cli_version ]; then \
curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -zx && \
mv cf cf-cli-$cf_cli_version && \
cp $DWNLD_DIR/cf-cli-$cf_cli_version $LTS_VERS_DIR \
; fi

### Update CFOPS and Plugins ###

# Check if newest version of cfops is already downloaded, if not, download it.
if [ ! -f $DWNLD_DIR/cfops_binaries-$cfops_version.tgz ]; then \
curl -v -k -L -o $DWNLD_DIR/cfops_binaries-$cfops_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops/releases/latest | grep cfops_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*") && \
cp $DWNLD_DIR/cfops_binaries-$cfops_version.tgz $LTS_VERS_DIR \
; fi

## NFS-Plugin

# Check if newest version of nfs-plugin is already downloaded, if not, download it.
if [ ! -f $DWNLD_DIR/cfops-nfs-plugin_binaries-$cfops_nfs_plugin_version.tgz ]; then \
curl -v -k -L -o $DWNLD_DIR/cfops-nfs-plugin_binaries-$cfops_nfs_plugin_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops-nfs-plugin/releases/latest | grep cfops-nfs-plugin_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*") && \
cp $DWNLD_DIR/cfops-nfs-plugin_binaries-$cfops_nfs_plugin_version.tgz $LTS_VERS_DIR \
; fi

## RabbitMQ 

# Check if newest version of rabbit-mq-plugin is already downloaded, if not, download it.
if [ ! -f $DWNLD_DIR/cfops-rabbit-mq-plugin-binaries-$rabbit_mq_plugin_version.tgz ]; then \
curl -v -k -L -o $DWNLD_DIR/cfops-rabbit-mq-plugin-binaries-$rabbit_mq_plugin_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops-rabbitmq-plugin/releases/latest | grep cfops-rabbitmq-plugin_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*") && \
cp $DWNLD_DIR/cfops-rabbit-mq-plugin-binaries-$rabbit_mq_plugin_version.tgz $LTS_VERS_DIR \
; fi

## Redis plugin

# Check if newest version of redis-plugin is already downloaded, if not, download it.
if [ ! -f $DWNLD_DIR/cfops-redis-plugin_binaries-$redis_plugin_version.tgz ]; then \
curl -v -k -L -o $DWNLD_DIR/cfops-redis-plugin_binaries-$redis_plugin_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops-redis-plugin/releases/latest | grep cfops-redis-plugin_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*") && \
cp $DWNLD_DIR/cfops-redis-plugin_binaries-$redis_plugin_version.tgz $LTS_VERS_DIR \
; fi

## MySQL plugin

# Check if newest version of mysql-plugin is already downloaded, if not, download it.
if [ ! -f $DWNLD_DIR/cfops-mysql-plugin_binaries-$mysql_plugin_version.tgz ]; then \
curl -v -k -L -o $DWNLD_DIR/cfops-mysql-plugin_binaries-$mysql_plugin_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops-mysql-plugin/releases/latest | grep cfops-mysql-plugin_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*") && \
cp $DWNLD_DIR/cfops-mysql-plugin_binaries-$mysql_plugin_version.tgz $LTS_VERS_DIR \
; fi
