#!/usr/bin/env bash
# Puppet manifest to add a custom HTTP header

# Define a class for Nginx configuration with custom header
class custom_http_response_header {

  # Ensure the nginx package is installed
  package { 'nginx': ensure => present }

  # Define a server block named 'default' with custom header
  nginx::server {
    name => 'default'
    listen => [80]

    # Configure the location block
    location / {
      # Add the custom header using add_header
      add_header => { 'X-Served-By' => '$hostname' }

      # Optional: Configure proxy pass if needed
      # proxy_pass http://localhost:8080;
    }
  }

  # Ensure the service is restarted after configuration changes
  service { 'nginx': ensure => running, restart => true }
}

# Include the custom_http_response_header class on the managed node
class { 'custom_http_response_header': }

