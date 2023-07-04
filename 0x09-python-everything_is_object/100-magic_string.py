#!/usr/bin/python3
"""Documentation for magic_string function"""


def magic_string():
    def helper(counter=[0]):
        counter[0] += 1
        return "BestSchool" * counter[0]
    return helper
