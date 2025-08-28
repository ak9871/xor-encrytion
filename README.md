# XOR Encryption CLI Tool

A command-line utility for encrypting and decrypting text using XOR-based encryption. 
This tool allows you to securely encode and decode messages with a key of your choice.

---

## Features
- Encrypt text with a custom key
- Decrypt previously encrypted text
- Simple, fast, and portable
- Packaged as a `.deb` for easy installation on Linux

## Installation

### Using the .deb package
1. Download from .deb GitHub Releases
2. To download, in terminal run sudo dpkg -i xor-encryptor.deb 
3. Enter encryptor into the terminal to start the program

### Not using the .deb package
1. Clone your repository with: git clone https://github.com/ak.9871/xor-encryptor.git
2. Navigate into the repository folder: cd xor-encryptor
3. Make the Python script executable: chmod +x xor-encryption.py
4. (Optional) Move it to a directory in your system PATH so you can run it from anywhere: sudo cp xor-encryption.py /usr/local/bin/encryptor
5. Run the tool (encryptor in shell if you did step 4./xor-           encryption.py from repo folder if not) 
   
## Uninstallation
To delete, use sudo dpkg -r xor-encryptor

## How to use
1. Initialise the program
2. Choose whether you want to encrypt / decrypt
3. Enter text you want to encrypt / decrypt
4. Enter your key
5. Copy the encrypted text and use as necessary, REMEMBER THE KEY IF YOU WANT TO DECRYPT
