###
# run this script after cloning the repo to setup the server
###

# variables
SITE_URL="cocoo.de"
SITE_WWW_URL="www.$SITE_URL"

# dirs
mkdir tmp/
mkdir tmp/static
mkdir tmp/media
mkdir tmp/logs
touch tmp/secrets.json

# install everything
apt update
apt install python3-pip python3-venv python3-dev apache2 libapache2-mod-wsgi-py3 libpq-dev snapd gettext libjpeg-dev zlib1g-dev
snap install core
snap refresh core
snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot

# create venv and install deps
python3 -m venv tmp/venv
source tmp/venv/bin/activate
pip install -r requirements.txt

# setup apache configs
# certbot certonly --apache -d $SITE_URL -d $SITE_WWW_URL --register-unsafely-without-email
a2enmod ssl
a2enmod rewrite
ln -s /home/$SITE_URL/apache.conf /etc/apache2/sites-available/$SITE_URL.conf
# a2ensite $SITE_URL.conf
# systemctl restart apache2
