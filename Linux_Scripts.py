#!/usr/bin/env python
import sys # used for passing arguments to the script
import os
import subprocess
import re # used for matching stuff in the apache log parsing function
import paramiko # used for connecting to servers over SSH

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
    for item in array_of_files:
        subprocess.call(['zip', name_of_zip, item])

def grep_search(file, pattern):
    """ Pass file and pattern - if pattern in line, print the line """
    with open(file, 'r') as file_object:
        for line in file_object.readlines():
            if line.find(pattern) != -1:
                print line
                
def dir_usage(path):
    """ Check disk usage of a directory - provide full path"""
    cmd = 'du '
    arg = '-sh '
    os.system(cmd + arg + path)

def check_port(port):
    """ Check if a certain port is open, provide info about processes using it """
    cmd = 'netstat '
    arg = '-apn '
    search = 'grep ' + port
    os.system(cmd + arg + '|' +  search)

def user_add(user_name, action):
    """ Add or delete a Linux User - user, pass, add or delete"""
    add = 'useradd '
    delete = 'userdel '
    if action == 'add':
        os.system(add + user_name)
        print "User %s created." % (user_name)
        print "Switch to %s and execute passwd, to change your password" % (user_name)
    elif action == 'delete':
        os.system(delete + user_name)
        print "User %s deleted" % (user_name)
    else:
        print "Action should be either 'add' or 'delete', not - %s" % (action)
        
def server_info():
    result = subprocess.Popen(['uname', '-a'], stdout=subprocess.PIPE)
    uname = result.stdout.read()
    return uname

def apache_log_parser(log_path):
    """ Parse access log to show only - return code, host, bytes_sent """
    log_file = open(log_path, 'r')
    for line in log_file.readlines():
        #compile regex to match the values of status, host and bytes
        log_line_re = re.compile(r'''(?P<remote_host>\S+) #IP ADDRESS
                              \s+ #whitespace
                              \S+ #remote logname
                              \s+ #whitespace
                              \S+ #remote user
                              \s+ #whitespace
                              \[[^\[\]]+\] #time
                              \s+ #whitespace
                              "[^"]+" #first line of request
                              \s+ #whitespace
                              (?P<status>\d+)
                              \s+ #whitespace
                              (?P<bytes_sent>-|\d+)
                              \s* #whitespace
                              ''', re.VERBOSE)
        # match entries with regex
        m = log_line_re.match(line)
        print m.groupdict() # print a dictionary of the matched values

def ssh_connect(hostname, port, user, passwd, command):
    """ Connect to a server over SSH and execute commands """
    paramiko.util.log_to_file('python_ssh.log')
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys() # load known_hosts file of the user
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # set policy to autoadd keys of unknown hosts
    ssh_client.connect(hostname, port, user, passwd)
    stdin, stdout, stderr = ssh_client.exec_command(command) # provide full_path to cmd in linux
    output = stdout.read()
    print "SSH connection successful. Closing connection..." 
    ssh_client.close()
    print "Connection closed !"
    return output

def main():
    #copy_files('/home/burizz/Desktop/test.txt', '/home/burizz/Desktop/askldjs.txt')
    #walk_dirs('/home/burizz')
    #find_files()
    #zip_files('test123', ['/home/burizz/Desktop/asd', '/home/burizz/Desktop/askjdh'])
    #grep_search('/home/burizz/Desktop/asd', 'test123')
    #dir_usage('/etc')
    #check_port('631')
    #user_add('testing', 'delete')
    #print server_info()
    #apache_log_parser('/var/log/httpd/access_log')
    print ssh_connect('localhost', 22, 'burizz', 'case363166', '/sbin/ifconfig')
    
if __name__ == "__main__":
    main()
