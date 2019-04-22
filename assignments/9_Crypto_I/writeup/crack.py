#!/usr/bin/env python3

import hashlib
import string

def crack():
    hash_file = open("hashes.txt") # open and read hashes.txt
    passwords = open("passwords.txt") # open and read passwords.txt
    characters = string.ascii_lowercase
    
    hashes = hash_file.read().split('\n')

    for p in passwords:
        for c in characters:
            # crack hashes

            # print hashes as 'input:hash'
            # i.e.  yeet:909104cdb5b06af2606ed4a197b07d09d5ef9a4aad97780c2fe48053bce2be52
            context = hashlib.sha256()

            test = (c + p).rstrip()
            context.update(bytes(test, 'ascii'))
            d = context.hexdigest()
            
            if d in hashes:
                print("{}:{}".format(test, d))

if __name__ == "__main__":
    crack()
