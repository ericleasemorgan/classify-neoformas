#!/usr/bin/env bash

# divide.sh - given a few configurations, move plain text files from one place to another

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# July 23, 2019 - first documentation; note All_neg and All_pos!


# configure
POSITIVE='./model/positive'
NEGATIVE='./model/negative'
PDF='./pdf'

# make file system
mkdir -p $POSITIVE
mkdir -p $NEGATIVE

rm -rf $POSITIVE/*.txt
rm -rf $NEGATIVE/*.txt

# do the work and done
mv $PDF/All_neg/*.txt $NEGATIVE
mv $PDF/All_pos/*.txt $POSITIVE
exit
