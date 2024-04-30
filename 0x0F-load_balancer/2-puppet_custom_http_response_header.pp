#!/usr/bin/env puppet
# Puppet manifest to add a custom HTTP header
class custom_http_response_header {

  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "server {
                   listen 80 default_server;
                   server_name _;
                   add_header X-Served-By \$hostname;
                   location / {
                       proxy_pass http://localhost:8080;
                   }
               }",
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
  }
}

include custom_http_response_header
