#!/usr/bin/env bash

# clean.sh - given a directory, recursively normalize all .txt files 

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# July 23, 2019 - first documentation


# configure
DIRECTORY='./model'

# change case
find $DIRECTORY -name '*.txt' -exec perl -pe '$_ =  lc( $_ )' -i {} \;

# remove digits, punctation, and multiple spaces
find $DIRECTORY -name '*.txt' -exec perl -pe '$_ =~ s/\d/ /g'          -i {} \;
find $DIRECTORY -name '*.txt' -exec perl -pe '$_ =~ s/[[:punct:]]/ /g' -i {} \;
find $DIRECTORY -name '*.txt' -exec perl -pe '$_ =~ s/ +/ /g'          -i {} \;

# done
exit