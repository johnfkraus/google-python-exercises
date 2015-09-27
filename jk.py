#!/usr/bin/python -tt
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import commands
import sys
import os

def List(dir):
  filenames = os.listdir(dir)
  for filename in filenames:
    local_path = os.path.join(dir, filename)
    print 'filename = ', filename
    print 'local_path = ', local_path
    print 'os.path.abspath(local_path) = ', os.path.abspath(local_path)
    print
  return


"""
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
""" 
  filenames = os.listdir(dir)
  for filename in filenames:
    path = os.path.join(dir, filename) # creates a valid path
    print path
    print os.path.abspath(path)
"""
  
# Define a main() function that does something?
def main():
  List(sys.argv[1])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
