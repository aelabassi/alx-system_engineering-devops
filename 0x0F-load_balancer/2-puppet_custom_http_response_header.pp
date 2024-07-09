# http header custom response
exec { 'command':
  command  => 'sudo apt-get -y update,
  sudo apt-get -y nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
