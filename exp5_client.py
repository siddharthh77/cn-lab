import socket
import random
import json

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

n = int(input("Enter order of matrix: "))

matrix = []

for i in range(n):
    row = []

    for j in range(n):
        row.append(random.randint(0, 50))

    matrix.append(row)

print("Generated Matrix:")

for row in matrix:
    print(row)

client.send(json.dumps(matrix).encode())

result = client.recv(1024).decode()

print("Matrix Type:", result)

client.close()
