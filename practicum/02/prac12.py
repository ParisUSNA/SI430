from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad
from Cryptodome.Util.Padding import unpad
from Cryptodome.Util.strxor import strxor

def Finv(K, C):
    if type(K) != bytes:
        print("Error! The key must be a bytes object.")
        return b""
    elif type(C) != bytes:
        print("Error! The ciphertext must be a bytes object.")
        return b""
    elif(len(C) % 16):
        print("Error! The ciphertext must be 16 bytes long.")
        return b""
    elif len(K) % 16:
        print("Error! The key must be 16 bytes long.")
        return b""

    cipher = AES.new(K, AES.MODE_ECB)
    plain = cipher.decrypt(C)
    return plain


def print_cbc_dec(K, C):
    if type(K) != bytes:
        print("Error! The key must be a bytes object.")
        return b""
    elif type(C) != bytes:
        print("Error! The ciphertext must be a bytes object.")
        return b""
    elif(len(C) % 16):
        print("Error! The ciphertext must be 16 bytes long.")
        return b""
    elif len(K) % 16:
        print("Error! The key must be 16 bytes long.")
        return b""

    cipher = [ C[i*16:(i+1)*16] for i in range(len(C)//16)]
    iv = cipher[0]

    for i in range(1, len(cipher)):
        p = Finv(K, cipher[i])
        print(f"D{i} (hex): {p.hex()}")
        plain = strxor(p, cipher[i-1])
        print(f"M{i} (hex): {plain.hex()}")
        print(f"M{i}: {plain}")
        print()
