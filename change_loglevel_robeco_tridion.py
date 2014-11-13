#/usr/bin/env python
import subprocess
import os

file_to_edit = "logback.xml"
source_text = "TRACE"
replace_text = "ERROR"
processed_files = []  # Array used to keep track of all files that have been processed


def backup_file(file_to_backup, backup_dir):
    """ Get a file and copy it with a different name for backup """
    backup_config = subprocess.call(['cp', file_to_backup, backup_dir])
    print "Backing up file %s to folder : %s ! " % (file_to_backup, backup_dir)

def replace_loglevel(file_to_edit, source_text, replace_text):
    """ Open file and replace the source_text with the replace_text strings """
    open_file = open(file_to_edit, 'r')
    text_from_original = open_file.read()
    open_file.close()

    file_to_write = open(file_to_edit, 'w')
    file_to_write.write(text_from_original.replace(source_text, replace_text))
    print "Replacing string %s with string %s in file %s" % (source_text, replace_text, file_to_edit)

def backup_and_edit_files(dir_path, backup_dir):
    """ Backup the file and replace the source_text with replace_text """
    for item in os.listdir(dir_path): # Iterate over each dir in the dir_path
        path = os.path.join(dir_path, item) # Create full path to file
        if path not in processed_files:
            if os.path.isfile(path) and item == file_to_edit: # Match filename to be the same as in file_to_edit
                print "Matched file %s " % (file_to_edit)
                print "Backing up the current file - %s - before editing" % (item)
                backup_file(path, backup_dir)
                print "Replacing loglevel from %s to %s " % (source_text, replace_text)
                replace_loglevel(path, source_text, replace_text)
                processed_files.append(path)
                print "Processed - %s" % path
            else:
                backup_and_edit_files(path, backup_dir)

if __name__ == '__main__':
    dir_path = "/var/apphome/tridion_cms/webapps/"
    backup_dir = "/tmp/eds1057/"
    backup_and_edit_files(dir_path, backup_dir)
