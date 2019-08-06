# Let’s practice using Puppet to make changes to our configuration file
exec { 'change_configuration_file':
  command => '/bin/echo -e "PasswordAuthentication no\nIdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
  path    => '/usr/bin';
}
