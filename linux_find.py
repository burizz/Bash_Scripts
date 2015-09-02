#!/usr/bin/env python
import sys
import os
import subprocess

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


def copy_files(source, destination):
    """ Copy source to destionation, if destination doesn't exist, it is created """ 
    with open(source, 'r') as file_object:
        text = file_object.read()
        file_object.close()
         
    with open(destination, 'w') as write_object:
        write_object.write(text)
        write_object.close()
    
    print "Copied %s to %s" % (source, destination)


def zip_files(name_of_zip, array_of_files):
    """Create a ZIP file containing the array of files"""
    #os.system('zip' + name_of_zip + array_of_files)
    for item in array_of_files:
        subprocess.call(['zip', name_of_zip, item])

if __name__ == "__main__":
    #copy_files('/home/burizz/Desktop/sirenie.txt', '/home/burizz/Desktop/askldjs.txt')
    #find_files()
    zip_files('sirenie', ['/home/burizz/Desktop/asd', '/home/burizz/Desktop/askjdh'])


# 5. find and print all strings that match a certain criteria from a file
def grep_search(directory, pattern):
    pass
