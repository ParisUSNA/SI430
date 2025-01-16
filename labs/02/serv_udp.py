import socket
import sys

sock = socket(type=SOCK_DGRAM)
sock.bind(("0.0.0.0", 9000))



while(1):
    
