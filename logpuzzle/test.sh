#!/bin/bash

clear
# test with one param: logfile

./logpuzzle.py animal_developers.google.com

echo
echo

# test with --todir dir logfile

rm -rf /home/codio/workspace/logpuzzle/imgs
./logpuzzle.py --todir imgs animal_developers.google.com

tree imgs

