# 🔐 Secure File Transfer System

## 📌 Project Overview

This project implements a **Secure File Transfer System** using **Python**, ensuring safe communication over an insecure network. The system uses **AES encryption (Fernet)** and **TCP/IP socket programming** to protect data confidentiality and integrity during transmission.

---

## 🚀 Features

* 🔒 File Encryption using AES (Fernet)
* 🔑 Secure Key Generation
* 🌐 Client-Server Communication using Sockets
* 📁 Secure File Transfer over Network
* 🔓 Decryption at Receiver End
* ✔️ Data Integrity Verification

---

## 🛠️ Technologies Used

* Python
* Socket Programming
* Cryptography Library (Fernet - AES)
* TCP/IP Protocol

---

## 📂 Project Structure

```
secure-file-transfer-system/
│── key_generator.py   # Generates secret key
│── encrypt.py         # Encrypts file
│── client.py          # Sends encrypted file
│── server.py          # Receives file
│── decrypt.py         # Decrypts file
│── sample.txt         # Input file
│── encrypted.enc      # Encrypted file
│── decrypted.txt      # Output file
│── README.md
```

---

## ⚙️ How to Run the Project

### Step 1: Install Dependencies

```
pip install cryptography
```

### Step 2: Generate Key

```
python key_generator.py
```

### Step 3: Encrypt File

```
python encrypt.py
```

### Step 4: Start Server

```
python server.py
```

### Step 5: Run Client

```
python client.py
```

### Step 6: Decrypt File

```
python decrypt.py
```

---

## 🔄 Working Flow

1. User selects a file (sample.txt)
2. File is encrypted using AES key
3. Encrypted file is sent via socket
4. Server receives encrypted file
5. File is decrypted using same key
6. Original file is restored

---

## 🔐 Security Features

* **Confidentiality** – AES Encryption
* **Integrity** – Data remains unchanged
* **Authentication** – Shared secret key
* **Tamper-Proofing** – Encrypted transmission

---

## 📊 Example

* Original: `Bank Password: 12345`
* Encrypted: `gAAAAAB...`
* Decrypted: `Bank Password: 12345`

---

## 👩‍💻 Author

**Nitya Gupta**
Network Security Project – UPES (2025–2026)

---

## 📜 License

This project is developed for academic purposes only.
