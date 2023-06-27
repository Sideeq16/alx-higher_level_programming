#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as e:
        result = None
        print("Exception:", e, file=sys.stderr)
    return result
