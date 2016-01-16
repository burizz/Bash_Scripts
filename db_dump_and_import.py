#!/usr/bin/env python

import subprocess, paramiko, os


def exec_remote_cmd(remote_host, remote_port, remote_user, remote_pass, remote_cmd):
    """ Connect to a server over SSH and execute commands """

    # Uncomment line below if we need SSH to log stuff
    # paramiko.util.log_to_file('python_ssh.log')

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()  # load known_hosts file of the user
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # auto-add keys of unknown hosts
    ssh_client.connect(remote_host, remote_port, remote_user, remote_pass)

    stdin, stdout, stderr = ssh_client.exec_command(remote_cmd)
    output = stdout.read()
    ssh_client.close()

    return output


def dump_database(db_host, db_user, db_pass, db_name, sql_dump_filename):
    """ Dump MySQL DB with Drop Database commands to file """

    args = ['mysqldump', '-h', db_host, '-u', db_user, '-p' + db_pass, '--add-drop-database', db_name]

    with open(sql_dump_filename, 'w', 0) as f:
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        f.write(p.stdout.read())
        f.close()


def send_dump(hostname, port, username, password, sql_file, dest_sql_file):
    """ Send sql file to remote host over SCP """

    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()  # load known_hosts file of the user
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # auto-add keys of unknown hosts
    ssh.connect(hostname, port, username, password)

    sftp = ssh.open_sftp()
    sftp.put(sql_file, dest_sql_file)  # Send src to remote dest over scp
    sftp.close()
    ssh.close()


def main():
    os.system('clear')  # Clear screen before executing stuff
    
    remote_host = "localhost"
    remote_port = 22
    remote_user = "user"
    remote_pass = "pass"

    local_sql_file = "/home/mysql_dump.sql"
    remote_sql_file = "/home/dump.sql"

    db_host = 'localhost'
    db_user = 'user'
    db_pass = 'pass'
    db_name = 'database_name'
    sql_dump_filename = '/home/mysql_dump.sql'

    # Set command for importing SQL dump on remote server
    remote_cmd = "mysql -u user -ppass db_name < %s" % (remote_sql_file)

    # Dump db from any host in local SQL file
    dump_database(db_host, db_user, db_pass, db_name, sql_dump_filename)

    # Send SQL dump to remote server
    send_dump(remote_host, remote_port, remote_user, remote_pass, local_sql_file, remote_sql_file)

    # Import SQL dump on remote server in DB
    exec_remote_cmd(remote_host, remote_port, remote_user, remote_pass, remote_cmd)


if __name__ == "__main__":
    main()
