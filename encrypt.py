from cryptography.fernet import Fernet

# Load key
key = open("key.key", "rb").read()
cipher = Fernet(key)

# Read original file
with open("sample.txt", "rb") as f:
    data = f.read()

# Encrypt
encrypted = cipher.encrypt(data)

# Save encrypted file
with open("encrypted.enc", "wb") as f:
    f.write(encrypted)

print("File encrypted!")
