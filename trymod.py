#!/usr/bin/python -tt
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import commands
import sys
import os

def readfile(filename):
  try:
  ## Either of these two lines could throw an IOError, say
  ## if the file does not exist or the read() encounters a low level error.
    f = open(filename, 'rU')
    text = f.read()
    print 'text:', text[:500]
    f.close()
  except IOError:
    ## Control jumps directly to here if any of the above lines throws IOError.
    sys.stderr.write('problem reading: ' + filename + '\n')

  ## In any case, the code then continues with the line after the try/except
  return

