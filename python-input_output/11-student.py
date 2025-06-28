#!/usr/bin/python3
''' 11 '''


class Student:
    ''' 11 '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            filtered = {}
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    filtered[attr] = getattr(self, attr)
            return filtered
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
