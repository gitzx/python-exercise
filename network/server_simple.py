import socket,sys
host = ''
port = 9000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(1)
while 1:
	clientsock, clientaddr = s.accept()
	data = clientsock.recv(2048)  #socket object
	if not len(data):
		break
	print data
	clientsock.send(data)
	print s.getsockname()
	clientsock.close()
s.close()


