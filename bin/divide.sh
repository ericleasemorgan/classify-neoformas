#!/usr/bin/env bash

# divide.sh

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
