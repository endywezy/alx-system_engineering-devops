#!/usr/bin/env bash
# Puppet manifest to add a custom HTTP header

exec { 'configure_nginx':
  command     => 'apt-get -y update && apt-get -y install nginx && sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $(hostname);" /etc/nginx/sites-available/default && service nginx restart',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}

