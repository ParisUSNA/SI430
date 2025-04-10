from math import gcd
from Cryptodome.Util.number import getPrime
from Cryptodome.Random.random import randrange
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Hash import *
from Cryptodome.Signature import *

def is_e_good(e, p, q):
    phi = (p-1) * (q-1)
    try:
        d = pow(e, -1, phi)
        return True
    except ValueError:
        return False

def compute_d(e, p, q):
    phi = (p-1) * (q-1)
    try:
        d = pow(e, -1, phi)
        return d
    except ValueError:
        return -1

def gen(bit_len):
    p = getPrime(bit_len//2)
    q = getPrime(bit_len//2)
    n = p*q

    e = randrange(1, n)
    # fill
    while(not is_e_good(e, p, q)):
        e = randrange(1, n)

    d = compute_d(e,p,q)

    pk = (n, e)
    sk = (n, d)
    return (pk, sk)

def enc(pk, m):
    n, e = pk
    return pow(m, e, n)

def dec(sk, c):
    n, d = sk
    return pow(c, d, n)

def enc_oaep(pk, m):
    key = RSA.construct(pk)
    cipher = PKCS1_OAEP.new(key)
    ct = cipher.encrypt(m)
    return ct

def dec_oaep(n, e, d, c):
    key = RSA.construct((n,e,d))
    cipher = PKCS1_OAEP.new(key)

    try:
        ct = cipher.decrypt(c)
        return ct
    except:
        print("OAEP: decryption error!")
        return b""

def verify(pk, b, s):
    x = SHA256.new(b)
    y = int(x.hexdigest(), 16)
    n, e = pk

    print("Hash of the data (bytes): ", x.digest())
    print("Hash of the data (number): ", y)

    z = pow(s, e, n)

    return y == z

def sign(sk, b):
    x = SHA256.new(b)
    y = int(x.hexdigest(), 16)
    n, d = sk
    return pow(y, d, n)
