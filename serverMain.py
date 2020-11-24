import socket
import time
import pyautogui
import os
import sys

#cd C:\Users\bultm\Documents\Code\Sockets




HOST = ""
PORT = 8080

addr = ("", 8080)  #ipv6 address all interfaces, port 8080
'''if socket.has_dualstack_ipv6():
    s = socket.create_server(addr, family=socket.AF_INET6, dualstack_ipv6=True)
    print(s.getsockname())
else:
    s = socket.create_server(addr)
    print(s.getsockname())
'''
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.bind(sa)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)


if __name__ == '__main__': 

    dataOld = ''
    

    with s:

        (clientConnection, clientAddress) = s.accept()

        with clientConnection:
            
            print("Accepted connection!")

            while True:

                data = clientConnection.recv(1024) #recieves bytes of data
                info = data.decode("utf-8")
                print(info)

                if not data: break
                
                time.sleep(.2)
