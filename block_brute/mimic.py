#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

def print_dict(dict):
  for k, v in dict.items(): 
    print k, '>', v

def print_dict_count(dict):
  for k, v in dict.items(): 
    print k, '>', v, '; len(v) = ', len(v)

def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  db = False # debugging messages on?
  dict = {}
  file = open(filename, 'rU')
  contents = file.read()
  contents_list = contents.split()
  # print 'len = ', len(contents_list)
  dict[''] = [contents_list[0]]
  i = 0
  mylen = (len(contents_list)-1)
  # print 'len contents list ', mylen
  next_to_last = range(mylen)[-1] 
  for i in range(mylen):
    # while i < len(contents_list)-1:
    if db: print 'line 59', print_dict(dict)
    word1 = contents_list[i] 
    word2 = contents_list[i+1]
    if db:
      if i  == next_to_last: # range(mylen)[-1]:
        print 'next to last word: ', word1, 'last word: ',word2 
    if db: print 'line 60; i = ', i, '/', len(contents_list),'; ', word1,'->', word2
    if word1 in dict:
      if db: print 'line 62; i = ', i, '/', len(contents_list),'; ', word1,'->', word2, '; dict[', word1, '] = ', dict[word1]
      value_list = dict[word1]
      if db: print 'line 64; i = ', i, '/', len(contents_list),';', word1,'->', word2, '; value_list = ', value_list
      if db: print 'type(value_list) = ', type(value_list)
      # duplicates are not added to the values list, although this was not an
      # explicit direction; duplicates might appropriately reflect word use
      # probability; but watch out for repeating words in output!
      if word2 not in value_list: 
        value_list.append(word2)
        dict[word1] = value_list
    else:
      # word1 is not already in dict; add it
      dict[word1] = [word2]
      if db: print 'line 73; i = ', i, '/', len(contents_list),'; ', word1,'->', word2, '; dict[', word1, '] = ', dict[word1], 'type(dict[word1]) = ', type(dict[word1])
    # i+=1
  if db: print dict
  if db: print 'len(dict) = ', len(dict)
  if db: print_dict(dict)
  if db: print_dict_count(dict)
  if db: print 'dict = ', dict
  return dict

def pick_random_from_list(list):
  # print '95 list = ', list
  if len(list) > 1:
    # print random.randrange(0, len(list)-1)
    return list[random.randrange(0, len(list)-1)]
  else:
  # return list(random.randrange(0, len(list)-1))
    return list[0]
  return

def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  # +++your code here+++
  # print word
  # list = mimic_dict[word]
  # print mimic_dict[word] # returns list
  i = 0
  string = ''
  for i in range(200):
  # while i < 200:
    list = mimic_dict[word]
    word = pick_random_from_list(list)
    # print word
    string = string + ' ' +  word
    # i+=1
  print string
  return


# Provided main(), calls mimic_dict() and mimic()
def main():
  if len(sys.argv) != 2:
    print 'usage: ./mimic.py file-to-read'
    sys.exit(1)
  dict = mimic_dict(sys.argv[1])
  print_mimic(dict, '')


if __name__ == '__main__':
  main()
