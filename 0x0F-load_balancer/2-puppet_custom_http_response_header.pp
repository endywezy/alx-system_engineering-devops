#!/usr/bin/env bash
# File: 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define custom HTTP header response
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                server_name _;

                location / {
                    add_header X-Served-By $hostname;
                    # Your other configuration directives here
                    root /var/www/html;
                    index index.html index.htm;
                }
            }",
}

# Ensure Nginx service is running
service { 'nginx':
  ensure => running,
}
