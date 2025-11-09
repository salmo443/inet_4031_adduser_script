#!/usr/bin/python3

# INET4031 - Add Users Script with Dry-Run Mode
# Author: Salman Mahamed
# Date: November 2025

import os
import re
import sys

def main():
    # open /dev/tty so input() works even when stdin is redirected
    with open('/dev/tty') as tty:
        dry_run = input("Run in dry-run mode? (Y/N): ").strip().lower() if tty else 'n'
        if tty:
            dry_run = tty.readline().strip().lower()
        dry = (dry_run == 'y')

    # read each line from input file
    for line in sys.stdin:
        # skip comment lines
        match = re.match("^#", line)
        # split fields by ':'
        fields = line.strip().split(':')

        # if the line is invalid or commented, skip
        if match or len(fields) != 5:
            if dry:
                if match:
                    print("Skipping commented line.")
                else:
                    print("Error: missing fields ->", line.strip())
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

        # if dry-run, just show what command would run
        if dry:
            print("DRY-RUN: Would run ->", cmd)
        else:
            os.system(cmd)

        # show password being set for user
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # if dry-run, show password command, else run it
        if dry:
            print("DRY-RUN: Would run ->", cmd)
        else:
            os.system(cmd)

        # loop through group list and add user
        for group in groups:
            if group != '-':   # skip '-' marker for no group
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                if dry:
                    print("DRY-RUN: Would run ->", cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
