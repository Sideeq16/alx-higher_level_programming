#!/usr/bin/python3

def best_score(a_dictionary):
    maxi = 0
    store = "None"
    if a_dictionary:
        for k,v in a_dictionary.items():
            if a_dictionary[k] > maxi:
                maxi = a_dictionary[k]
                store = k
        return store
