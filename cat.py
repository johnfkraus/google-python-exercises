#!/usr/bin/python -tt
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

def Cat(filename):
  f = open(filename)
  text = f.read()
  print '---', filename
  print text
  return


# Define a main() function that prints a little greeting.
def main():
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: filename [filename ...]"
    sys.exit(1)

  for arg in args:
    Cat(arg)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

