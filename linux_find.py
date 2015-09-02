#!/usr/bin/env python
import sys
import os

def find_files():
    """
    Linux Find in Python
    find_files.py path_to_start_search filename_to_search_for
    """
    arguments = sys.argv
    path = arguments[1]
    pattern = arguments[2]

    files = walk_dirs(path)[0]
    dirs = walk_dirs(path)[1]

    for file in files:
        if pattern in file:
            print file

def walk_dirs(dir_name):
    """ Walk all dirs recursively and return all files, dirs with their full path """
    file_list = []
    dir_list = []

    for root, dirs, files in os.walk(dir_name):
        for item in files:
            file_list.append(os.path.join(root, item))
        for item in dirs:
            dir_list.append(os.path.join(root, item))

    return file_list, dir_list

def zip_files():
    pass
def copy_files(source, destination): # if destination is missing create it
    pass
def grep_search(dir, pattern):
    pass


if __name__ == "__main__":
    find_files()