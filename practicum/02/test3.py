#!/usr/bin/python3
# test3.py
from prac12 import *
from Cryptodome.Cipher import AES

K = b"aoiijfadafddafaf"
iv = b"adfa2upijlanfa;0"
M = open("aes.txt", "rb").read() + b"\x05"*5
aes = AES.new(K, AES.MODE_CBC, iv)
C = iv + aes.encrypt(M)
print_cbc_dec(K, C)


