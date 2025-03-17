# project.py
# name: Christopher Paris
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad

# read in_plain_file, encrypt the data, and store the ciphertext in out_cipher_file
def encrypt_ecb(in_plain_file, out_cipher_file, key):
  # do something

# read in_cipher_file, decrypt the ciphertext, and store the plaintext in out_plain_file
def decrypt_ecb(in_cipher_file, out_plain_file, key):
  # do something

# read normal_bmp_file and in_cipher_file, fix the header in the ciphertext and
# store the results in out_cipher_bmp_file
def fix_bmp_header(normal_bmp_file, in_cipher_file, out_cipher_bmp_file):
  # do something
