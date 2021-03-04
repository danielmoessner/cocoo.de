TODAY=`date +'%Y-%m-%d'`
FILENAME="/home/cocoo_project/tmp/backup/${TODAY}.sqlite3"
cp /home/cocoo_project/tmp/db.sqlite3 ${FILENAME}
echo $FILENAME
