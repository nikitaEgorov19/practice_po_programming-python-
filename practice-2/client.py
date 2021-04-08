import socket


def input_check(sending=''):
    a = input(sending)
    if a == '/stop' or a == '/exit':
        exit()

    return a


while True:
    while True:
        host = input_check("Name host: ")
        try:
            port = int(input_check(f"Введите порт для {host}: "))
        except ValueError:
            print("ERROR! Try again!")
            continue

        try:
            sock = socket.socket()
            sock.setblocking(True)
            sock.connect((host, port))
            print(f"Подключение к {host}:{port} успех!\n")
            break
        except (socket.gaierror, ConnectionRefusedError) as e:
            print(f"НЕ успех подключиться к {host}:{port} ({e})!")

    while True:
        try:
            data = sock.recv(1024)
            print(data.decode())

            msg = input_check("=>")

            if msg == '':
                msg = 'None'

            if msg == '/close':
                print(f"Отключение от {host}:{port}\n")
                sock.shutdown(0)
                break
            sock.send(msg.encode())
        except (ConnectionRefusedError, ConnectionAbortedError, ConnectionResetError) as e:
            print(e)
            break

    sock.close()