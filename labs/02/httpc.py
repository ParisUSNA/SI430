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

data = sock.recv(1024)
data = data.decode()
print(data)
