#!/usr/bin/env python
import os
import shutil

def backup_file(file_to_backup):
    """ Copy file to backup dir """
    destination_file = file_to_backup + "_bkp_eds1057"
    shutil.copyfile(file_to_backup, destination_file)
    print "Backing up file %s to file : %s ! " % (file_to_backup, destination_file)

def replace_loglevel(file_to_edit, source_text, replace_text):
    """ Open file and replace the source_text with the replace_text strings """
    open_file = open(file_to_edit, 'r')
    text_from_original = open_file.read()
    open_file.close()

    file_to_write = open(file_to_edit, 'w')
    file_to_write.write(text_from_original.replace(source_text, replace_text))
    file_to_write.close()
    print "Replacing string %s with string %s in file %s" % (source_text, replace_text, file_to_edit)

file_to_edit = "logback.xml"
source_text = "TRACE"
replace_text = "ERROR"
processed_files = []  # Array used to keep track of all files that have been processed

def backup_and_edit_files(dir_path):
    """ Backup the file and replace the source_text with replace_text """
    for item in os.listdir(dir_path): # Iterate over each dir in the dir_path
        path = os.path.join(dir_path, item) # Create full path to file
        if path not in processed_files:
            if os.path.isfile(path) and item == file_to_edit: # Match filename to be the same as in file_to_edit
                print "Backing up the current file - %s - before editing" % (item)
                backup_file(path)
                print "Replacing loglevel from %s to %s " % (source_text, replace_text)
                replace_loglevel(path, source_text, replace_text)
                processed_files.append(path)
                print "Processed - %s" % path
            elif os.path.isdir(path): # Only descend into dirs
                backup_and_edit_files(path)

if __name__ == '__main__':
    dir_path = ""   # Put full path to dir to search in
    backup_and_edit_files(dir_path)

"""
Runtime:

Python:
real	0m0.017s
user	0m0.007s
sys	    0m0.006s

PHP:
real	0m0.013s
user	0m0.007s
sys	0m0.004s

"""