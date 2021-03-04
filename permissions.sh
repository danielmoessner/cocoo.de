chown -R root:www-data /home/cocoo_project
chmod -R 750 /home/cocoo_project
find /home/cocoo_project -type f -print0|xargs -0 chmod 740
chmod -R 770 /home/cocoo_project/tmp/media
find /home/cocoo_project/tmp/media -type f -print0|xargs -0 chmod 760
chmod 770 /home/cocoo_project/tmp/logs
chmod -R 760 /home/cocoo_project/tmp/logs/*
chmod 770 /home/cocoo_project/tmp
chmod -R 760 /home/cocoo_project/tmp/db.sqlite3
