#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and displays the response body."""

import urllib.request

def fetch_status():
    """Fetch and display status content from a given URL."""
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    with urllib.request.urlopen(req) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))

if __name__ == "__main__":
    fetch_status()
