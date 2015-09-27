#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""
'Copy Special' exercise
https://developers.google.com/edu/python/exercises/copy-special
The copyspecial.py program takes one or more directories as its arguments.
notes: zip -j


"""
# +++your code here+++
# Write functions and modify main() to call them

def List(dir):
  cmd = 'ls -l ' + dir
  print 'about to do this:', cmd
  # return
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    # print sys.stderr, 'there was an error:', output
    print sys.stderr.write('there was an error:' + output)
    sys.exit(1)
  print output

""" 
  filenames = os.listdir(dir)
  for filename in filenames:
    path = os.path.join(dir, filename) # creates a valid path
    print path
    print os.path.abspath(path)
"""
def get_input():
  var = raw_input("Enter to continue; n to quit: ").lower()
  print 'you entered something like [', var, ']'
  if var == '' or var == 'y' or var == 'Y': 
    return True
  else: 
    print 'you entered something like [', var, ']'
    return False


# suggested functions
def get_special_paths(dir):
  # returns a list of the absolute paths of the special files in the given directory
  cmd = 'ls -l ' + dir
  print 'about to do this:', cmd
  gi = get_input()
  print 'gi: ', gi
  if not gi: 
    return
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    # print sys.stderr, 'there was an error:', output
    print sys.stderr.write('there was an error:' + output)
    sys.exit(1)
  print output


  return

def copy_to(paths, dir):
  # given a list of paths, copies those files into the given directory
  return

def zip_to(paths, zippath): 
  # given a list of paths, zip those files up into the given zipfile
  return


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  print 'args: ', args
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for dir in args:
    get_special_paths(dir)

if __name__ == "__main__":
  main()





