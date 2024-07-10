#!/usr/bin/env bash
# Sets up the web servers for the web static deployment.

if [ ! -x /usr/sbin/nginx ]; then
	sudo apt-get update -y -qq && \
		sudo apt-get install -y nginx
fi

sudo mkdir -p /data/web_static/releases/test data/web_static/shared/

body_content="Welcome to sabeem.tech!"
current_date=&(date +"%Y-%m-%d %H:%M:%S")
html_content="<html>
  <head></head>
  <body>$body_content</body>
  <p>Generated on: $current_date</p>
</html>"

echo "$html_content" | sudo tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo cp /etc/nginx/sites-available/default nginx-sites-available_default.backup

sudo sed -i '37i\\tloaction /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
