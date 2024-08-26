from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

class PDCPSecurity:
    def __init__(self):
        self.key = os.urandom(16)  # Generate a random AES key (128 bits)
        self.iv = os.urandom(AES.block_size)  # Generate a random IV
        self.bearer = None
        self.direction = None
        self.count = 0

    def protect(self, data):
        """Encrypt data using AES encryption."""
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))
        return self.iv + encrypted_data  # Prepend IV for decryption

    def unprotect(self, encrypted_data):
        """Decrypt data using AES encryption."""
        iv = encrypted_data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)
        return decrypted_data

    def set_parameters(self, bearer, direction):
        """Set the security parameters."""
        self.bearer = bearer
        self.direction = direction

    def generate_key(self):
        """Regenerate the encryption key."""
        self.key = os.urandom(16)
        print("New encryption key generated.")
