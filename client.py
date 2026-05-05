import socket

client = socket.socket()
client.connect(("127.0.0.1", 9999))

with open("encrypted.enc", "rb") as f:
    data = f.read()

client.sendall(data)

print("File sent!")

client.close()
