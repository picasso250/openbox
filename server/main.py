import socket
import sys

import struct
import json

def recv(sc):
    length = sc.recv(4)
    length = struct.unpack('i', length)
    if length[0] > 0:
        head = sc.recv(length[0]).decode('UTF-8')
        head = json.loads(head)
    else:
        head = None
    print ('recv header ', head)
    
    return head

s = socket.socket()
s.bind(("localhost",9999))
s.listen(10) # Acepta hasta 10 conexiones entrantes.

while True:
    sc, address = s.accept()

    head = recv(sc)
    if head is not None:
        # upload
        f = open(head['name'],'wb') #open in binary
        while True:
            c = sc.recv(4096)
            if len(c) == 0:
                break
            f.write(c)
        sc.close()
        f.close()

s.close()
