import socket
import datetime


def save_log(text):
	log = open("logs.txt", "a")  # запись логов 
	
	now = datetime.datetime.now()  # текущее время 
	log.write('<<' + str(now) + '>> ' + text + '\n')
	
	log.close()


""" СТАРТ СЕРВЕРА """
sock = socket.socket()
print('Server is starting.')
save_log('Server is starting.')


port = input('Enter port: ')  # вводим порт
sock.bind(('', int(port)))


while True:

	""" ПРОСЛУШКА ПОРТА """
	sock.listen(1)
	print(f"Listening to the port ({port})")
	save_log(f"Listening to the port ({port})")


	""" НОВЫЙ СОКЕТ И АДРЕС КЛИЕНТА """
	try:
	    conn, addr = sock.accept()
	except KeyboardInterrupt as k:
		print(f"ERROR: {k}")
		save_log(f"ERROR: {k}")
		exit()

	print(f"Connected to {addr}")
	save_log(f"Connected to {addr[0]}:{addr[1]}")

	print()

	while True:

		""" ПОЛУЧЕНИЕ СООБЩЕНИЯ ОТ КЛИЕНТА """
		try:
			data = conn.recv(1024).decode("utf8")

		except ConnectionResetError as e:
			print(f"ERROR: {e}")
			save_log(f"ERROR: {e}")
			exit()

		except KeyboardInterrupt as k:
			print(f"ERROR: {k}")
			save_log(f"ERROR: {k}")
			exit()


		# """ ВЫХОД КЛИЕНТА """
		if data == "" or data == "exit":
			print(f"Client disconnected.")
			save_log(f"Client disconnected.")
			break

		elif data == "stop":
			break

		print(f"Accepting data: {data}")
		save_log(f"Accepting data: {data}")


		# """ ОБРАТНАЯ ОТПРАВКА СООБЩЕНИЯ """
		data += '!!!'
		conn.send(data.encode())
		print(f"Sending data: {data}")
		save_log(f"Sending data: {data}")

	if data == "stop":
		break

print('Closing connection.')
save_log('Closing connection.')
conn.close()
