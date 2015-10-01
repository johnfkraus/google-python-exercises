#!/usr/bin/python -tt
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
"""
Cat() function with try / except
from day 2 part 3 lecture of Google's Python Class
"""

import sys

def Cat(filename):
  """
  Print a text file to standard output.
  """
  try:
    f = open(filename)
    text = f.read()
    print '---', filename
    print text
  except IOError:
    HandleError()
    print 'IO Error', filename
  return

# Define a main() function that prints a little greeting.
def main():
  """
  Define a main() function that runs the Cat function.
  """
  # Make a list of command line arguments, omitting the [0] element.
  # The omitted sys.argv[0] element is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: filename [filename ...]"
    sys.exit(1)

  for arg in args:
    Cat(arg)

# The following two lines are the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

