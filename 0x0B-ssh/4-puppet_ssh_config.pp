exec { 'change_configuration_file':
     command => 'echo -e "	PasswordAuthentication no\n	IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
     path    => '/bin';
}
