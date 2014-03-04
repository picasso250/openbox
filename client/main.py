import socket
import sys
import json

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

head = json.dumps({
    'cmd': 'upload',
    'name': 'test.txt'
})
length = len(head)
print(head)
print(length)

import struct
length = struct.pack('i', length)
print length


s.send(length)
s.send(head)
s.send('file content\n')
s.close()

