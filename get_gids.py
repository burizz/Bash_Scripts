#!/usr/bin/env python

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
    

if __name__ == "__main__":
    get_gids()


#