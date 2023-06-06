#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    last_digit_char = str(last_digit)
    print("{:s}".format(last_digit_char), end="")
    return last_digit
