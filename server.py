#!/usr/local/bin/python3

# filename: server.py

import socket
import sys

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

serversocket.bind((host, port))

serversocket.listen(5)

while True:
	clientsocket, addr = serversocket.accept()

	print('url: %s' % str(addr))
	msg = 'this is response message'
	clientsocket.send(msg.encode('utf-8'))
	clientsocket.close()