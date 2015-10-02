#!/usr/bin/python
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# john kraus did this assignment

import sys
import re
import os
import shutil
import commands
import inspect
import time

# suggested functions
# get_special_paths(dir): returns a list of the absolute paths of the special files in the given directory
def get_special_paths(dir):
  abs_paths_list = []
  filenames = os.listdir(dir)
  for filename in filenames:
    if haz_special(filename):
      # print lineno(), 'haz_special(', filename, '):', haz_special(filename)
      path = os.path.join(dir, filename) # creates a valid path
      # print lineno(), 'path: ',path
      # print lineno(), 'os.path.abspath(path): ', os.path.abspath(path) 
      abs_paths_list.append(os.path.abspath(path))
  # print lineno(), '70 get_special_paths(', dir, ') returning abs_paths_list:', abs_paths_list
  return abs_paths_list


