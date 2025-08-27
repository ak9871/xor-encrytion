def xorCipher(text, key):
    return bytearray(value ^ key[(index % len(key))] for index, value in enumerate(text)) #Function that encrypts the text

# Encrypts the plaintext
def encrypt():
    key = input("Enter a key, ensure the key is something you can remember, treat it as a password\n").encode()
    plaintext = input("Enter the text you want to encrypt\n").encode()
    ciphertext = xorCipher(plaintext, key)
    print(f"Encrypted code: {ciphertext}\n")

# Decryptes the ciphertext
def decrypt():
    key = input("Enter your previous key\n").encode()
    ciphertext = input("Enter the encrypted text\n").encode()
    plaintext = xorCipher(ciphertext, key)
    print(f"Decrypted code: {plaintext}\n")

# Chooses whether the user wants to encrypt or decrypt
EncryptOrDecypt = input("Do you want to encrypt text, or decrypt text?\n")
if EncryptOrDecypt.lower() == "encrypt":
    encrypt()
elif EncryptOrDecypt.lower() == "decrypt":
    decrypt()
else:
    print("Invalid input")