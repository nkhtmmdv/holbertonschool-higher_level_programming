#!/usr/bin/python3
''' 6 '''

import json


def load_from_json_file(filename):
    ''' 6 '''
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
