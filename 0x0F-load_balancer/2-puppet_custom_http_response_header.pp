#!/usr/bin/env bash
# Puppet manifest to add a custom HTTP header

exec { 'command':
command  => 'apt-get -y update;
	apt-get -y install nginx;
	sed -i "/listen 80 default_server;/a add_header X-Served-By ${::hostname};" /etc/nginx/sites-available/default;
	service nginx restart',
  provider => shell,
  path     => '/usr/bin:/bin', # Set proper PATH to avoid potential issues
  require  => Package['nginx'], # Ensure Nginx is installed before executing this command
}
