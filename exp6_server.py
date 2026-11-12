import socket

HOST = '127.0.0.1'
PORT = 12345

dictionary = {
    "tbh": "to be honest",
    "ig": "I guess",
    "tbf": "to be fair",
    "atm": "at the moment",
    "irl": "in real life",
    "lol": "laughing out loud",
    "asap": "as soon as possible",
    "omg": "oh my God",
    "ttyl": "talk to you later",
    "idk": "I don't know",
    "nvm": "never mind",
    "idc": "I don't care"
}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print("UDP Server running...")

while True:

    data, addr = server.recvfrom(1024)

    sentence = data.decode()

    print("Received:", sentence)

    words = sentence.split()

    translated = []

    for word in words:

        translated.append(dictionary.get(word, word))

    result = " ".join(translated)

    server.sendto(result.encode(), addr)
