from SocketServer import BaseRequestHandler, TCPServer

class EchoHandler(BaseRequestHandler):
	def handle(self):
		print("Got connection from",self.client_address)
		help(self.request)
		while True:
			msg = self.request.recv(8192)
			if not msg:
				break
			self.request.send(msg)

if __name__=='__main__':
	serv = TCPServer(('',20001),EchoHandler)
	serv.serve_forever()
