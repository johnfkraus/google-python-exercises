#!/usr/bin/python
# john kraus did this

import sys
import re
import os
import shutil
import commands
import inspect
import time

import csv
import json

"""lineno() is a function to make it easy to grab the line
number that we're on. Danny Yoo (dyoo@hkn.eecs.berkeley.edu)
"""
def lineno():
  # Returns the current line number in our program.
  return inspect.currentframe().f_back.f_lineno
