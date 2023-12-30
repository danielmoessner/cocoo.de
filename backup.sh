# backup db
TODAY=`date +'%Y-%m-%d'`
FILENAME="tmp/backup/${TODAY}.sqlite3"
cp tmp/db.sqlite3 ${FILENAME}
echo $FILENAME

# delete old backups
PREVIOUS=`date -d '1 year ago' +%Y`
find tmp/backup/ -name "${PREVIOUS}-*" -exec rm {} \;
