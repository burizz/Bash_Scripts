#!/bin/bash

# This script checks the latest available versions of all cf_tools and updates the ones that have newer versions
# It depends on the following
#
# * curl
# * tar
# * grep

BASE_DIR=`pwd`

# Get latest versions of each component -----------------------------------------------------------------------------------------------------------------------------------#

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

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

### Update CF UAAC if a newer version is available ###

# Check if version is newest
if $cf_uaac_version

# Download latest cf_uaac_version
curl -k -L -o cf-uaac-$cf_uaac_version.tar.gz $(curl -k -L https://api.github.com/repos/cloudfoundry/cf-uaac/releases/latest | grep "tarball_url" |grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*")

###  ###

### Update CF CLI and its Plugins if newer versions are available ###

# Check if version is newest
if $cf_cli_version

# Download latest binary
curl -L "https://cli.run.pivotal.io/stable?release=linux64-binary&source=github" | tar -zx

# Check version
./cf version

### ###

### Update CFOPS and its Plugins if newer versions are available ###

# Check if version is newest
if $cfops_version

# Download latest cfops binary 
curl -v -k -L -o cfops_binaries-$cfops_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops/releases/latest | grep cfops_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*")

## NFS-Plugin

# Check if version is newest
if $cfops_nfs_plugin_version

curl -v -k -L -o cfops-nfs-plugin_binaries-$cfops_nfs_plugin_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops-nfs-plugin/releases/latest | grep cfops-nfs-plugin_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*")

## RabbitMQ 

# Check if version is newest
if $rabbit_mq_plugin_version

curl -v -k -L -o cfops-nfs-plugin_binaries-$rabbit_mq_plugin_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops-rabbitmq-plugin/releases/latest | grep cfops-rabbitmq-plugin_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*")

## Redis plugin

# Check if version is newest
if $redis_plugin_version

curl -v -k -L -o cfops-redis-plugin_binaries-$redis_plugin_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops-redis-plugin/releases/latest | grep cfops-redis-plugin_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*")

## MySQL plugin

# Check if version is newest
if $mysql_plugin_version

curl -v -k -L -o cfops-mysql-plugin_binaries-$mysql_plugin_version.tgz $(curl -s -k -L https://api.github.com/repos/pivotalservices/cfops-mysql-plugin/releases/latest | grep cfops-mysql-plugin_binaries.tgz | grep browser_download_url | grep -Eo "(http|https)://[\da-z./?A-Z0-9\D=_-]*")
