from SocketServer import TCPServer, StreamRequestHandler
class Handler(StreamRequestHandler):
	def handle(self):
		addr = self.request.getpeername()
		print 'got connection from',addr
		self.wfile.write('connection')

server = TCPServer(('',9000),Handler)
server.serve_forever()
