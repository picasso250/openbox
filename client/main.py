import socket
import sys

import json
import struct

def send(skt, header=None, content=b''):
    if header is not None:
        header = json.dumps(header)
        header = bytes(header, 'UTF-8')
        len_ = len(header)
    else:
        len_ = 0
    skt.send(struct.pack('i', len_))
    if len_ > 0:
        print (header)
        skt.send(header)
    if isinstance(content, str): # file name
        f=open (filename, "rb") # read binary
        l = f.read(1024)
        while len(l) > 0:
            skt.send(l)
            l = f.read(1024)
            # print(l)
        f.close()
    else:
        skt.send(content)
    skt.close()

# cmd table
# u upload --rs-- file name --rs-- file content
# d

def upload_file(filename):
    s = socket.socket()
    s.connect(("localhost",9999))
    f=open (filename, "rb") # read binary
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
    s.close()


s = socket.socket()
s.connect(("localhost",9999))

filename = 'test.mp4'
head = ({
    'cmd': 'upload',
    'name': filename
})
send(s, head, filename)
