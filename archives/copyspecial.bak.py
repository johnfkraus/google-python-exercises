#!/usr/bin/python
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
note: zip -j
"""
# +++your code here+++
# Write functions and modify main() to call them

def List(dir):
  cmd = 'ls -l ' + dir
  print '28 about to do this:', cmd
  # return
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    # print sys.stderr, 'there was an error:', output
    print sys.stderr.write('there was an error:' + output)
    sys.exit(1)
  print output
  return

# pause for confirmation; for debugging
def get_input():
  var = raw_input("39 Enter to continue; n to quit: ").lower()
  print '40 you entered something like [', var, ']'
  if var == '' or var == 'y' or var == 'Y': 
    return True
  else: 
    print '44 you entered something like [', var, ']'
    return False

# pause for confirmation; for debugging
def pause_for_confirmation():
  var = raw_input("44 Enter to continue; n to quit: ").lower()
  print '45 you entered something like [', var, ']'
  if var == '' or var == 'y':
    return True
  else: 
    return False

def haz_special(filename):
  db = True
  match = re.search(r'__.*__', filename)
  if match:                      
    # if db: print 'found match.group: ', match.group() 
    # if db: print 'found match.group(1): ', match.group(1) 
    return True
  else: 
    return False
  return

# suggested functions
# get_special_paths(dir): returns a list of the absolute paths of the special files in the given directory
def get_special_paths(dir):
  abs_paths_list = []
  filenames = os.listdir(dir)
  for filename in filenames:
    if haz_special(filename):
      # print 'haz_special(', filename, '):', haz_special(filename)
      path = os.path.join(dir, filename) # creates a valid path
      # print 'path: ',path
      # print 'os.path.abspath(path): ', os.path.abspath(path) 
      abs_paths_list.append(os.path.abspath(path))
  # print '70 get_special_paths(', dir, ') returning abs_paths_list:', abs_paths_list
  return abs_paths_list

"""
def commands_copy_to(paths, dir):
  # given a list of (absolute) paths, copies those files into the given directory
  print '75 paths: ', paths, '; dir: ', dir

  for path in paths:
    cmd = 'cp ' + path + " " + dir
    # print 'about to do this:', cmd
    # if not get_input(): return
    (status, output) = commands.getstatusoutput(cmd)
    if status:
      print sys.stderr.write('83 there was an error:' + output)
      sys.exit(1)
    # print '85 output: ', output
  return
"""
def copy_to(paths, target_dir):
  # given a list of paths, copies those files into the given directory
  print '85 paths: ', paths, '; target_dir: ', target_dir
  abs_target_dir = os.path.abspath(target_dir)
  print 'abs_target_dir:', abs_target_dir
  for path in paths:
    basename = os.path.basename(path)
    print 'basename:', basename
    target_path = os.path.join(target_dir, basename)
    abs_target_path = os.path.abspath(target_path)
    target_dirname = os.path.dirname(abs_target_path) 
    print 'target_dirname:', target_dirname
    print 'target_path:', target_path
    print 'abs_target_path:', abs_target_path
    if not os.path.exists(target_dirname):
      print 'target path doex not exist: ', target_dirname
      os.makedirs(target_dirname)
    shutil.copy(path, target_path)
    # cmd = 'cp ' + path + " " + dir

    # print 'about to do this:', cmd
    # if not get_input(): return
    # (status, output) = commands.getstatusoutput(cmd)

    # if status:
      # print sys.stderr.write('83 there was an error:' + output)
      # sys.exit(1)
    # print '85 output: ', output
  return

def make_abs_target_path_exists(zippath):
  print '123 zippath: ', zippath 
  abs_target_path = os.path.abspath(zippath)

  return abs_target_path_exists

def zip_to(paths, zippath): 
  # given a list of paths, zip those files up into the given zipfile
  # print 'need to implement zip_to method'
  print '131 paths: ', paths, '; zippath: ', zippath 
  # target_path = os.path.join(dir, basename)
  abs_target_path = os.path.abspath(zippath)
  print 'abs_target_path:', abs_target_path

  sys.exit(0)
  basename = os.path.basename(path)
  print 'basename:', basename
  target_path = os.path.join(dir, basename)
  abs_target_path = os.path.abspath(target_path)
  target_dirname = os.path.dirname(abs_target_path) 
  print 'target_dirname:', target_dirname
  print 'target_path:', target_path
  if not os.path.exists(target_dirname):
    print 'target path doex not exist: ', target_dirname
    os.makedirs(target_dirname)
  paths = []
  for path in paths:
    cmd = 'cp ' + path + " " + dir
    # print 'about to do this:', cmd
    # if not get_input(): return
    (status, output) = commands.getstatusoutput(cmd)
    if status:
      print sys.stderr.write('83 there was an error:' + output)
      sys.exit(1)
    # print '85 output: ', output
  abs_target_dir = os.path.abspath(dir)
  print 'abs_target_dir:', abs_target_dir
  for path in paths:
    basename = os.path.basename(path)
    print 'basename:', basename
    target_path = os.path.join(dir, basename)
    abs_target_path = os.path.abspath(target_path)
    target_dirname = os.path.dirname(abs_target_path) 
    print 'target_dirname:', target_dirname
    print 'target_path:', target_path
    print 'abs_target_path:', abs_target_path
    if not os.path.exists(target_dirname):
      print 'target path doex not exist: ', target_dirname
      os.makedirs(target_dirname)
    shutil.copy(path, target_path)
    # cmd = 'cp ' + path + " " + dir

    # print 'about to do this:', cmd
    # if not get_input(): return
    # (status, output) = commands.getstatusoutput(cmd)


  return


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  # print 'args: ', args
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
    sys.exit(1)

# If the '--todir dir' option is present at the start of the 
# command line, do not
# print anything and instead copy the files to the given directory, creating it if necessary. Use the python module 'shutil' for file copying.

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1] 
    # todir now contains the target directory
    del args[0:2]
    # args[:] now contains only the source directories 


  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1] # the zip target
    # tozip now contains the target directory
    del args[0:2]
    # args[:] now contains only the source directories 

  if len(args) == 0:
    print "error: must specify one or more source dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  spec_paths_list = [] # list of abs paths to all special files 

  for source_dir in args:
    # args[:] is a list of the source directories 
    spec_paths_list.extend(get_special_paths(source_dir))

  if todir:
    copy_to(spec_paths_list, todir)
    # If the "--todir dir" option is present at the start of the 
    # command line, do not print anything and instead ... 
  else:
    for path in spec_paths_list:
      print path



  if tozip:
    zip_to(spec_paths_list, tozip)

if __name__ == "__main__":
  main()

