import hashlib

def hmac():
    key = input("key: ").encode("utf-8")
    plaintext = input("plaintext: ").encode("utf-8")

    ipad = b'0x36' * 64
    opad = b'0x5c' * 64

    key += b'0x00' * (64 - len(key))
    i_key_pad = bytes(a ^ b for a,b in zip(key, ipad))
    print(i_key_pad)
    H1 = hashlib.sha256()
    H1.update(i_key_pad + plaintext )
    
    o_key_pad = bytes(a ^ b for a,b in zip(key, opad))
    print(o_key_pad)
    H2 = hashlib.sha256()
    H2.update(o_key_pad + H1.digest())

    print(H2.hexdigest())
