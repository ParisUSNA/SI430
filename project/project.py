# project.py
# name: Christopher Paris
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad
from Cryptodome.Util import Counter

# read in_plain_file, encrypt the data, and store the ciphertext in out_cipher_file
def encrypt_ecb(in_plain_file, out_cipher_file, key):
  # do something
  cipher = AES.new(key, AES.MODE_ECB)
  plain = open(in_plain_file, "rb").read()
  plain = pad(plain, 16)

  ciphertext = cipher.encrypt(plain)

  open(out_cipher_file, "wb").write(ciphertext)

# read in_cipher_file, decrypt the ciphertext, and store the plaintext in out_plain_file
def decrypt_ecb(in_cipher_file, out_plain_file, key):
  # do something
  cipher = AES.new(key, AES.MODE_ECB)
  ciphertext = open(in_cipher_file, "rb").read()
  
  plain = cipher.decrypt(ciphertext)
  plain = unpad(plain, 16)

  open(out_plain_file, "wb").write(plain)

# read normal_bmp_file and in_cipher_file, fix the header in the ciphertext and
# store the results in out_cipher_bmp_file
def fix_bmp_header(normal_bmp_file, in_cipher_file, out_cipher_bmp_file):
  # do something
  header = open(normal_bmp_file, "rb").read(54)
  data = open(in_cipher_file, "rb"). read()[54:]
  open(out_cipher_bmp_file, "wb").write(header + data)

# read in_plain_file, encrypt the data, and store the ciphertext in out_cipher_file
def encrypt_cbc(in_plain_file, out_cipher_file, key, iv = None):
  # do something
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plain = open(in_plain_file, "rb").read()
  plain = pad(plain, 16)

  ciphertext = cipher.encrypt(plain)

  open(out_cipher_file, "wb").write(ciphertext)

# read in_cipher_file, decrypt the ciphertext, and store the plaintext in out_plain_file
def decrypt_cbc(in_cipher_file, out_plain_file, key, iv = None):
  # do something
  cipher = AES.new(key, AES.MODE_CBC, iv)
  ciphertext = open(in_cipher_file, "rb").read()
  
  plain = cipher.decrypt(ciphertext)
  plain = unpad(plain, 16)

  open(out_plain_file, "wb").write(plain)

# read in_plain_file, encrypt the data, and store the ciphertext in out_cipher_file
def encrypt_ctr(in_plain_file, out_cipher_file, key, ctr=None):
  # do something
  cipher = AES.new(key, AES.MODE_CTR, nonce = ctr[:8], initial_value = ctr[8:])
  plain = open(in_plain_file, "rb").read()

  ciphertext = cipher.encrypt(plain)

  open(out_cipher_file, "wb").write(ciphertext)

# read in_cipher_file, decrypt the ciphertext, and store the plaintext in out_plain_file
def decrypt_ctr(in_cipher_file, out_plain_file, key, ctr=None):
  # do something
  cipher = AES.new(key, AES.MODE_CTR, nonce = ctr[:8], initial_value = ctr[8:])
  ciphertext = open(in_cipher_file, "rb").read()
  
  plain = cipher.decrypt(ciphertext)

  open(out_plain_file, "wb").write(plain)

#my own pad function
def pad2(A):
    length = 16 - (len(A) % 16)
    if length == 0:
        length = 16
    padding = length.to_bytes(1, byteorder = 'big')

    return A + padding * length

#my own unpad function
def unpad2(A):
    if(len(A)%16):
        print("padding error!")
        return

    padding = A[-1]
    length = 0
    if(padding <= 16):
        length = padding
    
    for i in range(length):
        if(A[-1] != padding):
            print("padding error!")
            return
        
        A = A[:-1]

    return A

def breakCTR(P, C, tgt):
    plain = b'known plaintext atk CTR\n'
    return plain 
