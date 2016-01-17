#!/usr/bin/env python

import smtplib, subprocess, gzip, shutil, os 


def dump_database(db_host, db_user, db_pass, sql_dump_filename):
    args = ["mysqldump", "-h", db_host, "-u", db_user, "-p" + db_pass, "--max_allowed_packet=512M", "--all-databases", "--ignore-table=mysql.event"]

    with open(sql_dump_filename, 'w', 0) as f:
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        f.write(p.communicate()[0])
        f.close()

    gziped_filename = "%s.gz" % (sql_dump_filename)

    with open(sql_dump_filename, "rb") as file_in, gzip.open(gziped_filename, "wb") as file_out:
            shutil.copyfileobj(file_in, file_out)
            os.remove(sql_dump_filename) # Remove uncompressed file.

    return p.returncode
    

def send_mail(sender, receivers, message):

    try:
        smtpObj = smtplib.SMTP('localhost', 25)
        smtpObj.sendmail(sender, receivers, message)
        print "Successfully sent email"
    except SMTPException:
        print "Error: unable to send email"


def main():
    # Check how to add date timestamp to filename

    sender = "atlassian_mysql@eda-tech.com"
    receivers = ["borisy@delatek.com", "monitor@secureemail.biz"]

    return_code = dump_database("localhost", "root", "1234", "/home/veeambackup/atlassian-all-$(date +%Y%m%d).sql")

    if return_code == 0:
        print "Atlassian MySQL Backup - OK"
        send_mail(sender, receivers, "Atlassian MySQL Backups - OK" "MySQL Backup completed successfully OK")
    else:
        print "Atlassian MySQL Backups gave an ERROR !"
        send_mail(sender, receivers, "Atlassian MySQL Backups - Gave an ERROR!" "MySQL Backup failed - Need to investigate!!")


if __name__ == "__main__":
    main()

# Get timestamp to add to filename
# Remove old dumps should keep only 3.
