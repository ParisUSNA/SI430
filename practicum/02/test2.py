#!/usr/bin/python3
# test2.py
from prac12 import *
from Cryptodome.Cipher import AES

K = b"adbnkq83rafba379"
M = b"This message is " \
  + b"to be decrypted " \
  + b"using CBC mode.\x01"

iv = b"a90jdafaij;afjda"

aes = AES.new(K, AES.MODE_CBC, iv)
C = iv + aes.encrypt(M)
print_cbc_dec(K, C)


