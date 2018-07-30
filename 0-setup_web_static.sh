#!/usr/bin/env bash
# sets up web servers for deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static_releases/test /data/web_static/shared
echo "this is a test" | sudo tee /data/web_static_releases/test/index.html
sudo ln -sf /data/web_static_releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
msg="location /hbnb_static {\nalias /data/web_static/current;\n}\n"
sudo sed -i "40i $msg" /etc/nginx/sites-enabled/default
sudo service nginx restart
