import socket


print('Server starting...')
sock = socket.socket()
port=input("Type in the port: ")


if not ((0<=port<65536) and isinstance(port, int)):
	print('Wrong port id, the default one will be used (9080)')
	port=9080


sock.bind(('', int(port)))


while True:
	print('Listening to the port...')
	sock.listen(1)
	conn, addr = sock.accept()
	print('Connected to ', addr)

	while True:
		msg = ''
		data = conn.recv(1024)

		if not data:
			break

		print('Accepting data...')
		msg += data.decode()
		
		print('Sending data...')
		conn.send(data)
		print(msg)

	print('Closing connection...')
	conn.close()