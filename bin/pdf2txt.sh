#!/usr/bin/env bash

# pdf2txt.sh - launch Tika and feed it files to convert to plain text; a front-end to file2txt.sh

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# July 22, 2019 - first documentation


# configure
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
