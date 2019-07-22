#!/usr/bin/env bash

# build.sh - one script to rule them all

# Eric Lease Morgan <emorgan@nd.edu>
# (c) University of Notre Dame; distributed under a GNU Public License

# July 23, 2019 - first documentation; assumes train.py has been configured "correctly"


# do the work and done
./bin/pdf2txt.sh
./bin/divide.sh
./bin/clean.sh
./bin/train.sh
exit
