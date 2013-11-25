import socket,sys
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9000
s.connect((host,port))
s.send("test socket")
print s.getpeername()
while 1:
	data = s.recv(2048)
	if not len(data):
		break
	print data
s.close()
