#!/usr/bin/python
# john kraus did this; kjcparser.py

import sys
import os
import inspect
import csv
import json

"""lineno() is a function to make it easy to grab the line
number that we're on. Danny Yoo (dyoo@hkn.eecs.berkeley.edu)
"""
def lineno():
  # Returns the current line number in our program.
  return inspect.currentframe().f_back.f_lineno

def getFilenameWithoutExtension(csv_filename):
  filename, file_extension = os.path.splitext(csv_filename)
  print lineno(),  "filename =", filename
  return filename

def getHeadersAsTuple(csv_filename):
  with open(csv_filename, 'rb') as f:
    reader = csv.reader(f)
    your_list = map(tuple, reader)
    return your_list[0]

def csv2json(csv_filename, json_filename):
  # Open the CSV
  f = open(csv_filename, 'rb')
  has_header = csv.Sniffer().has_header(f.readline())
  print lineno(), "has_header =", has_header
  fieldnames = getHeadersAsTuple(csv_filename)
  print lineno(), "fieldnames =", fieldnames
  csvreader = csv.DictReader(f, fieldnames)
  # print "54 len(list(csvreader)) =", len(list(csvreader))

  if (has_header):
    print "has header =  true"
    # This skips the first row of the CSV file.
    # csvreader.next()
    # next(reader)
  # Parse the CSV into JSON; add 'indent=2' for pretty printing
  out = json.dumps([ row for row in csvreader ], indent=2)

  print "JSON parsed!"
  # Save the JSON
  f = open(json_filename, 'w')
  f.write(out)
  print "JSON saved!"
  print out
  print lineno(), "type(out) =", type(out)

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  # print lineno(), 'args: ', args
  if not args:
    print "usage: filename.csv filename.json"
    sys.exit(1)

  csv_filename = args[0]
  print "75 csv_filename =", csv_filename
  print "76 len(args) = ", len(args)
  if (len(args) < 2):
    json_filename = getFilenameWithoutExtension(csv_filename) + ".json"
    print "json_filename =", json_filename

  # +++your code here+++
  # Call your functions
  # csv2dict(args[0])

  csv2json(args[0], json_filename)

if __name__ == "__main__":
  main()
