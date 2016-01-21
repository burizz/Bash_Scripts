#!/usr/bin/env python

import smtplib, subprocess, gzip, shutil, os, time


def dump_database(db_host, db_user, db_pass, sql_dump_filename, backup_dir):
    args = ["mysqldump", "-h", db_host, "-u", db_user, "-p" + db_pass, "--max_allowed_packet=512M", "--all-databases", "--ignore-table=mysql.event"]

    with open(sql_dump_filename, 'w', 0) as f:
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        f.write(p.communicate()[0])
        f.close()

    timestamp = time.strftime("%Y_%m_%d")
    gzip_with_timestamp = "%s_%s.gz" % (sql_dump_filename, timestamp)

    with open(sql_dump_filename, "rb") as file_in, gzip.open(gzip_with_timestamp, "wb") as file_out:
            shutil.copyfileobj(file_in, file_out)
            os.remove(sql_dump_filename)  # Remove uncompressed file.

    return p.returncode


def send_mail(sender, receivers, message):

    try:
        smtp_object = smtplib.SMTP('localhost', 25)
        smtp_object.sendmail(sender, receivers, message)
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"


def cleanup(backup_dir, files_to_keep):

    file_data = {}

    for filename in os.listdir(backup_dir):
        file_data[filename] = os.stat(filename).st_mtime

    sorted_files = sorted(file_data.items())

    delete = len(sorted_files) - files_to_keep
    for x in range(0, delete):
        print "Removed older backup - %s" % (sorted_files[x][0])
        print "Keeping the last %s backups" % (files_to_keep)
        os.remove(sorted_files[x][0])


def main():

    sender = "atlassian_mysql@eda-tech.com"
    receivers = ["borisy@delatek.com", "monitor@secureemail.biz"]
    backup_dir = "/home/veeambackup"
    files_to_keep = 2

    return_code = dump_database("localhost", "root", "1234", "/home/veeambackup/atlassian_mysql_backup.sql", backup_dir)
    cleanup(backup_dir, files_to_keep)

    if return_code == 0:
        print "Atlassian MySQL Backup - OK"
        send_mail(sender, receivers, "Atlassian MySQL Backups - OK" "MySQL Backup completed successfully OK")
    else:
        print "Atlassian MySQL Backups gave an ERROR !"
        send_mail(sender, receivers, "Atlassian MySQL Backups - Gave an ERROR!" "MySQL Backup failed - Need to investigate!!")

if __name__ == "__main__":
    main()

# To test send_mail func