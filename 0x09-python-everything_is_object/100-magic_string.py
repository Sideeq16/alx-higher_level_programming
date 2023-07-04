#!/usr/bin/python3
def magic_string():
    counter = [0]
    return lambda: (counter.append(counter.pop() + 1), "BestSchool" * counter[0])[1]
