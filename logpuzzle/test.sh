#!/bin/bash

clear

# identify os platform
if [ "$(uname)" == "Darwin" ]; then
  echo Darwin Mac OSX platform
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  echo Linux platform
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  echo Windows NT platform MINGW32_NT
fi


# test with one param: logfile

./logpuzzle.py animal_developers.google.com

echo
echo

# test with --todir dir logfile

rm -rf /home/codio/workspace/logpuzzle/imgs
./logpuzzle.py --todir imgs animal_developers.google.com

tree imgs

