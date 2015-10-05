#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# images are found here: https://developers.google.com/edu/python/images/puzzle/a-baab.jpg
import os
import re
import sys
import urllib
import urlparse
import inspect

import shutil
import commands

# TODO: pretty print html file
# import BeautifulSoup as bs

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.
Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
db = False

"""
Create an html file that displays the retrieved images
"""
def make_html(local_img_urls_list):
  db = False
  if db: print lineno(), 'local_img_urls_list:', local_img_urls_list
  html = '<html><head><title>John\'s Google Pythone logpuzzle exercise solution</title></head><body>'
  for img_url in local_img_urls_list:
    html = html + '<img src=\"' + img_url + '\">'
  html = html + '</body></html>'
# TODO: pretty print html file
  # root = html
  # root=lh.tostring(sliderRoot) #convert the generated HTML to a string
  # soup=bs(root)                #make BeautifulSoup
  # prettyHTML=soup.prettify()   #prettify the html
  # print 'html = ', html
  f = open('image_view.html', 'w')
  f.write(html)
  f.close()
  return 


def lineno():
  """
  Returns the current line number in our program.
  lineno() is a function to make it easy to grab the line
  number that we're on. Danny Yoo (dyoo@hkn.eecs.berkeley.edu)
  """
  return inspect.currentframe().f_back.f_lineno

def make_abs_target_basename_exists(todir):
  db = False
  if db: print 'todir: ', todir
  abs_target_basename = os.path.abspath(todir)
  if db: print lineno(), 'abs_target_basename: ', abs_target_basename
  if db: print lineno(), 'abs_target_basename: ', abs_target_basename
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
  hostname = filename.split('_')[1]
  logfile = open(filename, 'rU')
  if db: print 'logfile:', logfile
  url_list = []
  url_dict = {}
  for line in logfile: ## iterates over the lines of the file
    # print 'line: ', line, 
    ## trailing , so print does not add an end-of-line char
    ## since 'line' already includes the end-of line.
    match = re.search(r'(\S*jpg)', line)
    baseurl = hostname
    if match:
      url = match.group(1)
      if db: print lineno(),  'found match.group(1): ', match.group(1), ' url = ', url
      url_pieces = url.split('/')
      if db: print 'url_pieces = ', url_pieces
      image_filename = url_pieces[-1]
      # currently the images are found here:
      # https://developers.google.com/edu/python/images/puzzle/a-baab.jpg
      # regardless of the urls in the logs file we are supposed to parse
      fullurl = 'http://' + hostname + '/edu/python/images/puzzle/' + image_filename 
      if db: print 'fullurl: ', fullurl
      url_list.append(fullurl)
      url_dict[fullurl] = 1
  logfile.close()
  urls = sorted(url_dict.keys())
  # save results for debugging or tinkering
  f = open('image_url_list.txt', 'w')
  for url in urls:
    print>>f, url
  f.close()
  return urls

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Prints 'Retreiving...' and prints local filenames as retrieved.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  db = False
  # +++your skanky code here+++
  if db: print lineno(), 'dest_dir:', dest_dir
  abs_target_dir_exists = make_abs_target_basename_exists(dest_dir)
  abs_dest_filename_list = []
  local_dest_filename_list = []
  print 'Retrieving...'
  # i is index for image file numbering
  i = 0
  for url in img_urls:
    i+=1 
    if i> 3: db = False
    if db: print lineno(), 'url: ', url
    # format as string the integer for appending to 'img' filename; provide
    # leading zero for sorting
    string_num = str(i).zfill(2) 
    # default image filename extension is 'img' in case we don't find a jpg,
    # which is actually impossible in this program since our read_urls() method
    # searches for a jpg, but hey I'm thinking reuse here.
    img_file_extension = '.img'
    match = re.search(r'(\.jpg)\s*$', url)
    if match:
      img_file_extension = match.group(1)
    dest_filename = 'img' + string_num + img_file_extension
    print dest_filename
    abs_dest_filename = abs_target_dir_exists + '/' + dest_filename
    local_dest_filename = dest_dir + '/' + dest_filename
    abs_dest_filename_list.append(abs_dest_filename)
    local_dest_filename_list.append(local_dest_filename)
    if db: print lineno(), 'abs_dest_filename_list = ', abs_dest_filename_list
    if db: print lineno(), 'local_dest_filename_list = ', local_dest_filename_list
    # ufile is a file-like object
    ufile = urllib.urlopen(url)
    info = ufile.info() # -- the meta info for that request. info.gettype() is the
    file_type = info.gettype() # -- the meta info for that request. info.gettype() is the
    if db: print lineno(), 'file_type = ', file_type
    if db: print lineno(),  'file_type: ', file_type
    # download the url data to the given file path
    val = urllib.urlretrieve(url, local_dest_filename) 
  # save results for debugging
  f = open('abs_dest_list.txt', 'w')
  print>>f, abs_dest_filename_list
  f.close()
  if db: print 'local_dest_filename_list = ', local_dest_filename_list
  make_html(local_dest_filename_list)
  f = open('local_dest_list.txt', 'w')
  print>>f, local_dest_filename_list
  f.close()
  return


def main():
  db = False
  args = sys.argv[1:]
  # print 'args = ', args
  if not args:
    print 'usage: [--todir dir] logfile'
    sys.exit(1)
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    # print 'todir = ', todir
    # print 'os.path.dirname(todir):', os.path.dirname(todir)
    del args[0:2]
    if db: print lineno(), 'args = ', args 

  img_urls = read_urls(args[0])
  if db: print lineno(), 'img_urls = ', img_urls

  if todir:
    if db: print lineno(), 'todir = ', todir
    download_images(img_urls, todir)
    if db: print lineno(), 'downloaded images!'
    # make_html(img_urls, todir) 
  else: # user entered only one param: logfile
    print
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()


