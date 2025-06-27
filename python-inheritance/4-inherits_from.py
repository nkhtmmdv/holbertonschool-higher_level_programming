#!/usr/bin/python3
''' 4 '''


def inherits_from(obj, a_class):
    ''' 4 '''
    obj_type = type(obj)
    if issubclass(obj_type, a_class) and obj_type is not a_class:
        return True
    return False
