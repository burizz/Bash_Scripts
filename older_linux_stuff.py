#/usr/bin/env python

def sed(pattern, replacement, file_one, file_two):
    """ A funciton similar to the Unix sed program, i.e.
    get a pattern and a replacement strings if the pattern exists, 
    replace it with the string, if opening a file does not work, raise an exception """
    try :
        initial_file = open(file_one, 'r')
        final_file = open(file_two, 'w')

        for item in initial_file:
            item = item.replace(pattern, replacement)
            final_file.write(item)
        
        initial_file.close()
        final_file.close()

    except IOError:
        print "Can't open or write to file"
    else:
        print "Replaced occurances of %s with %s successfully" % (pattern, replacement)


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
    
def get_gids():
    """ Open Unix group file and return only the group IDs """

    with open('/etc/group', 'r') as groups_file:
        group_lines = []
        for line in groups_file:
            group_lines.append(line.strip().split(':'))
    
    gids = []
    gid_index = 2
    for item in group_lines:
        gids.append(item[gid_index])
	
    print gids
   
   
def argv_excercise1():
    """ Exercies from Learn Python the Hard Way """
    from sys import argv
    
    script, filename = argv
    
    print "We're going to erase %r." % filename
    print "If you don't want that, hit CTRL-C (^C)."
    print "If you do want that, hit RETURN."
    
    raw_input("?")
    
    print  "Opening the file..."
    target = open(filename, 'w')
    
    print "Truncating the file. Goodbye!"
    target.truncate()
    
    print "Now I'm going to ask you for three lines."
    
    line1 = raw_input("line1: ")
    line2 = raw_input("line2: ")
    line3 = raw_input("line3: ")
    
    print "I'm going to write these to the file."
    
    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")
    
    print "And finally, we close it."
    target.close()

if __name__ == '__main__':
    edit_user_attrib('users.txt')
    output_string = "['PoolManager name:JDBC/BOSSCS', 'PoolManager object:2082207303', 'Total number of connections: 1 (max/min 10/1, reap/unused/aged 180/1800/0, connectiontimeout/purge 180/EntirePool)', '(testConnection/inteval false/0, stuck timer/time/threshold 0/0/0, surge time/connections 0/-1)', 'Shared Connection information (shared partitions 200)', '  No shared connections', '', 'Free Connection information (free distribution table/partitions 5/1)', '  (0)(0)MCWrapper id 2a405b3a  Managed connection WSRdbManagedConnectionImpl@2112be64  State:STATE_ACTIVE_FREE', '', '  Total number of connection in free pool: 1', 'UnShared Connection information']"
    total_conn_number(output_string)
    get_gids()
