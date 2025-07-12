#!/usr/bin/python3
"""1"""


import urllib.request
import sys

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    """1"""
    print(response.getheader('X-Request-Id'))
