#!/usr/bin/env bashi
# Define SSH client configuration class
class ssh_client_config {

  # Ensure SSH client configuration directory exists
  file { '/home/ubuntu/.ssh':
    ensure  => 'directory',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0700',
    require => File['/home/ubuntu'],
  }

  # Ensure SSH client configuration file exists
  file { '/home/ubuntu/.ssh/config':
    ensure  => 'file',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0600',
    content => template('ssh_client/config.erb'),
    require => File['/home/ubuntu/.ssh'],
  }
}

# Template for SSH client configuration
file { '/etc/puppetlabs/code/modules/ssh_client/templates/config.erb':
  ensure  => 'file',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "
Host *
    PubkeyAuthentication yes
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
",
}
