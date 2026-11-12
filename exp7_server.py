import socket
import threading

HOST = '0.0.0.0'
PORT = 9000

clients = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((HOST, PORT))

server.listen(5)

print("Multi User Chat Server Started")
print("Port:", PORT)


def handle_client(conn, addr):

    name = conn.recv(1024).decode().strip()

    clients[conn] = name

    print(name, "Connected")

    while True:

        try:
            message = conn.recv(1024).decode()

            if not message:
                break

            full_message = name + " : " + message

            print(full_message)

            for client in list(clients):

                if client != conn:

                    client.send(full_message.encode())

        except:
            break

    print(name, "Disconnected")

    clients.pop(conn, None)

    conn.close()


while True:

    conn, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )

    thread.start()
