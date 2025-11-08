#!/usr/bin/python3

# INET4031
# Salman Mahamed
# Date Created: Nov 2025
# Last Modified: Nov 2025

import os     # run shell commands (adduser, passwd)
import re     # handle regex to skip lines or comments
import sys    # read input lines from stdin

def main():
    for line in sys.stdin:
        # skip comment lines that start with '#'
        match = re.match("^#", line)

        # split line data by ':' into list fields
        fields = line.strip().split(':')

        # skip if commented or wrong number of fields
        if match or len(fields) != 5:
            continue

        # store username, password, and name info
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # separate multiple groups by commas
        groups = fields[4].split(',')

        # show which user is being added
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # dry run: comment these out for test mode
        #print(cmd)
        #os.system(cmd)

        # show password being set for user
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # dry run: comment these out for test mode
        #print(cmd)
        #os.system(cmd)

        # loop through group list and add user
        for group in groups:
            if group != '-':   # skip empty group marker
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                #print(cmd)
                #os.system(cmd)

if __name__ == '__main__':
    main()
