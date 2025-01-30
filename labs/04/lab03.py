import struct

def showpkts(data):
    data = data[24:]

    packets = []

    while(data):
        (length, ) = struct.unpack("I",data[8:12])
        data1 = data[16:16+length]
        packets.append(data1)
        data = data[16+length:]

    for i in packets:
        printData(i)

def printData(data):
    print("data:")
    for i,j in enumerate(data):
        if(i%16 == 15):
            print(f"{j:02x}")
        elif(i%16 == 7):
            print(f"{j:02x}", end="  ")
        else:
            print(f"{j:02x}", end=" ")

    print("\n")

def showpkts_Eth(data):
    data = data[24:]

    packets = []

    while(data):
        (length, ) = struct.unpack("I",data[8:12])
        data1 = data[16:16+length]
        packets.append(data1)
        data = data[16+length:]

    for i in packets:
        a = dataDST(i)
        print(f"Dst-MAC= {printMAC(a[0])}")
        print(f"Src-MAC= {printMAC(a[1])}")
        print(f"Type= {a[2][0]:02x} {a[2][1]:02x}")
        printData(a[3])

def dataDST(data):
    dest = data[:6]
    src = data[6:12]
    typ = data[12:14]
    rest = data[14:]

    return((dest,src,typ, rest))

def printMAC(mac):
    out = ""
    for i,j in enumerate(mac):
        if(i == 5):
            out += f"{j:02x}"
        else:
            out += f"{j:02x}:"

    return out
