import socket
import time

socket.setdefaulttimeout(5)

s0 = socket.socket()

url = raw_input("Target URL: ")
port = int(raw_input("Target Port: "))
enumPorts = raw_input("Enumerate all ports? Y/N ")
samsClass = raw_input("Samsclass? Y/N ")
portKnock = raw_input("Port Knock? Y/N ")

if enumPorts == "Y":
	for x in range(1, 65535):
		s0.connect((url,x))
		print s0.recv(1024)
		s0.close()
elif samsClass == "Y": #not working
	num = 1000
	for x in range(1, 65):
		try:
			s0.connect((url, num))
			print s0.recv(1024)
			print num
			s0.close()
			num + 1000
		except Exception:
			pass
elif portKnock == "Y":
	s1 = socket.socket()
	s2 = socket.socket()
	s0.connect((url, 3100))
	s0.close()
	portList = (3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900)
	for x in portList:
		try:
			s1.connect((url, x))
			s1.close()
			time.sleep(2)
			print x
		except Exception:
			pass
		try:
			s2.connect((url, 3003))
			print s0.recv(1024)
			print x
			s2.close()
		except Exception:
			pass
else:
	s0.connect((url, port)) 
	print s0.recv(1024)
	s0.close()

