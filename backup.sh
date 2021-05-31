TODAY=`date +'%Y-%m-%d'`
FILENAME="tmp/backup/${TODAY}.sqlite3"
cp tmp/db.sqlite3 ${FILENAME}
echo $FILENAME
