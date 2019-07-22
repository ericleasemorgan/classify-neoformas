#!/usr/bin/env bash

# clean.sh

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