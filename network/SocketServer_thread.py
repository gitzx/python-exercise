#-*- encoding: utf-8 -*-  
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler
class Server(ThreadingMixIn,TCPServer):pass
class Handler(StreamRequestHandler):
	def handler(self):
		addr = self.request.getpeername()
		print 'got connection from',addr
		self.wfile.write('connection')
	
server = Server(('',5000),Handler)
server.serve_forever()

#使用了线程处理的服务器
