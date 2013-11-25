#-*- encoding: utf-8 -*-  
from SocketServer import TCPServer,ForkingMixIn,StreamRequestHandler
class Server(ForkingMixIn,TCPServer):pass
class Handler(StreamRequestHandler):
	def handler(self):
		addr = self.request.getpeername()
		print 'got connection from',addr
		self.wfile.write('connection')

server = Server(('',9000),Handler)
server.serve_forever()

#使用分叉技术（fork）的服务器
