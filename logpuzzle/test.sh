#!/bin/bash

clear

# identify os platform
if [ "$(uname)" == "Darwin" ]; then
  echo Darwin Mac OSX platform-Good luck
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  echo Linux platform, this script should work
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  echo Windows NT platform MINGW32_NT- this script might not work!
fi

# test with a single param: logfile

./logpuzzle.py animal_developers.google.com

echo

# test with --todir dir logfile
# delete old results
# rm -rf /home/codio/workspace/logpuzzle/imgs
rm -rf imgs
./logpuzzle.py --todir imgs animal_developers.google.com

tree imgs

