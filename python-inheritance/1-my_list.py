#!/usr/bin/python3
"""
This module defines MyList class.

Example:
>>> my_list = MyList()
>>> my_list.append(3)
>>> my_list.append(1)
>>> my_list.append(2)
>>> print(my_list)
[3, 1, 2]
>>> my_list.print_sorted()
[1, 2, 3]
>>> print(my_list)
[3, 1, 2]
"""

class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
