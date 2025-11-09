# inet_4031_adduser_script

#INET4031 Add Users Script and User List
Program Description

This program automates the process of adding multiple user accounts to a Linux system. Normally, an administrator would run commands such as sudo adduser username, sudo passwd username, and sudo adduser username groupname. This script performs those same tasks automatically by reading user details from an input file and running the necessary commands in sequence. It saves time, prevents mistakes, and makes large-scale user management consistent and repeatable.

#Program User Operation

This section explains how to use the program and what to know before running it. The comments inside the code describe how each part works.

Input File Format

Each line in the input file represents one user account and follows this format:

username:password:lastname:firstname:group1,group2

Fields

username – login name

password – account password

lastname and firstname – stored in user info (GECOS field)

group1,group2 – optional list of groups to add the user to

Lines starting with # are ignored (comments). If you don’t want a user added to any group, put - for that field.
Example:
user01:pass01:Smith:John:group01,group02
user02:pass02:Doe:Jane:-
# This line is skipped

Command Execution

Run the script from your Ubuntu terminal using:
sudo ./create-users.py < create-users.input

Make sure the script is executable before running it by using:
chmod +x create-users.py

This will read the input file, create each user, set their password, and add them to any groups listed. Each action is printed so you can verify what’s happening.

#Dry Run

A dry run lets you test the script safely. When running in dry-run mode, the program prints all the commands (adduser, passwd, adduser group) but doesn’t actually execute them. This allows you to confirm everything looks correct before uncommenting the os.system(cmd) lines to run the real version.
