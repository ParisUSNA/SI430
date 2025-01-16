from socket import *

#set up socket
servePort = 8000
serveSock = socket(AF_INET, SOCK_STREAM)
serveSock.bind(('',servePort))
serveSock.listen(1)

#receive/send information over the socket
while True:
    connectSock, addr = serveSock.accept()
    try:
        request = connectSock.recv(1024).decode()
        filename = request.split()[1]
        output = open(filename[1:]).read()
        length = len(output.encode())
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {length}\r\n\r\n"
        connectSock.send(response.encode())
        connectSock.send(output.encode())
        connectSock.close()

    #if a requested file is not found
    except IOError:
        response2 = 'HTTP/1.1 404 ERROR\r\nContent-Type: text/html\r\nContent-Length: 1\r\n\r\n'
        connectSock.send(response2.encode())
        connectSock.close()

