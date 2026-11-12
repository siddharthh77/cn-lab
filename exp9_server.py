import socket
import threading
import os

HOST = '0.0.0.0'
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print("UDP Concurrent File Server Started")
print("Listening on Port", PORT)


def handle_request(filename, addr):

    pid = os.getpid()

    if os.path.isfile(filename):

        with open(filename, 'r') as file:

            content = file.read()

        response = (
            f"Handled by Server PID: {pid}\n\n"
            + content
        )

    else:

        response = (
            f"Handled by Server PID: {pid}\n\n"
            "Requested File Not Found."
        )

    server.sendto(response.encode(), addr)

    print("Request for", filename, "served by PID", pid)


while True:

    data, addr = server.recvfrom(1024)

    filename = data.decode().strip()

    thread = threading.Thread(
        target=handle_request,
        args=(filename, addr)
    )

    thread.start()
