#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urlparse

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your lame ass code here+++
  db = False # are we printing debugging messages?
  if db: print 'running read_urls(', filename, ')'
  # print filename
  hostname = filename.split('_')[1]

  # print 'hostname: ',  hostname
  name_list = []
  logfile = open(filename, 'rU')
  if db: print 'logfile:', logfile
  # logcontents = logfile.read()
  # print 'logcontents = ', logcontents
  url_list = []
  url_dict = {}
  # f = open('foo.txt', 'rU')
  
  for line in logfile: ## iterates over the lines of the file
    # print 'line: ', line, 
    ## trailing , so print does not add an end-of-line char
    ## since 'line' already includes the end-of line.
    match = re.search(r'(\S*jpg)', line)                                                               
    baseurl = hostname
    if match:                                                                                                                                                       
      # if db: print 'found match.group: ', match.group()                                                                                                             
      # if db: print 'found match.group(1): ', match.group(1)                                                                                                         
      url = match.group(1)                                                                                                         
      # print 'url: ', url
      # print 'baseurl:', baseurl 
      # not working: ????? fullurl = urlparse.urljoin(baseurl, url) 
      fullurl = 'http://' + baseurl + url
      # print 'fullurl: ', fullurl
      # -- given a url that may or may not be full, and the baseurl of the page it comes from, return a full url. Use geturl() above to provide the base url.
      url_list.append(fullurl) # match.group(1))                           
      url_dict[fullurl] = 1

  
  logfile.close()
  urls = sorted(url_dict.keys())
  # print 'urls ', urls
  for url in urls:
    print url
  return urls

  """
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
  """
  return name_list




def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++



def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()


