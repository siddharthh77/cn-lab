import socket

HOST = '127.0.0.1'
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "TIME"

client.sendto(message.encode(), (HOST, PORT))

data, addr = client.recvfrom(1024)

print("\nCurrent Server Time")

print(data.decode())

client.close()
