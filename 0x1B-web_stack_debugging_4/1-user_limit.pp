#Change the OS configuration so that it is possible to login with the holberton
#user and open a file without any error message.

exec {'change-os-configuration-for-holberton-user':
  command  => "sed -i 's/nofile 5/nofile 1000/g' /etc/security/limits.conf;\
              sed -i 's/nofile 4/nofile 1000/g' /etc/security/limits.conf",
  provider => 'shell';
}
