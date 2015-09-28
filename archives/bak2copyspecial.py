#!/usr/bin/python
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import inspect

"""This provides a lineno() function to make it easy to grab the line
number that we're on.
Danny Yoo (dyoo@hkn.eecs.berkeley.edu)
"""

def lineno():
  # Returns the current line number in our program.
  return inspect.currentframe().f_back.f_lineno

"""
if __name__ == '__main__':
  print "hello, this is line number", lineno()
  print 
  print 
  print "and this is line", lineno()
"""

# import currentframe, getframeinfo
# from inspect import currentframe, getframeinfo

# alias for lnum(inspect.currentframe()); global var!!
# icf = inspect.currentframe()
"""
def lnum(currentframe):
  frameinfo = inspect.getframeinfo(currentframe)
  print 'frameinfo = ', frameinfo
  print 'inspect.stack() = ', inspect.stack()
  current_line_no = inspect.stack()[0][2]
  print 'inspect.stack()[0][2]) = ', inspect.stack()[0][2]
"""
  # current_function_name = inspect.stack()[0][3]
  # print lineno(), frameinfo.filename, frameinfo.lineno
  # return frameinfo.lineno


# print lineno()

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
  print lineno(), '28 about to do this:', cmd
  # return
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    # print lineno(), sys.stderr, 'there was an error:', output
    print lineno(), sys.stderr.write('there was an error:' + output)
    sys.exit(1)
  print lineno(), output
  return

# pause for confirmation; for debugging
def get_input():
  var = raw_input("39 Enter to continue; n to quit: ").lower()
  print lineno(), '40 you entered something like [', var, ']'
  if var == '' or var == 'y' or var == 'Y': 
    return True
  else: 
    print lineno(), '44 you entered something like [', var, ']'
    return False

# pause for confirmation; for debugging
def pause_for_confirmation():
  var = raw_input("44 Enter to continue; n to quit: ").lower()
  print lineno(), '45 you entered something like [', var, ']'
  if var == '' or var == 'y':
    return True
  else: 
    return False

def haz_special(filename):
  db = True
  match = re.search(r'__.*__', filename)
  if match:                      
    # if db: print lineno(), 'found match.group: ', match.group() 
    # if db: print lineno(), 'found match.group(1): ', match.group(1) 
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
      # print lineno(), 'haz_special(', filename, '):', haz_special(filename)
      path = os.path.join(dir, filename) # creates a valid path
      # print lineno(), 'path: ',path
      # print lineno(), 'os.path.abspath(path): ', os.path.abspath(path) 
      abs_paths_list.append(os.path.abspath(path))
  # print lineno(), '70 get_special_paths(', dir, ') returning abs_paths_list:', abs_paths_list
  return abs_paths_list

def copy_to(paths, target_dir):
  # given a list of paths, copies those files into the given directory
  print lineno(), 'paths: ', paths, '; target_dir: ', target_dir
  abs_target_dir = os.path.abspath(target_dir)
  print lineno(), 'abs_target_dir:', abs_target_dir
  for path in paths:
    basename = os.path.basename(path)
    print lineno(), 'basename:', basename
    target_path = os.path.join(target_dir, basename)
    abs_target_path = os.path.abspath(target_path)
    target_dirname = os.path.dirname(abs_target_path) 
    print lineno(), 'target_dirname:', target_dirname
    print lineno(), 'target_path:', target_path
    print lineno(), 'abs_target_path:', abs_target_path
    if not os.path.exists(target_dirname):
      print lineno(), 'target path doex not exist: ', target_dirname
      os.makedirs(target_dirname)
    shutil.copy(path, target_path)
    # cmd = 'cp ' + path + " " + dir

    # print lineno(), 'about to do this:', cmd
    # if not get_input(): return
    # (status, output) = commands.getstatusoutput(cmd)

    # if status:
      # print lineno(), sys.stderr.write('83 there was an error:' + output)
      # sys.exit(1)
    # print lineno(), '85 output: ', output
  return

