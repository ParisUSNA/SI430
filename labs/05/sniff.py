#!/usr/bin/python3
# raw.py

from socket import *
import struct
ETH_P_ALL = 0x0003
raw_socket = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL))

while(True):
    (data, addr) = raw_socket.recvfrom(1024)
    
    if data[12] == 0x08 and data[13] == 0:
        data1 = data[14:]
        if data1[9] == 17:
            dstm = struct.unpack("BBBBBB", data[:6])
            srcm = struct.unpack("BBBBBB", data[6:12])
            src = struct.unpack("BBBB", data1[12:16])
            dst = struct.unpack("BBBB", data1[16:20])
            pkt = data1[20:]
            (srcp,) = struct.unpack(">H", pkt[:2])
            (dstp,) = struct.unpack(">H", pkt[2:4])
            (length,) = struct.unpack(">H", pkt[4:6])
            if 9000 in [srcp, dstp]:
                msg = pkt[8:length]
                print(src, srcp, srcm)
                print(dst, dstp, dstm)
                print(msg)
                print()

