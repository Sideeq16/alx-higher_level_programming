#!/usr/bin/python3

def no_c(my_string):
    nw_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            nw_string += char
    return nw_string
