#!/usr/bin/python3
# part4.py

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad
from Cryptodome import Random 
from project import *
import json

# choose the key and ctr at random
key = Random.get_random_bytes(16)
ctr = Random.get_random_bytes(16)

# write the plaintext in file "P.txt"
P = b"This is a known message!"
with open("P.txt", "wb") as f: 
  f.write(P)

# encrypt "P.txt" with CTR mode into "C.txt"
encrypt_ctr("P.txt", "C.bin", key, ctr)
C = open("C.bin", "rb").read() 

# print the plaintext P and ciphertext C
print("P:", P.hex() )
print("C:", C.hex() )

#!!!!! ENCRYPT THE SECRET MESSAGE (in secret.txt)!!!!
encrypt_ctr("secret.txt", "target.bin", key, ctr)
target = open("target.bin", "rb").read()
print("target:", target.hex() )

P = b'\x54\x68\x69\x73\x20\x69\x73\x20\x61\x20\x6b\x6e\x6f\x77\x6e\x20\x6d\x65\x73\x73\x61\x67\x65\x21'
C = b'\xed\x6b\x6e\xe5\x50\x65\x0f\x5b\x9b\xb6\x99\x67\x8e\x24\x42\x60\xc3\xbc\x87\xec\x8a\x31\x72\xd7'

target = b'\xd2\x6d\x68\xe1\x1e\x2c\x0c\x17\x9b\xff\x9c\x7d\x84\x2b\x58\x60\xcf\xad\x9f\xbf\xa8\x02\x45\xfc'

keys = [ i ^ j for i,j in zip(P, C) ]
print(keys)
plain = [ i ^ j for i,j in zip(keys, target)]
print(bytes(plain))
#breaking it

