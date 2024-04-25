package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask',  # Install latest version
  unless => '/usr/bin/pip3 show flask',       # Check for any Flask installation
  require => Package['python3-pip'],
  onFailure => { loglevel => 'err', message => 'Failed to install Flask' },
}

