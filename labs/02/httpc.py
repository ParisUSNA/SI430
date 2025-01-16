from socket import *
import sys

dest = sys.argv[1]

sock = socket()
sock.settimeout(1000)
try:
    sock.connect((dest, 80))
except TimeoutError:
    sock.close()
    quit()

payload = f"GET / HTTP/1.1\r\nHost: {dest}\r\nAccept:*/*\r\n\r\n"
sock.send(payload.encode())

length = 0
data = sock.recv(1024)
data = data.decode()
print(data)
split = data.split("\r\n")
for i in split:
    temp = i.split(":")
    if temp[0] == "Content-Length":
        length = int(temp[1].strip())

content = sock.recv(length)
print(content.decode())
