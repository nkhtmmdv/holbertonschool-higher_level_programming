#!/usr/bin/python3
"""Send requests and handle exceptions"""
import sys
import requests

if __name__ == "__main__":
    """Ensure code is executed when directly run"""
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
