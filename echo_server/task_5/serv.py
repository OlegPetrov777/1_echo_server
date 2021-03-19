import socket

log = open("ServerLog.txt", "a")
log.write('Server starting...\n')
sock = socket.socket()
port=input("Type in the port: ")


if not ((0<=port<65536) and isinstance(port, int)):
	log.write('Wrong port id, the default one will be used (9080)\n')
	print('Wrong port id, the default one will be used (9080)\n')
	port=9080
sock.bind(('', int(port)))


while True:
	log.write('Listening to the port: ' + str(port) + "\n")
	sock.listen(1)
	conn, addr = sock.accept()
	log.write('Connected to ' + addr[0] + ' ' + str(addr[1]) + '\n')
	print('Connected to ' + addr[0] + ' ' + str(addr[1]))
	

	while True:
		msg = ''
		data = conn.recv(1024)

		if not data:
			break

		log.write('Accepting data...\n')
		msg += data.decode()
		log.write(msg + '\n')
		
		log.write('Sending data...\n')
		conn.send(data)
		print(msg)

	log.write('Closing connection...\n')
	conn.close()
	
log.close()