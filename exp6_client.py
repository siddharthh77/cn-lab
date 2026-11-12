import socket

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sentence = input("Enter sentence: ")

client.sendto(sentence.encode(), (HOST, PORT))

data, addr = client.recvfrom(1024)

print("Translated Sentence:")
print(data.decode())

client.close()
