import socket

socket.setdefaulttimeout(2)
s = socket.socket()

target = raw_input("Target Host: ")
port = 80

s.connect((target, port))
s.send('HEAD / HTTP/1.1\nHost: ' + target + '\n\n')
print s.recv(1024)
s.close()
