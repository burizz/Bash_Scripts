#/usr/bin/env python

#import subprocess

def edit_user_attrib(file_path):
    ''' Get a list of users as input and delete a specific ODSEE attribute for all users '''
    ldap_user = ''
    del_attrib_content = "dn: uid=%s,ou=unixuser,ou=People,dc=uas,dc=robeco,dc=nl\n\
changetype: modify\n\
delete: passwordexpirationtime " % ldap_user

    dsee_users = open(file_path, 'r')

    del_attrib_ldif = open('delPassAttrib.ldif', 'r+')

    for item in dsee_users:
        ldap_user = item
        del_attrib_ldif.write(del_attrib_content)
        #subprocess.call(['ldapmodify', '-v', '-h', 'rbcdeesh750', '-p', '389', '-x', '-w', 'hp0nly2013', '-D', '"cn=Directory Manager"', '-f', "'/tmp/delPassAttrib.ldif'"])


if __name__ == '__main__':
    edit_user_attrib('srb_users.txt')


