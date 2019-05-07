#!/usr/bin/env bash

# pdf2txt.sh

TIKA='./etc/tika-server.jar'
FILE2TXT='./bin/file2txt.sh'
PDF='./pdf'

# start Tika
java -jar $TIKA &
PID=$!
sleep 10

# do the work
find $PDF -name '*.pdf' | parallel $FILE2TXT {}

# clean up and done
kill $PID
exit
