import socket


print('Server starting...')
sock = socket.socket()
sock.bind(('', 9091))


while True:
	print('Listening to the port...')
	sock.listen(1)
	conn, addr = sock.accept()
	print('Connceted to ', addr)

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