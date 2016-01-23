#!/usr/bin/env python
import os, subprocess, re, paramiko, socket

# Fix menu in main() - include usage specifics of each func
# Review zip func...  should zip on relative path and work on dirs
# Do a func with rsync implementation. To be used for copying dirs also. - shutil
# Add case sens and insens to grep - string.lower()
# Check sed() from older_linux_stuff.py to implement something from it - can remove it there after.


def find_files(path, file_name):
    """
    Recursive find
    path == Starting point
    file_name == File name to search for
    """

    files = walk_dirs(path)[0]

    for item in files:
        if file_name in item:
            print item


def walk_dirs(dir_name):
    """ Walk dirs recursively - return all files' and dirs' full path """
    file_list = []
    dir_list = []

    for root, dirs, files in os.walk(dir_name):
        for item in files:
            file_list.append(os.path.join(root, item))
        for item in dirs:
            dir_list.append(os.path.join(root, item))

    return file_list, dir_list


def copy_file(source, destination):
    """ Copy source to destination - if destination doesn't exist, create it """
    with open(source, 'r') as file_object:
        text = file_object.read()
        file_object.close()

    with open(destination, 'w') as write_object:
        write_object.write(text)
        write_object.close()

    print "Copied %s to %s" % (source, destination)


def zip_files(name_of_zip, array_of_files):
    """ Create zip from a list of files. """
    for item in array_of_files:
        subprocess.call(['zip', name_of_zip, item])
    print "Created %s in %s." % (name_of_zip, os.getcwd())


def grep_search(file, pattern):
    """ Search pattern in file """
    with open(file, 'r') as file_object:
        for line in file_object.readlines():
            if line.find(pattern) != -1:
                print line


def dir_usage(path):
    """ Check disk usage of a directory - provide full path """
    cmd = 'du '
    arg = '-sh '
    os.system(cmd + arg + path)


def user_mod(user_name, action):
    """ Add, delete or purge a Linux User - provide user, pass, action"""
    add = 'useradd '
    delete = 'userdel '
    purge = 'userdel -r '  # Same as delete but removes home directory and files owned by the user

    if action == 'add':
        os.system(add + user_name)
        print "User %s created." % user_name
        passwd = str(raw_input("Enter password for the new user : "))
        os.system('echo ' + passwd + ' | passwd --stdin ' + user_name)

    elif action == 'delete':
        os.system(delete + user_name)
        print "User %s deleted" % user_name

    elif action == 'purge':
        os.system(purge + user_name)
        print "User %s purged - including his home directory and all their files" % user_name

    else:
        print "Action should be either 'add', 'delete' or 'purge', not - %s" % action


def port_checker(address, port):
    """ Check if port is on address is open """
    tcp_socket = socket.socket()
    print "Attempting to connect to %s on port %s" % (address, port)
    try:
        tcp_socket.connect((address, port))
        print "Connected to %s on port %s" % (address, port)
    except socket.error, error:
        print "Connection to %s on port %s failed: %s" % (address, port, error)


def server_info():
    """ :return Kernel info """
    result = subprocess.Popen(['uname', '-a'], stdout=subprocess.PIPE)
    uname = result.stdout.read()
    return uname


def apache_log_parser(log_path):
    """ Parse access log, show only - return code, host, bytes_sent """
    log_file = open(log_path, 'r')
    for line in log_file.readlines():
        # compile regex to match the values of status, host and bytes
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
        print m.groupdict()  # print a dictionary of the matched values


def ssh_connect(hostname, port, user, passwd, command):
    """ Connect to a server over SSH and execute command """

    # Uncomment line if we need paramiko to log info
    paramiko.util.log_to_file('python_ssh.log')

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys() # load known_hosts file of the user
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # set policy to autoadd keys of unknown hosts
    ssh_client.connect(hostname, port, user, passwd)

    stdin, stdout, stderr = ssh_client.exec_command(command)  # provide full_path to cmd in linux
    output = stdout.read()
    print "SSH connection successful. Closing connection..."
    ssh_client.close()
    print "Connection closed !"

    return output


def main():
    os.system('clear')  # Clear screen

    #options_list = [find_files(), walk_dirs(), copy_file(), zip_files(), grep_search(), dir_usage(), user_mod(), port_checker(), server_info(), apache_log_parser(), ssh_connect()]
    menu = '' #remove if not needed

    print "1. Find filenames that match a pattern."
    print "2. Walk dirs recursively and return all filenames and directories"
    print "3. Copy file."
    print "4. Zip a list of files"
    print "5. Grep - Search for a pattern in a file"
    print "6. Disk usage of a directory"
    print "7. User management - add, delete, purge(delete all user files and dirs)"
    print "8. Test port availability - similar to Telnet"
    print "9. Check server info"
    print "10. Parse apache log file"
    print "11. Execute command on remote server over SSH"

    choice = int(raw_input("\nSelect option >> "))
    # - check if choice in range of possible choices

# Test each function examples
    # find_files('/etc/', 'hosts')
    # walk_dirs('/home/burizz')
    # copy_file('/home/burizz/Desktop/file1.txt', '/home/burizz/Desktop/file2.txt')
    # zip_files('zip_file_name', ['/home/burizz/Desktop/file1', '/home/burizz/Desktop/file2'])
    # grep_search('/home/burizz/Desktop/asd', 'test123')
    # dir_usage('/etc')
    # user_mod('user_name', 'add')
    # port_checker('localhost', 80)
    # print server_info()
    # apache_log_parser('/var/log/httpd/access_log')
    # print ssh_connect('localhost', 22, 'user', 'password', '/sbin/ifconfig')

if __name__ == "__main__":
    main()
