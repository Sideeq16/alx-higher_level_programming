#!/usr/bin/python3
""" Module for inserts a line of text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)  # Reset the file pointer to the beginning
        
        for line in lines:
            file.write(line)  # Write the original line
            
            if search_string in line:
                file.write(new_string + '\n')  # Write the new line after the matched line
        
        file.truncate()  # Remove any remaining content after the last line
