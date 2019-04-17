#!/usr/bin/env python2

import sys
import struct
import datetime


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0x8BADF00D
VERSION = 1

SECTION_ASCII = 0x1
SECTION_UTF8 = 0x2
SECTION_WORDS = 0x3
SECTION_DWORDS = 0x4
SECTION_DOUBLES = 0x5
SECTION_COORD = 0x6
SECTION_REFERENCE = 0x7
SECTION_PNG = 0x8
SECTION_GIF87 = 0x9
SECTION_GIF89 = 0xA

if len(sys.argv) < 2:
    sys.exit("Usage: python stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8

magic, version, timestamp = struct.unpack("<LLL", data[0:12])
curr = 12

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

(author,) = struct.unpack("8s", data[curr:(curr+8)])
curr += 8
(section_count,) = struct.unpack("<L", data[curr:(curr+4)])
curr += 4

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: EPOCH %d -- UTC %s" % (int(timestamp), str(datetime.datetime.utcfromtimestamp(timestamp))))
print("AUTHOR: %s" % str(author))
print("SECTION COUNT: %d" % int(section_count))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

for section in range(1, section_count+1):
    (stype, slen) = struct.unpack("II", data[curr:(curr+8)])
    curr += 8
    if stype != 0:
        (svalue,) = struct.unpack("%ds" % slen, data[curr:(curr+slen)])
        if stype == SECTION_ASCII:
            print("ASCII SECTION %d" % section)
            print("%s" % str(svalue))
            
        elif stype == SECTION_UTF8:
            print("UTF8 SECTION %d" % section)
            print("%s" % svalue.decode('utf8'))
        
        elif stype == SECTION_WORDS:
            print("WORDS SECTION %d" % section)
            num_words = slen / 4
            for w in range(1, num_words+1):
                (word,) = struct.unpack("L", svalue[(w-1)*4:w*4])
                print("WORD %d : %s" % (w, hex(word)))
            
        elif stype == SECTION_DWORDS:
            print("DWORDS SECTION %d" % section)
            num_dwords = slen / 8
            for dw in range(1, num_dwords+1):
                (dword,) = struct.unpack("Q", svalue[(dw-1)*8:dw*8])
                print("DWORD %d : %s" % (dw, hex(dword)))
            
        elif stype == SECTION_DOUBLES:
            print("DOUBLES SECTION %d" % section)
            num_doubles = slen / 8
            for d in range(1, num_doubles+1):
                (double,) = struct.unpack("d", svalue[(d-1)*8:d*8])
                print("DOUBLE %d : %f" % (d, double))
        
        elif stype == SECTION_COORD:
            if slen != 16:
                bork("Bad coordinate section encounted in body in section %d" % (section + 1))
                
            print("COORD SECTION %d" % section)
            latitude, longitude = struct.unpack("dd", svalue[0:slen])
            print("Latitude %f, Longitude %f" % (latitude, longitude))
        
        elif stype == SECTION_REFERENCE:
            print("REFERENCE SECTION %d" % section)
            ref = struct.unpack("L", svalue)
            if ref not in range(0, section_count):
                bork("Section reference is not inside this file!")
            print("Referencing section %d" % (ref + 1))
            
        elif stype == SECTION_PNG:
            print("PNG SECTION %d" % section)
            
            filename = "png%d.png" % section
            out = open(filename, "wb")
            
            pngmagic1 = 0x474e5089
            pngmagic2 = 0x0a1a0a0d
            out.write(struct.pack("ii", pngmagic1, pngmagic2))
            out.write(data[curr:(curr+slen)])
            out.close()
            
            print("Created png file %s" % filename)
                   
        elif stype == SECTION_GIF87:
            print("GIF87 SECTION %d" % section)
            # Signature: GIF87a
        
        elif stype == SECITON_GIF89:
            print("GIF89 SECTION %d" % section)
            # Signature: GIF89a
            
        else:
            bork("Unknown section type reached")
            
        curr += slen
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
