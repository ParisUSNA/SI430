#!/usr/bin/python3
# bob.py

import socket
import sys
import select
from dh import *
from hashlib import *
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes

#==============================================
# UDP socket on port 9000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0",9000))

#==============================================
# global parameters
g = generator()
p = prime()
length = p.bit_length()//8 + 1    # length of p in bytes 

#==============================================
# recv msg A from Alice 
A, addrAlice = sock.recvfrom(1024)
A = int.from_bytes(A, 'big')  # bytes to int (big endian)

#==============================================
# send msg B from Alice 
(B, b) = sendB(g, p)
sock.sendto( B.to_bytes(length, 'big'), addrAlice) 

#==============================================
# compute the key K and compress it to 265 bits using sha256
K = keyB(g, p, B, b, A)
K = K.to_bytes(length, 'big')
H = sha256()
H.update(K)
K = H.digest()

#===============================================
# We uses AES-CBC
def enc(M):
  iv = get_random_bytes(16)
  aes = AES.new(K, AES.MODE_CBC, iv)
  C = aes.encrypt(pad(M, AES.block_size))
  return iv + C

def dec(C):
  iv = C[:16]
  aes = AES.new(K, AES.MODE_CBC, iv)
  return unpad(aes.decrypt(C[16:]), AES.block_size)

#================================================
# sock send/recv with the dedicated Alice
def send(C):
  sock.sendto(C, addrAlice)

def recv():
  while True:
    (C, addr) = sock.recvfrom(1024)
    if addr == addrAlice:
      return C


#================================================
# Receive the first encrypted message. 
# Alice always has to send an encrypted message of b"Hello"
C = recv()
M = dec(C)
print(M)
if M != b"Hello":
  send(b"Error!")
  exit(0)
  
#================================================
# Now, let's chat
while True:
  socklist = [sock, sys.stdin]  ## focus here!!!
  (r_sockets, w_sockets, e_sockets) = select.select(socklist, [], [])

  if sock in r_sockets:   # we have something to read from sock!
    C, sndaddr = sock.recvfrom(1024)
    M = dec(C).decode()
    if sndaddr == addrAlice:
      print("-->", M)
      if M == "quit": break 

  if sys.stdin in r_sockets:  # we have something to read from sys.stdin! 
    s = input()
    send(enc(s.encode()))
    if s == "quit": break

sock.close()
