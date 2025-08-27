def xor_encrypt_decrypt(input_bytes: bytes, key: bytes) -> bytes:
    """Encrypt or decrypt data using XOR with a repeating key."""
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(input_bytes)])


# Example usage
key = b"mysecretkey"

# Encrypt text
plaintext = b"hello world"
ciphertext = xor_encrypt_decrypt(plaintext, key)
print("Encrypted:", ciphertext)

# Decrypt (just run again with same key)
decrypted = xor_encrypt_decrypt(ciphertext, key)
print("Decrypted:", decrypted.decode())