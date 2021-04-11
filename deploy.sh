tmp/venv/bin/python manage.py migrate
./permissions.sh
npm run build
systemctl restart apache2
