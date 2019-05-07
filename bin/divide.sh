#!/usr/bin/env bash

# divide.sh

# configure
POSITIVE='./model/positive'
NEGATIVE='./model/negative'
PDF='./pdf'

# make file system
mkdir -p $POSITIVE
mkdir -p $NEGATIVE

# do the work and done
mv $PDF/*_neg_*.txt $NEGATIVE
mv $PDF/*_pos_*.txt $POSITIVE
exit
