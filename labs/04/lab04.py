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

    return((dest,src,typ,rest))

def printMAC(mac):
    out = ""
    for i,j in enumerate(mac):
        if(i == 5):
            out += f"{j:02x}"
        else:
            out += f"{j:02x}:"

    return out

def showpkts_IP(data):
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
        print(f"IHL= {ihlSplit(a[3])}")
        printIP(a[3])

def ihlSplit(data):

    ihl = data[0]
    ihl = ihl % 16
    return ihl

def printIP(data):
    (length, ) = struct.unpack(">H",data[2:4])
    source = data[12:16]
    dest = data[16:20]
    rest = data[20:length]

    print(f"Total Length= {length}")
    print(f"Src-IP= ", end="")
    printIPADDR(source)
    print("Dst-IP= ", end="")
    printIPADDR(dest)
    printData(rest)

def printIPADDR(addr):
    for i in addr[:3]:
        print(f"{i:d}",end=".")
    print(f"{addr[3]:d}")

def showpkts_TCP(data, src, dst):
    data = data[24:]
    
    IPPkts = []

    while(data):
        (length, ) = struct.unpack("I",data[8:12])
        data1 = data[16:16+length]
        (x,) = struct.unpack(">H", data1[12:14])
        if(x  == 0x0800):
            IPPkts.append(data1)
        data = data[16+length:]

    tcpPkts = []

    for i in IPPkts:
        data1 = i[14:]
#        (x,) = struct.unpack("B", data1[9])
        x = data1[9]
        if(x == 6):
            tcpPkts.append((data1[12:16], data1[16:20], data1[20:]))

    packets = []
    for i in tcpPkts:
        offset = 4 * (i[2][12] // 16)
        packets.append((i[0], i[2][:2], i[1], i[2][2:4], i[2][offset:]))

    for i in packets:
        if(i[0] == getIP(src) or i[0] == getIP(dst)):
            if(i[2] == getIP(src) or i[2] == getIP(dst)):
                if(i[4] != b""):
                    printPKT(i)
                
def getIP(ip):
    a = ip.split(".")
    a = list(map(int, a))
    x = struct.pack("BBBB", a[0],a[1],a[2],a[3])
    return x

def printPKT(i):
    src = struct.unpack("BBBB", i[0])
    src = ".".join(list(map(str,src)))
    (srcp,) = struct.unpack(">H", i[1])
    dst = struct.unpack("BBBB", i[2])
    dst = ".".join(list(map(str,dst)))
    (dstp,) = struct.unpack(">H", i[3])
    msg = i[4]

    print(f"{src}({srcp}) -> {dst}({dstp}) :")
    print(f"\t{msg}")
