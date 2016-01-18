#!/usr/bin/env python

import smtplib, subprocess, gzip, shutil, os, time


def dump_database(db_host, db_user, db_pass, sql_dump_filename):
    args = ["mysqldump", "-h", db_host, "-u", db_user, "-p" + db_pass, "--max_allowed_packet=512M", "--all-databases", "--ignore-table=mysql.event"]

    with open(sql_dump_filename, 'w', 0) as f:
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        f.write(p.communicate()[0])
        f.close()

    timestamp = time.strftime("%Y%m%d")
    gzip_with_timestamp = "%s_%s.gz" % (sql_dump_filename, timestamp)

    with open(sql_dump_filename, "rb") as file_in, gzip.open(gzip_with_timestamp, "wb") as file_out:
            shutil.copyfileobj(file_in, file_out)
            os.remove(sql_dump_filename)  # Remove uncompressed file.

    return p.returncode


def send_mail(sender, receivers, message):

    try:
        smtpObj = smtplib.SMTP('localhost', 25)
        smtpObj.sendmail(sender, receivers, message)
        print "Successfully sent email"
    except smtplib.SMTPException:
        print "Error: unable to send email"


def main():

    sender = "atlassian_mysql@eda-tech.com"
    receivers = ["borisy@delatek.com", "monitor@secureemail.biz"]

    return_code = dump_database("localhost", "root", "1234", "/home/veeambackup/atlassian_mysql_backup.sql")

    if return_code == 0:
        print "Atlassian MySQL Backup - OK"
        send_mail(sender, receivers, "Atlassian MySQL Backups - OK" "MySQL Backup completed successfully OK")
    else:
        print "Atlassian MySQL Backups gave an ERROR !"
        send_mail(sender, receivers, "Atlassian MySQL Backups - Gave an ERROR!" "MySQL Backup failed - Need to investigate!!")

    os.system("find /home/veeambackup/* -mtime +3 -exec rm {} \;") # Remove older dumps. Should keep only three.

if __name__ == "__main__":
    main()
