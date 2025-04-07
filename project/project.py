# project.py
# name: Christopher Paris
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad
from Cryptodome.Util import Counter
from Cryptodome import Random

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
def encrypt_cbc(in_plain_file, out_cipher_file, key, iv):
  # do something
  cipher = AES.new(key, AES.MODE_CBC, iv)
  plain = open(in_plain_file, "rb").read()
  plain = pad(plain, 16)

  ciphertext = cipher.encrypt(plain)

  open(out_cipher_file, "wb").write(ciphertext)

# read in_cipher_file, decrypt the ciphertext, and store the plaintext in out_plain_file
def decrypt_cbc(in_cipher_file, out_plain_file, key, iv):
  # do something
  cipher = AES.new(key, AES.MODE_CBC, iv)
  ciphertext = open(in_cipher_file, "rb").read()
  
  plain = cipher.decrypt(ciphertext)
  plain = unpad(plain, 16)

  open(out_plain_file, "wb").write(plain)

# read in_plain_file, encrypt the data, and store the ciphertext in out_cipher_file
def encrypt_ctr(in_plain_file, out_cipher_file, key, ctr):
  # do something
  cipher = AES.new(key, AES.MODE_CTR, nonce = ctr[:8], initial_value = ctr[8:])
  plain = open(in_plain_file, "rb").read()

  ciphertext = cipher.encrypt(plain)

  open(out_cipher_file, "wb").write(ciphertext)

# read in_cipher_file, decrypt the ciphertext, and store the plaintext in out_plain_file
def decrypt_ctr(in_cipher_file, out_plain_file, key, ctr):
  # do something
  cipher = AES.new(key, AES.MODE_CTR, nonce = ctr[:8], initial_value = ctr[8:])
  ciphertext = open(in_cipher_file, "rb").read()
  
  plain = cipher.decrypt(ciphertext)

  open(out_plain_file, "wb").write(plain)

#my own pad function
def pad2(A, block_length=16):
    length = block_length - (len(A) % block_length)
    if length == 0:
        length = block_length
    padding = length.to_bytes(1, byteorder = 'big')

    return A + padding * length

#my own unpad function
def unpad2(A):
    padding = A[-1]
    length = int(padding)
    
    for i in range(length):
        if(A[-1] != padding):
            print("padding error!")
            return
        
        A = A[:-1]

    return A

def breakCTR(P, C, tgt):
    plain = b'known plaintext atk CTR\n'
    return plain


def errorProp():
    key = Random.get_random_bytes(16)
    iv = Random.get_random_bytes(16)
    ctr = Random.get_random_bytes(16)
    encrypt_ecb("pic_original.bmp", "pic_ecb.bin", key)
    encrypt_ctr("pic_original.bmp", "pic_ctr.bin", key, ctr)
    encrypt_cbc("pic_original.bmp", "pic_cbc.bin", key, iv)

    pic = bytearray(open("pic_ecb.bin", "rb").read())
    pic[70] = 0
    open("pic_ecb.bin", "wb").write(pic)

    pic = bytearray(open("pic_ctr.bin", "rb").read())
    pic[70] = 0
    open("pic_ctr.bin", "wb").write(pic)

    pic = bytearray(open("pic_cbc.bin", "rb").read())
    pic[70] = 0
    open("pic_cbc.bin", "wb").write(pic)

    decrypt_ecb("pic_ecb.bin", "pic_ecb.bmp", key)
    decrypt_ctr("pic_ctr.bin", "pic_ctr.bmp", key, ctr)
    decrypt_cbc("pic_cbc.bin", "pic_cbc.bmp", key, iv)
