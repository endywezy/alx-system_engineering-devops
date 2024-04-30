#!/usr/bin/env bash
# File: 2-puppet_custom_http_response_header.pp

exec { 'configure_custom_http_header':
  command  => 'apt-get -y update; \
               apt-get -y install nginx; \
               sed -i "/listen 80 default_server;/a add_header X-Served-By ${hostname};" /etc/nginx/sites-available/default; \
               service nginx restart',
  provider => shell,
  path     => '/usr/bin:/bin', # Set proper PATH to avoid potential issues
  require  => Package['nginx'], # Ensure Nginx is installed before executing this command
}
