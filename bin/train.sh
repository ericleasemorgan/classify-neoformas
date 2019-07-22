#!/usr/bin/env bash

# train.sh - given a few configurations, create a model; a front-end to train.py

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# July 22, 2019 - first documentation


# configure
TRAIN='./bin/train.py'
MODEL='./etc/model.bin'
POSITIVE='./model/positive'
NEGATIVE='./model/negative'

# do the work and done
$TRAIN $MODEL $POSITIVE $NEGATIVE
exit
