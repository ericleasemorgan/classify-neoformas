#!/usr/bin/env bash

# build.sh - one script to rule them all


find ThirdSet -name '*.pdf' -exec cp {} ./pdf \;
./bin/pdf2txt.sh
./bin/divide.sh
./bin/clean.sh
./bin/train.sh
