import socket
server = socket.socket()
server.bind(("0.0.0.0", 9999))
server.listen(1)

print("Waiting for connection...")

conn, addr = server.accept()
print("Connected from:", addr)

data = conn.recv(1024 * 1024)

with open("received.enc", "wb") as f:
    f.write(data)

print("File received!")

conn.close()