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
def make_html(local_img_urls_list, todir):
  db = False
  if db: print lineno(), 'local_img_urls_list:', local_img_urls_list
  html = '<html><head><title>John\'s Google Python ' + puzzle_name + ' logpuzzle exercise solution</title></head><body>'
  for img_url in local_img_urls_list:
    html = html + '<img src=\"' + img_url + '\">'
  html = html + '</body></html>'
  # TODO: pretty print html file
  # root = html
  # root=lh.tostring(sliderRoot) #convert the generated HTML to a string
  # soup=bs(root)                #make BeautifulSoup
  # prettyHTML=soup.prettify()   #prettify the html
  # print 'html = ', html
  f = open(puzzle_name + '_image_view.html', 'w')
  f.write(html)
  f.close()
  return 

def make_place_html(sorted_orig_fname_paths, todir):
  db = True
  if db: print lineno(), 'sorted_orig_fname_paths:', sorted_orig_fname_paths[:800]
  html = '<html><head><title>John\'s Google Python ' + puzzle_name + ' logpuzzle exercise solution</title></head><body>'
  for img_url in sorted_orig_fname_paths:
    html = html + '<img src=\"' + img_url + '\">'
  html = html + '</body></html>'
  # TODO: pretty print html file
  # root = html
  # root=lh.tostring(sliderRoot) #convert the generated HTML to a string
  # soup=bs(root)                #make BeautifulSoup
  # prettyHTML=soup.prettify()   #prettify the html
  # print lineno(),  'html = ', html
  f = open(puzzle_name + '_image_view.html', 'w')
  f.write(html)
  f.close()
  print lineno(), 'html = ', html[:900]
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
  puzzle_name = filename.split('_')[0]
  hostname = filename.split('_')[1]
  logfile = open(filename, 'rU')
  if db: print 'logfile:', logfile
  orig_fname_list = []
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
      orig_fname_list.append(image_filename)
      # currently the images are found here:
      # https://developers.google.com/edu/python/images/puzzle/a-baab.jpg
      # regardless of the urls in the logs file we are supposed to parse
      fullurl = 'http://' + hostname + '/edu/python/images/puzzle/' + image_filename 
      if db: print 'fullurl: ', fullurl
      url_list.append(fullurl)
      url_dict[fullurl] = 1
  logfile.close()
  urls = sorted(url_dict.keys())
  # save results as list for debugging or tinkering
  f = open(puzzle_name + '_orig_fname_list.txt', 'w')
  print>>f, orig_fname_list
  f.close()
 
  f = open(puzzle_name + '_urls_list.txt', 'w')
  print>>f, urls
  f.close()
 
  f = open(puzzle_name + '_image_url_list.txt', 'w')
  print>>f, urls
  f.close()
 
  # save results as text for debugging or tinkering
  f = open(puzzle_name + '_image_url_text.txt', 'w')
  for url in urls:
    print>>f, url
  f.close()
  if db: print lineno(), 'urls = ', urls
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
  backup_abs_target_dir_exists = make_abs_target_basename_exists('images_orig_name')
  abs_dest_filename_list = []
  local_dest_filename_list = []
  backup_files_location_list = []
  orig_fname_dict = {}
  backup_dest_filename_list = []
  orig_fname_dest_dict = {}
  print 'Retrieving...'
  # i is index for image file numbering
  i = 0
  for url in img_urls:
    i+=1 
    if db: print lineno(), 'i = ', + i
    # if i> 3: db = False
    original_filename = url.split('/')[-1]
    if db: print lineno(), 'original_filename', original_filename,  'url: ', url
    # sys.exit(1)
    # format as string the integer for appending to 'img' filename; provide
    # leading zero for sorting
    string_num = str(i).zfill(3) 
    # default image filename extension is 'img' in case we don't find a jpg,
    # which is actually impossible in this program since our read_urls() method
    # searches for a jpg, but hey I'm thinking reuse here.
    img_file_extension = '.img'
    match = re.search(r'(\.jpg)\s*$', url)
    if match:
      img_file_extension = match.group(1)
     
    dest_filename = 'img' + string_num + img_file_extension
    # print as specified sort of 
    if puzzle_name == 'animal':
      if db: print lineno(), puzzle_name
      print dest_filename + ' (' + original_filename + ')',
      if i % 3 == 0: print
    else:
      if db: print lineno(), puzzle_name
      print i, original_filename,
      if i % 4 == 0: print
    abs_dest_filename = abs_target_dir_exists + '/' + dest_filename
    local_dest_filename = dest_dir + '/' + dest_filename
    backup_dest_filename = 'images_orig_name/' + original_filename
    abs_dest_filename_list.append(abs_dest_filename)
    local_dest_filename_list.append(local_dest_filename)
    # if db: print lineno(), 'abs_dest_filename_list = ', abs_dest_filename_list
    # if db: print lineno(), 'local_dest_filename_list = ', local_dest_filename_list
    # ufile is a file-like object
    ufile = urllib.urlopen(url)
    info = ufile.info() # -- the meta info for that request. info.gettype() is the
    file_type = info.gettype() # -- the meta info for that request. info.gettype() is the
    if file_type != 'image/jpeg': 
      backup_dest_filename = backup_dest_filename + '.txt'
      local_dest_filename = local_dest_filename + '.txt'
    else:
      backup_dest_filename_list.append(backup_dest_filename)

      # download the url data to the given file path
      val = urllib.urlretrieve(url, local_dest_filename) 
      val = urllib.urlretrieve(url, backup_dest_filename) 
      sort_key = (original_filename.split('.')[0]).split('-')[-1]
      orig_fname_dict[sort_key] = original_filename
      orig_fname_dest_dict[sort_key] = backup_dest_filename
      if db: print lineno(), 'orig_fname_dict[' + sort_key + '] = ' + orig_fname_dict[sort_key]
      if db: print lineno(), 'orig_fname_dest_dict[' + sort_key + '] = ' + orig_fname_dest_dict[sort_key]
  #  if i > 5: 
  #    break
 
  sorted_orig_fname_paths = []
  for key in sorted(orig_fname_dest_dict.keys()):
    sorted_orig_fname_paths.append(orig_fname_dest_dict[key])
  if db: print lineno(), 'sorted_orig_fname_paths', sorted_orig_fname_paths
  if db: print lineno(), 'puzzle_name = ', puzzle_name
  if puzzle_name == 'place':
    print lineno(), 'making html for place puzzle'
    make_place_html(sorted_orig_fname_paths, './')
  else:
    make_html(local_dest_filename_list, './' )
  # sys.exit(0)     

  # save results for debugging
  f = open('abs_dest_list.txt', 'w')
  print>>f, abs_dest_filename_list
  f.close()
  # print lineno(), 'puzzle_name:', puzzle_name
  orig_fname_dict_vals_list = []
  orig_fname_dict_keys_sorted = sorted(orig_fname_dict.keys())

  for key in orig_fname_dict_keys_sorted:
    fname_val = orig_fname_dict[key]
    orig_fname_dict_vals_list.append(fname_val)
  if db: print lineno(), 'orig_fname_dict_vals_list = ', orig_fname_dict_vals_list
     
  # if db: print 'local_dest_filename_list = ', local_dest_filename_list
  f = open('orig_fname_dict_keys_sorted.txt', 'w')
  print>>f, sorted(orig_fname_dict.keys())
  f.close()
  f=open('backup_dest_filename_list.txt', 'w')
  print>>f, backup_dest_filename_list
  f.close()

  # urls = sorted(url_dict.keys())
  
  f = open('local_dest_list.txt', 'w')
  print>>f, local_dest_filename_list
  f.close()
  return



def main():
  global db 
  global puzzle_name
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

  filename = args[0]
  puzzle_name = filename.split('_')[0]
  print lineno(), 'puzzle_name = ', puzzle_name
  img_urls = read_urls(args[0])
  if db: print lineno(), 'img_urls = ', img_urls

  if todir:
    if db: print lineno(), 'todir = ', todir
    download_images(img_urls, todir)
    if db: print lineno(), 'downloaded images!'
  else: # user entered only one param: logfile
    print
    print 'User entered only one param: logfile'
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()


