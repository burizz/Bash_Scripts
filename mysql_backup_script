def dump_database(db_host, db_user, db_pass, db_name, sql_dump_filename):
    args = ['mysqldump',
            '-h', db_host,
            '-u', db_user,
            '-p' + db_pass,
            '--max_allowed_packet=512M',
            '--all-databases',
            '--ignore-table=mysql.event',
            '>',
            sql_dump_filename]

    with open(sql_dump_filename, 'w', 0) as f:
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        f.write(p.stdout.read())
        f.close()
