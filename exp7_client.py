import socket
import threading

HOST = '127.0.0.1'
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

name = input("Enter your name: ")

client.send(name.encode())


def receive_messages():

    while True:

        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print("\n" + message)

        except:
            break


thread = threading.Thread(target=receive_messages)

thread.daemon = True

thread.start()

print("Connected to Chat Server")
print("Start chatting...")

while True:

    message = input()

    if message.lower() == "exit":
        break

    client.send(message.encode())

client.close()
