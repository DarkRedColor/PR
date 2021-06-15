import socket
import threading
import sys
import time

class Server:

	sucket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connections = []

	def __init__(self):
		self.sucket.bind(('0.0.0.0', 10000))
		self.sucket.listen(1)

	def handler(self, c, a):
		while True:
			data = None
			data = c.recv(1024)
			for connection in self.connections:
				connection.send(data)
			if not data:
				print(str(a[0]) + ':' + str(a[1]), "disconnected")
				self.connections.remove(c)
				c.close()
				break

	def get_ip(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			# doesn't even have to be reachable
			s.connect(('10.255.255.255', 1))
			IP = s.getsockname()[0]
		except Exception:
			IP = '127.0.0.1'
		finally:
			s.close()
		return IP

	def run(self):
		local_ip = self.get_ip()
		print(f'Chat-server running on {local_ip}')
		while True:
			c, a = self.sucket.accept()
			cThread = threading.Thread(target=self.handler, args=(c, a))
			cThread.daemon = True
			cThread.start()
			self.connections.append(c)
			print(str(a[0]) + ':' + str(a[1]), "connected")

server = Server()
server.run()
