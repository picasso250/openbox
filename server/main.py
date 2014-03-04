import socket
import sys
s = socket.socket()
s.bind(("localhost",9999))
s.listen(10) # Acepta hasta 10 conexiones entrantes.

while True:
    sc, address = s.accept()

    print address
    f = open('file_'+".txt",'wb') #open in binary
    l = sc.recv(1024)
    print('.')
    while (l):
            f.write(l)
            l = sc.recv(1024)
    f.close()

    sc.close()

s.close()
