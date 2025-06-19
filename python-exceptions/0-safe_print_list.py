#!/usr/bin/python3
def count_elements(my_list=[]):
    count1 = 0
    for _ in my_list:
        count1 += 1
    return count1

def safe_print_list(my_list=[], x=0):
    count = 0
    if x > count_elements(my_list):
        x = count_elements(my_list)  
    for i in range(x):
        try:
            print(my_list[i], end="")  
            count += 1
        except IndexError:
            break  
    print()  
    return count  
