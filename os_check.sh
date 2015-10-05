#!/bin/bash
# identify os platform
if [ "$(uname)" == "Darwin" ]; then
  echo Darwin Mac OSX platform
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  echo Linux platform
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
  echo Windows NT platform MINGW32_NT
fi

