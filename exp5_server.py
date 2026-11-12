import socket
import json

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(1)

print("Server waiting...")

conn, addr = server.accept()
print("Connected:", addr)

data = conn.recv(4096).decode()
matrix = json.loads(data)

n = len(matrix)

upper = True
lower = True
diagonal = True

for i in range(n):
    for j in range(n):

        if i > j and matrix[i][j] != 0:
            upper = False

        if i < j and matrix[i][j] != 0:
            lower = False

        if i != j and matrix[i][j] != 0:
            diagonal = False

if diagonal:
    result = "Diagonal Matrix"

elif upper:
    result = "Upper Triangular Matrix"

elif lower:
    result = "Lower Triangular Matrix"

else:
    result = "Not a special matrix"

conn.send(result.encode())

print("Matrix Type:", result)

conn.close()
server.close()
