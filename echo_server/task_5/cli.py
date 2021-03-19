import socket

sock = socket.socket()
sock.setblocking(1)
host=input("Type in the host: ")
port=input("Type in the port: ")


if not ((0<=port<65536) and isinstance(port, int)):
        print('Wrong port id, the default one will be used (9080)')
        port=9080

        
try:
	try:
		print("Connecting to server..")
		sock.connect((host, int(port)))

	except (TypeError, socket.gaierror):
		print("Wrong host! You'll be connected to localhost")
		sock.connect(('localhost', int(port)))

except socket.error:
	print('Connection to this port refused, redirecting to deafult port (9080)')
	sock.connect(('localhost', 9080))


msg = input("Type in the data: ")


while msg != "exit":
	print("Sending data...")
	sock.send(msg.encode())

	print("Accepting data...")
	data = sock.recv(1024)
	
	print(data.decode())
	msg = input()

print("Closing connection..")
sock.close()