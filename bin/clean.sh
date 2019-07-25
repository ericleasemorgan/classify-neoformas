#!/usr/bin/env bash

# clean.sh - given a directory, recursively normalize all .txt files 

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# July 23, 2019 - first documentation
# July 25, 2019 - added de-hypenation


# configure
DIRECTORY='./model'

# change case
find $DIRECTORY -name '*.txt' -exec perl -pe '$_ =  lc( $_ )' -i {} \;

# remove digits, punctation, and multiple spaces
find $DIRECTORY -name '*.txt' -exec perl -pe '$_ =~ s/-\n//g'          -i {} \;
find $DIRECTORY -name '*.txt' -exec perl -pe '$_ =~ s/\d/ /g'          -i {} \;
find $DIRECTORY -name '*.txt' -exec perl -pe '$_ =~ s/[[:punct:]]/ /g' -i {} \;
find $DIRECTORY -name '*.txt' -exec perl -pe '$_ =~ s/ +/ /g'          -i {} \;

# done
exit