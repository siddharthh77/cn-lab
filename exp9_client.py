import socket

HOST = '127.0.0.1'
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter File Name: ")

client.sendto(filename.encode(), (HOST, PORT))

data, addr = client.recvfrom(65535)

print("\nResponse Received From Server")

print(data.decode())

client.close()
