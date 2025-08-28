#!/usr/bin/env python3
import os
import base64

def xorCipher(text, key):
    return bytearray(value ^ key[(index % len(key))] for index, value in enumerate(text)) #Function that encrypts the text

def encrypt():
    # Encrypts the plaintext
    key = input("Enter a key, ensure the key is something you can remember, treat it as a password\n").encode()
    plaintext = input("Enter the text you want to encrypt\n").encode()
    ciphertext = xorCipher(plaintext, key)
    encodedcipher = base64.b64encode(ciphertext).decode() # Converts to base 64 so readable
    print(f"Encrypted text: {encodedcipher}\n")

def decrypt():
    # Decryptes the ciphertext
    key = input("Enter your previous key\n").encode()
    ciphertext = input("Enter the encrypted text\n")
    decodedcipher = base64.b64decode(ciphertext)
    plaintext = xorCipher(decodedcipher, key)
    print(f"Decrypted text: {plaintext.decode()}\n")

# Chooses whether the user wants to encrypt or decrypt
EncryptOrDecypt = input("Do you want to encrypt text, or decrypt text?\n")
if EncryptOrDecypt.lower() == "encrypt":
    encrypt()
elif EncryptOrDecypt.lower() == "decrypt":
    decrypt()
else:
    print("Invalid input")

