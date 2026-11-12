import socket
import threading
import datetime

HOST = '0.0.0.0'
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print("UDP Time Server Started")
print("Listening on Port", PORT)


def handle_client(addr):

    current_time = datetime.datetime.now()

    time_string = current_time.strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    server.sendto(time_string.encode(), addr)

    print("Time request served.")


while True:

    data, addr = server.recvfrom(1024)

    thread = threading.Thread(
        target=handle_client,
        args=(addr,)
    )

    thread.start()
