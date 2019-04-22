#!/usr/bin/env python3

import hashlib
import string
import socket
import time

def server_crack():
    flag = ""

    password_file = open("passwords.txt", 'r')
    passwords = password_file.read().split('\n')

    characters = string.ascii_lowercase
    server_ip = '134.209.128.58'
    server_port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((server_ip, server_port))
    data = s.recv(1024)
    # parse data
    # crack 3 times
    crack = 0
    
    while data != b"":
        if crack == 3:
            flag = data.decode("ascii").rstrip()
            break

        serv_h = data.decode("ascii").split("\n")[2].rstrip()
        found = False
        print("Finding input for {}".format(serv_h))
        
        for p in passwords:
            if not found:
                for c in characters:
                    context = hashlib.sha256()

                    test = (c + p).rstrip()
                    context.update(bytes(test, 'ascii'))
                    h = context.hexdigest()
                    
                    if serv_h == h:
                        found = True
                        s.send(bytes(test + '\n', 'ascii'))
                        print("Sent {}".format(test))
                        crack += 1
                        
        if found:
            data = s.recv(1024)
        else:
            print("Couldn't find hash for {}".format(serv_h))
            data = b""

    print(flag)

if __name__ == "__main__":
    server_crack()
