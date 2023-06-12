#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    return None
    max_int = my_list[0]
    for i in my_list:
        if i > i % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
