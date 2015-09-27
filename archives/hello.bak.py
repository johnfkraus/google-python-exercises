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

def Hello(name):
  name = name + '!!!!!'
  print 'Hello', name


# Define a main() function that prints a little greeting.
def main():
	#   print sys.argv
  Hello(sys.argv[1])

  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
	  name = sys.argv[1]
  else:
	  name = 'World'
  print 'Howdy', name

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