def make_abs_target_path_exists(zippath):
  # print lineno(), '107 zippath: ', zippath 
  abs_target_path = os.path.abspath(zippath)
  # print lineno(), '109 abs_target_path: ', abs_target_path
  basename = os.path.basename(abs_target_path)
  print lineno(), 'basename:', basename
  target_dirname = os.path.dirname(abs_target_path) 
  print lineno(), 'target_dirname:', target_dirname
  if not os.path.exists(target_dirname):
    print lineno(), 'target path did not exist, creating: ', target_dirname
    os.makedirs(target_dirname)
  else: print lineno(), 'target path exists'
  abs_target_path_exists = abs_target_path
  # sys.exit(1)
  return abs_target_path_exists

#   target_path = os.path.join(dir, basename)
#   abs_target_path = os.path.abspath(target_path)
#   print lineno(), 'target_path:', target_path
#   if not os.path.exists(target_dirname):
#     print lineno(), 'target path doex not exist: ', target_dirname
#     os.makedirs(target_dirname)
#   paths = []
#   for path in paths:
#     cmd = 'cp ' + path + " " + dir
#     # print lineno(), 'about to do this:', cmd
#     # if not get_input(): return
#     (status, output) = commands.getstatusoutput(cmd)
#     if status:
#       print lineno(), sys.stderr.write('83 there was an error:' + output)
#       sys.exit(1)
#     # print lineno(), '85 output: ', output
#   abs_target_dir = os.path.abspath(dir)
#   print lineno(), 'abs_target_dir:', abs_target_dir
#   for path in paths:
#     basename = os.path.basename(path)
#     print lineno(), 'basename:', basename
#     target_path = os.path.join(dir, basename)
#     abs_target_path = os.path.abspath(target_path)
#     target_dirname = os.path.dirname(abs_target_path) 
#     print lineno(), 'target_dirname:', target_dirname
#     print lineno(), 'target_path:', target_path
#     print lineno(), 'abs_target_path:', abs_target_path
#     if not os.path.exists(target_dirname):
#       print lineno(), 'target path doex not exist: ', target_dirname
#       os.makedirs(target_dirname)
#     shutil.copy(path, target_path)
#     # cmd = 'cp ' + path + " " + dir
# 
#     # print lineno(), 'about to do this:', cmd
#     # if not get_input(): return
#     # (status, output) = commands.getstatusoutput(cmd)
# 
#   return





def zip_to(spec_paths_list, zippath): 
  # given a list of paths, zip those files up into the given zipfile
  # print lineno(), 'need to implement zip_to method'
  print lineno(),  'spec_paths_list: ', spec_paths_list, '; zippath: ', zippath 
  delim = ' '
  spec_paths_list_joined = delim.join(spec_paths_list)
  print lineno(),  'spec_paths_list_joined: ', spec_paths_list_joined
  # target_path = os.path.join(dir, basename)
  abs_target_path = os.path.abspath(zippath)
  print lineno(),  'abs_target_path:', abs_target_path
  abs_target_path_exists =  make_abs_target_path_exists(abs_target_path)
  print lineno(),  'abs_target_path_exists =', abs_target_path_exists
  # sys.exit(0)
  basename = os.path.basename(abs_target_path_exists)
  print lineno(), 'basename:', basename
  target_dirname = os.path.dirname(abs_target_path_exists) 
  print lineno(), 'target_dirname:', target_dirname
  paths = []
  # sys.exit(0)
  # for path in spec_paths_list:
  # spec_paths_list_joined = ''
  # spec_paths_list_joined.join(spec_paths_list)
  cmd = 'zip -j ' + abs_target_path_exists + " " + spec_paths_list_joined
  print lineno(), 'about to do this:', cmd
  if not get_input(): return
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    print lineno(), sys.stderr.write('on line ' +lineno() +'there was an error:' + output)
    sys.exit(1)
    # shutil.copy(path, target_path)
    # cmd = 'cp ' + path + " " + dir

    # print lineno(), 'about to do this:', cmd
    # if not get_input(): return
    # (status, output) = commands.getstatusoutput(cmd)
  return



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  # print lineno(), 'args: ', args
  if not args:
    print lineno(), "usage: [--todir dir][--tozip zipfile] dir [dir ...]"
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
    print lineno(), "error: must specify one or more source dirs"
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
      print lineno(), path



  if tozip:
    zip_to(spec_paths_list, tozip)

if __name__ == "__main__":
  main()

