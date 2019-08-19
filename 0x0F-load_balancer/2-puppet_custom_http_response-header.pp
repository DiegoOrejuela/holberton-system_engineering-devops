# automate the task of creating a custom HTTP header response

exec { 'apt-update':
    command => '/usr/bin/apt-get -y update'
}

package { 'nginx':
    ensure => present,
}

exec { 'add HTTP header':
    command => '/bin/sed -i "14i\ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf'
}

exec { 'restart-nginx':
    command  => 'service nginx restart',
    provider => 'shell',
}


#sudo apt-get update
#sudo apt-get -y install nginx
#echo "Holberton School" >> /var/www/html/index.html
#sed -i "14i\ \tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf
#sudo service nginx restart
