git reset --hard HEAD
git pull
tmp/venv/bin/python manage.py migrate
./permissions.sh
npm run css
npm run js
tmp/venv/bin/python manage.py collectstatic --clear --noinput
systemctl restart apache2
