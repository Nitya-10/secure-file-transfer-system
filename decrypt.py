from cryptography.fernet import Fernet

key = open("key.key", "rb").read()
cipher = Fernet(key)

with open("received.enc", "rb") as f:
    encrypted_data = f.read()

decrypted = cipher.decrypt(encrypted_data)

with open("decrypted.txt", "wb") as f:
    f.write(decrypted)

print("File decrypted!")