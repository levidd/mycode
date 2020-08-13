#!/usr/bin/env python3

from csv import reader

with open("csv_users.txt") as csv_file:
    i = 0
    for row in reader(csv_file):
        i+= 1
        filename = "rc_files/admin.rc%d" %(i)
        with open(filename, "w+") as rcfile:
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)
