#!/usr/bin/python3
"""1"""
import urllib.request
import sys

if __name__ == "__main__":
    """1"""
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        """1"""
        print(response.getheader('X-Request-Id'))
