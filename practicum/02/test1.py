#!/usr/bin/python3
# test1.py
from prac12 import *

print("==== case 0 ====")
K = b"0123456789abcdef"
C = b'\xe5\xdb\x0c3Z~\x1c`\xde\xb1\xd2t\x02\xa7\xf0\xc0'
M = Finv(K, C)
print("M (hex):", M.hex())
print("M:", M)

print("==== case 1 ====")
K = b"0123456789abcdef"
C = b"aaaaaaaaaaaaaaaa"
M = Finv(K, C)
print("M (hex):", M.hex())
print("M:", M)


print("==== case 2 ====")
K = b"0123456789abcdef!"
C = b"aaaaaaaaaaaaaaaa"
M = Finv(K, C)
print("M (hex):", M.hex())
print("M:", M)

print("==== case 3 ====")
K = b"0123456789abcde"
C = b"aaaaaaaaaaaaaaaa"
M = Finv(K, C)
print("M (hex):", M.hex())
print("M:", M)


print("==== case 4 ====")
K = b"0123456789abcdef"
C = b"aaaaaaaaaaaaaaa"
M = Finv(K, C)
print("M (hex):", M.hex())
print("M:", M)

print("==== case 5 ====")
K = b"0123456789abcdef"
C = b"aaaaaaaaaaaaaaaab"
M = Finv(K, C)
print("M (hex):", M.hex())
print("M:", M)


print("==== case 6 ====")
K = "0123456789abcdef"
C = b"aaaaaaaaaaaaaaaab"
M = Finv(K, C)
print("M (hex):", M.hex())
print("M:", M)

print("==== case 7 ====")
K = b"0123456789abcdef"
C = "aaaaaaaaaaaaaaaab"
M = Finv(K, C)
print("M (hex):", M.hex())
print("M:", M)

