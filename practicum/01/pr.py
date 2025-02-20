import struct

def showpkts_ARP(data):
    
    ARPpkts = []

    while(data):
        destMac = data[:6]
        srcMac = data[6:12]
        (typ,) = struct.unpack(">H", data[12:14])

        if(typ == 0x0806):
            ARPpkts.append(((destMac, srcMac),data[14:14+42]))
        
            count = 0
            for i in range(14+42,len(data)):
                if(data[i] == 0):
                    count += 1
                else:
                    break

            data = data[14+42+count:]
        else:
            (length, ) = struct.unpack(">H", data[16:18])
            data = data[14+length:]
        


    for x, (dstsrc, i) in enumerate(ARPpkts):
        (hardtyp,) = struct.unpack(">H", i[:2])
        (prottyp,) = struct.unpack(">H", i[2:4])
        hwadd = i[4]
        pradd = i[5]
        (op,) = struct.unpack(">H", i[6:8])
        sendMAC = struct.unpack("BBBBBB", i[8:14])
        sendprot = struct.unpack("BBBB", i[14:18])
        tgtMAC = struct.unpack("BBBBBB", i[18:24])
        tgtprot = struct.unpack("BBBB", i[24:28])
        
        if(x != 0):
            print()

        print("===")
        print("Dst-MAC= ", end="")
        for x, i in enumerate(struct.unpack("BBBBBB", dstsrc[0])):
            if x != 0:
                print(":", end="")
            print(f"{i:02x}", end="")
        print()
        print("SRC-MAC= ", end="")
        for x, i in enumerate(struct.unpack("BBBBBB", dstsrc[1])):
            if x != 0:
                print(":", end="")
            print(f"{i:02x}", end="")
        print()
        print(f"Opcode= {op}")
        print("Sender-HW-Addr= ", end="")
        for x, i in enumerate(sendMAC):
            if x != 0:
                print(":", end="")
            print(f"{i:02x}", end="")
        print()
        print("Sender-Prot-Addr= ", end="")
        for x, i in enumerate(sendprot):
            if x != 0:
                print(".", end="")
            print(f"{i}", end="")
        print()
        print("Target-HW-Addr= ", end="")
        for x, i in enumerate(tgtMAC):
            if x != 0:
                print(":", end="")
            print(f"{i:02x}", end="")
        print()
        print("Target-Prot-Addr= ", end="")
        for x, i in enumerate(tgtprot):
            if x != 0:
                print(".", end="")
            print(f"{i}", end="")
        print()
        print("===")
