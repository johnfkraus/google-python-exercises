#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  name_list = []
  """
  Apparently the baby name dict is envisioned, for simplicity, 
  as gender-agnostic.  From the video on YouTube: if a name is both 
  male and female, it goes in the dictionary once with the popularity 
  rank integer representing the greatest popularity (i.e., use the 
  lowest integer). 
  """
  db = False # are we printing debugging messages?
  if db: print 'running extract_names'
  year = ''
  simple_babyname_dict = {}
  # complete_babyname_dict = {}
  file = open(filename, 'rU')
  if db: print 'file:', file
  contents = file.read()
  # print 'contents = ', contents

  # find the year
  # match = re.search(r'<h3 align="center">Popularity in (\d{4})<\/h3>', contents)
  match = re.search(r'<h\d.*>Popularity in (\d{4})<\/h\d>|<b>Popularity in (\d{4})<\/b>', contents)
  if match:                      
    if db: print 'found match.group: ', match.group() 
    if db: print 'found match.group(1): ', match.group(1) 
    name_list.append(match.group(1))
    if db: print 'name_list: ', name_list
  else:
    print 'did not find year for filename: ', filename

  # find names and ranks in html table
  match_list_tuples = re.findall(r'<tr align="right"><td>(\d+)<\/td><td>(\w+)<\/td><td>(\w+)<\/td>' , contents)
  if match_list_tuples:
    # print 'found', match.group() 
    # print 'found', match_list
    if db: print 'len(match_list_tuples):', len(match_list_tuples)
    if db: print 'found', match_list_tuples
    for tuple in match_list_tuples:
      if db: print tuple[0], tuple[1], tuple[2]
      # insert the list of male names into the dict
      simple_babyname_dict[tuple[1]] = tuple[0]
      if db: print tuple[1], tuple[0], tuple[2]
      if db: print 'tuple: ', tuple
      # insert the list of female names into the dict
      if tuple[2] not in simple_babyname_dict:
        simple_babyname_dict[tuple[2]] = tuple[0]
        if db: print tuple[2], tuple[0]
      else:
        if db: print tuple[2], 'ranks', tuple[0], 'as girl name,', simple_babyname_dict[tuple[2]], 'as boy name'
        # dict_rank = simple_babyname_dict[tuple[2]]
        best_rank = min( simple_babyname_dict[tuple[2]], tuple[0])
        simple_babyname_dict[tuple[2]] = best_rank
        if db: print tuple[2], simple_babyname_dict[tuple[2]] 
    # name_list.append(match.group(1))
  else:
    print 'did not find names and ranks in html table for filename:', filename

  if db: print len(simple_babyname_dict)
  for k, v in simple_babyname_dict.items(): 
    if db: print k, '>', v
    string = '%s %s' % (k, v)
    if db: print string 
    name_list.append(string)    
    
  if db: print 'name_list:', name_list, 'len:', len(name_list)
  return name_list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  # print 'running main'
  
  args = sys.argv[1:]
  # print args
  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  # jk sez: 'text output' is ambiguous; have to go back to the YouTube video to
  # see what they want for 'text output'; 
  
  for filename in args:
    name_list = extract_names(filename)
    if summary:
      out_filename = filename + '.summary'
      file = open(out_filename, 'w')
      for item in sorted(name_list):
        file.write(item + '\n')
      file.close()
    else: 
      # print '142 name_list:', name_list   
      for item in sorted(name_list):
        print item

if __name__ == '__main__':
  main()
