#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By Lynae Woody

# Cryptography libraries
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

#Building the key
key = os.urandom(32) #A 256-bit AES key
print("Generated AES Key: ", key)
iv = os.urandom(16) #A 128-bit initialization vector

#Encrypting the message
plaintext = input("Enter a plaintext message: ")
#It requires 16 bytes
padder = padding.PKCS7(128).padder()
padded_data = padder.update(plaintext.encode()) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

#Encrypted message
print("Ciphertext: ", ciphertext.hex())

#Decrypting the message

decryptor = cipher.decryptor()
decrypted_packets = decryptor.update(ciphertext) + decryptor.finalize()

#Unpad the decrypted packets
unpadder = padding.PKCS7(128).unpadder()
unpadded_data = unpadder.update(decrypted_packets) + unpadder.finalize()

print("Decrypted: ", unpadded_data.decode())

