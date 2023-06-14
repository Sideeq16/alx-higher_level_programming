#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    nw_dictionary = {}
    for k, v in a_dictionary.items():
        nw_dictionary[k] = v * 2
    return nw_dictionary
