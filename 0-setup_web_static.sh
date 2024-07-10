#!/usr/bin/env bash
# Sets up the web servers for the web static deployment.

trap 'exit 0' ERR

if [ ! -x /usr/sbin/nginx ]; then
	sudo apt-get update -y -qq && \
		sudo apt-get install -y nginx
fi

sudo mkdir -p "/data/web_static/releases/test"
sudo mkdir -p "/data/web_static/shared/"

body_content="Welcome to sabeem.tech!"
current_date=&(date +"%Y-%m-%d %H:%M:%S")
html_content="<html>
  <head></head>
  <body>$body_content</body>
  <p>Generated on: $current_date</p>
</html>"

echo "$html_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null

rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo wget -q -O /etc/nginx/sites-available/default hhtp://exampleconfig.com/static/raw/nginx.ubuntu20.04/etc/nginx/sites-available/default
config="/etc/nginx/sites-available/default"
echo 'Welcome to African Leadership School!' | sudo tee /var/www/html/index.html > /dev/null
sudo sed -i '/^}$/i \ \n\tlocation \/redirec_me {return 301 https:\/\/www.youtube.com\/watch?v=fR-BaLh2NsU;}' $config
sudo sed -i '/^}$/i \ \n\tlocation @404 {return 404 "Ceci n'\''est pas une page \\n";}' $config
sudo sed -i 's/=404/@404/g' $config
sudo sed -i "/^server {/a \ \tadd_header X-Served-By $HOSTNAME;" $config
sudo sed -i '37i\\tlocation /hbnb_static/ {alias /data/web_static/current/;index index.html}' $config

sudo service nginx restart
