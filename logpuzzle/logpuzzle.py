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
import inspect

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

def lineno():
  """
  Returns the current line number in our program.
  lineno() is a function to make it easy to grab the line
  number that we're on. Danny Yoo (dyoo@hkn.eecs.berkeley.edu)
  """
  return inspect.currentframe().f_back.f_lineno


def make_abs_target_basename_exists(todir):
  db = True
  print 'todir: ', todir
  abs_target_basename = os.path.abspath(todir)
  print lineno(), 'abs_target_basename: ', abs_target_basename
  # basename = os.path.basename(abs_target_path)
  print lineno(), 'abs_target_basename: ', abs_target_basename
  
  # target_dirname = os.path.dirname(abs_target_basename) 
  # print 'target_dirname = ', target_dirname
  if not os.path.exists(abs_target_basename):
    if db: print lineno(), 'target path did not exist, creating: ', abs_target_basename
    os.makedirs(abs_target_basename)
  else: 
    if db: 
      print lineno(), 'target path exists:', abs_target_basename
  # abs_target_basename_exists = abs_target_basename
  return abs_target_basename

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
  # name_list = []
  logfile = open(filename, 'rU')
  if db: print 'logfile:', logfile
  # logcontents = logfile.read()
  # print 'logcontents = ', logcontents
  url_list = []
  url_dict = {}
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



def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  print 'dest_dir:', dest_dir
  abs_target_dir_exists = make_abs_target_basename_exists(dest_dir)
  print 'abs_target_dir_exists:  ', abs_target_dir_exists
  for url in img_urls:
    print 'url:', url
  # need to make a path out of dest_dir!
  return



def main():
  args = sys.argv[1:]
  print 'args = ', args
  if not args:
    print 'usage: [--todir dir] logfile'
    sys.exit(1)
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    print 'todir = ', todir
    print 'os.path.dirname(todir):', os.path.dirname(todir)
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()








