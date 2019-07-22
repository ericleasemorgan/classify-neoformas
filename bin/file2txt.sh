#!/usr/bin/env bash

# file2txt.sh - convert a given file to plain text; a front-end to file2txt.py

# Eric Lease Morgan <emorgan@nd.edu>
# January 8, 2019 - first cut, more or less


# configure
FILE2TXT='./bin/file2txt.py'

# sanity check
if [[ -z "$1" ]]; then
	echo "Usage: $0 <file>" >&2
	exit
fi

# get input
FILE=$1

# compute output
ORIGINAL=$( dirname "${FILE}" )
LEAF=$( basename "$FILE" )
LEAF=${LEAF%.*}
OUTPUT="$ORIGINAL/$LEAF.txt"

# do the work and done
$FILE2TXT "$FILE" > "$OUTPUT"
exit