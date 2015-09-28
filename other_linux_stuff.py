#/usr/bin/env python

#import subprocess

def edit_user_attrib(file_path):
    ''' Get a list of users as input and delete a specific ODSEE attribute for all users '''
    ldap_user = ''
    del_attrib_content = "dn: uid=%s,ou=unixuser,ou=People,dc=uas,\n\
changetype: modify\n\
delete: passwordexpirationtime " % ldap_user

    dsee_users = open(file_path, 'r')

    del_attrib_ldif = open('delPassAttrib.ldif', 'r+')

    for item in dsee_users:
        ldap_user = item
        del_attrib_ldif.write(del_attrib_content)
        #subprocess.call(['ldapmodify', '-v', '-h', 'hostname', '-p', '389', '-x', '-w', 'password', '-D', '"cn=Directory Manager"', '-f', "'/tmp/delPassAttrib.ldif'"])


def total_conn_number(output_string):
    """ Get a string as input, find where in the string "total connections count is located" and display only the value for "Total number of connection: " with nothing after it. """

    total_connections = 'Total number of connections'
    delimiter_string = '('

    start_index = output_string.find(total_connections)
    end_index = output_string.find(delimiter_string, start_index)

    print output_string[start_index:end_index]
    

if __name__ == '__main__':
    edit_user_attrib('users.txt')
    output_string = "['PoolManager name:JDBC/BOSSCS', 'PoolManager object:2082207303', 'Total number of connections: 1 (max/min 10/1, reap/unused/aged 180/1800/0, connectiontimeout/purge 180/EntirePool)', '(testConnection/inteval false/0, stuck timer/time/threshold 0/0/0, surge time/connections 0/-1)', 'Shared Connection information (shared partitions 200)', '  No shared connections', '', 'Free Connection information (free distribution table/partitions 5/1)', '  (0)(0)MCWrapper id 2a405b3a  Managed connection WSRdbManagedConnectionImpl@2112be64  State:STATE_ACTIVE_FREE', '', '  Total number of connection in free pool: 1', 'UnShared Connection information']"
    total_conn_number(output_string)
