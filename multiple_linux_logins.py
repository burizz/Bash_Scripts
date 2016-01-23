#!/usr/bin/env python
import paramiko

def ssh_connect(hostname, port, user, passwd, command):
    """ Connect to a server over SSH and execute commands """
    paramiko.util.log_to_file('ssh_output.log')
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

def store_users_and_hosts():
    """
    - Load users from users.txt and build an associative array of the user/pass pairs - in format - user:pass
    - Load hosts from hostnames.txt and build a list of them.
    """
    users = {}

    # Read users from file and build a dict of all user:pass pairs
    with open('users.txt', 'r') as users_object:
        user_list = users_object.read().replace(" ", "").strip().split(",")
        users_object.close()

    for pair in user_list:
        pair = pair.split(':')
        users[pair[0]] = pair[1]

    # Build a list of hosts from hostnames.txt file
    with open('hostnames.txt', 'r') as hosts_object:
        hostnames = hosts_object.read().replace(" ", "").strip().split(",")
        hosts_object.close()

    return users, hostnames

def main():
    port = 22
    command = '/sbin/ifconfig'
    users, hostnames = store_users_and_hosts()

    for host in hostnames:
        for user in users:
            print "%s logged in to %s" % (user, host)
            print ssh_connect(host, port, user, users[user], command)

if __name__ == "__main__":
    main()

# Check how to encrypt, decrypt passwords
