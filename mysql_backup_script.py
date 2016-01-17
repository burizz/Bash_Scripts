#!/usr/bin/env python

import subprocess

def dump_database(db_host, db_user, db_pass, sql_dump_filename):
    args = ["mysqldump", "-h", db_host, "-u", db_user, "-p" + db_pass, "--max_allowed_packet=512M", "--all-databases", "--ignore-table=mysql.event"]

    with open(sql_dump_filename, 'w', 0) as f:
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        f.write(p.communicate()[0])
        f.close()

        return p.returncode

if __name__ == "__main__":
    print dump_database('localhost', 'root', '1234', 'dump_db.sql')
