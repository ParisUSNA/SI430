def set_one_at(a, i):
    x = 0b1 << i - 1

    return a | x

def pr(a):
    print(f"dec: {a}")
    print(f"hex: 0x{a:02x}")
    print(f"bin: {a:08b}")

def set_zero_at(a, i):
    x = (1 << i - 1) ^ (255)
    return a & x

def zero_out_top(a, n):
    x = 255 >> n
    return a & x
