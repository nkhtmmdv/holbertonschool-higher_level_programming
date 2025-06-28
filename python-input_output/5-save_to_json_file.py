#!/usr/bin/python3
''' 5 '''

import json


def save_to_json_file(my_obj, filename):
    ''' 5 '''
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
