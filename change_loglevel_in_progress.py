#/usr/bin/env python
import subprocess
import os
from datetime import datetime # used only to add timestamp to backed up files.

file_to_edit = "logback.xml"
source_text = "TRACE"
replace_text = "ERROR"
processed_files = []  # Array used to keep track of all files that have been processed


def backup_file(file_to_backup, backup_destination):
    """ Copy file to backup dir """
    timestamp = datetime.now().strftime('%Y-%m-%d')
    path_to_backup = backup_destination + file_to_backup + timestamp

    with open(file_to_backup) as text:
        with open(path_to_backup, 'w') as backedup_file:
            for line in text:
                backedup_file.write(line)
                backedup_file.close()

    # subprocess.call(['cp', file_to_backup, backup_destination])
    print "Backing up file %s to folder : %s ! " % (file_to_backup, backup_destination)

def replace_loglevel(file_to_edit, source_text, replace_text):
    """ Open file and replace the source_text with the replace_text strings """
    open_file = open(file_to_edit, 'r')
    text_from_original = open_file.read()
    open_file.close()

    file_to_write = open(file_to_edit, 'w')
    file_to_write.write(text_from_original.replace(source_text, replace_text))
    print "Replacing string %s with string %s in file %s" % (source_text, replace_text, file_to_edit)

def backup_and_edit_files(dir_path, backup_destination):
    """ Backup the file and replace the source_text with replace_text """
    for item in os.listdir(dir_path): # Iterate over each dir in the dir_path
        path = os.path.join(dir_path, item) # Create full path to file
        if path not in processed_files:
            if os.path.isfile(path) and item == file_to_edit: # Match filename to be the same as in file_to_edit
                print "Matched file %s " % (file_to_edit)
                print "Backing up the current file - %s - before editing" % (item)
                backup_file(path, backup_destination)
                print "Replacing loglevel from %s to %s " % (source_text, replace_text)
                replace_loglevel(path, source_text, replace_text)
                processed_files.append(path)
                print "Processed - %s" % path
            elif os.path.isdir(path): # Only descend into dirs
                backup_and_edit_files(path, backup_destination)

if __name__ == '__main__':
    dir_path = ""   # Put full path to dir to search in
    backup_destination = ""  # Dir to backup to
    backup_and_edit_files(dir_path, backup_destination)

# Fix the backup, have to add a timestamp at each backed up file
