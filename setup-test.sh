###
# run this script after cloning the repo to setup the server
# this script is optimized for debian servers
###

# variables
SITE_URL="test.cocoo.de"

# dirs
mkdir tmp/
mkdir tmp/static
mkdir tmp/media
mkdir tmp/logs
touch tmp/secrets.json

# create venv and install deps
python3 -m venv tmp/venv
source tmp/venv/bin/activate
pip install -r requirements.txt

# setup apache configs
certbot certonly --apache -d $SITE_URL --register-unsafely-without-email
ln -s /home/$SITE_URL/apache.test.conf /etc/apache2/sites-available/$SITE_URL.conf
a2ensite $SITE_URL.conf
systemctl restart apache2
