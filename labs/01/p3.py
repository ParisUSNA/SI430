def set_one_at(a, i):
    x = 128 >> i

    return a | x

def pr(a):
    print(f"dec: {a}")
    print(f"hex: 0x{a:02x}")
    print(f"bin: {a:08b}")

def set_zero_at(a, i):
    x = (128 >> i) ^ (255)
    return a & x

def zero_out_top(a, n):
    x = 255 >> n
    return a & x
