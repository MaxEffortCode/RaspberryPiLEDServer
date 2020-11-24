import socket
import sys
import time

HOST = "2601:446:8100:37c0::c573"    # The remote host
PORT = 8080              # The same port as used by the server
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        s = socket.socket(af, socktype, proto)
    except OSError as msg:
        s = None
        continue
    try:
        s.connect(sa)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)

with s:
    while True:
        info = input()
        msg = str.encode(info, "UTF-8")
        try:
            s.sendall(msg)#recieves bytes of data
        except ConnectionResetError as e:
            break
        '''
        info = sys.argv[n]
        if info not infoOld:
            infoOld = info
            s.sendall(bytes(infoOld))
            data = s.recv(1024)
            print('Received', repr(data))
        '''

        time.sleep(.5)
