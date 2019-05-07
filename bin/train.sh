#!/usr/bin/env bash

# train.sh

TRAIN='./bin/train.py'
MODEL='./etc/model.bin'
POSITIVE='./model/positive'
NEGATIVE='./model/negative'

# do the work and done
$TRAIN $MODEL $POSITIVE $NEGATIVE
exit
