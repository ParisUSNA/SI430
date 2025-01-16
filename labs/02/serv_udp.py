from socket import *
import sys
import select

sock = socket(type=SOCK_DGRAM)
sock.bind(("0.0.0.0", 9000))

addr = ""

while True:
    socklist = [sock, sys.stdin]
    (r_sockets, w_sockets, e_sockets) = select.select(socklist, [], [])

    if e_sockets:
        break

    if sock in r_sockets:
        (data, addr) = sock.recvfrom(1024)
        if not data:
            break
        if data.decode().strip() == "quit":
            break
        print(f"From {addr} : {data}")

    if sys.stdin in r_sockets:
        s = sys.stdin.readline()
        if s.strip() == "quit":
            s = "^C"
            sock.sendto(s.encode(), addr)
            break
        else:
            sock.sendto(s.encode(), addr)
        

sock.close()
