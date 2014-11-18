#/usr/bin/env python
import os

def backup_file(file_to_backup):
    """ Copy file to backup dir """
    path_to_backup = file_to_backup + "_bkp_eds1057"

    with open(file_to_backup) as text:
        with open(path_to_backup, 'w') as backedup_file:
            for line in text:
                backedup_file.write(line)
                backedup_file.close()
    print "Backing up file %s to file : %s ! " % (file_to_backup, path_to_backup)

def replace_loglevel(file_to_edit, source_text, replace_text):
    """ Open file and replace the source_text with the replace_text strings """
    open_file = open(file_to_edit, 'r')
    text_from_original = open_file.read()
    open_file.close()

    file_to_write = open(file_to_edit, 'w')
    file_to_write.write(text_from_original.replace(source_text, replace_text))
    print "Replacing string %s with string %s in file %s" % (source_text, replace_text, file_to_edit)

file_to_edit = "logback.xml"
source_text = "TRACE"
replace_text = "ERROR"
processed_files = []  # Array used to keep track of all files that have been processed

def backup_and_edit_files(dir_path, backup_destination):
    """ Backup the file and replace the source_text with replace_text """
    for item in os.listdir(dir_path): # Iterate over each dir in the dir_path
        path = os.path.join(dir_path, item) # Create full path to file
        if path not in processed_files:
            if os.path.isfile(path) and item == file_to_edit: # Match filename to be the same as in file_to_edit
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

# Fix the backup, create a copy of the initial file with a different name in the same dir
# Move initial vars before the last function