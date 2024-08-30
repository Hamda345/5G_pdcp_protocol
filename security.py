import logging
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

class PDCPSecurity:
    def __init__(self):
        self.key = os.urandom(16)  # Generate a random AES key (128 bits)
        self.bearer = None
        self.direction = None
        self.count = 0
        logging.info("PDCPSecurity initialized with a random AES key.")

    def protect(self, data):
        """Encrypt data using AES encryption."""
        iv = os.urandom(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_data = cipher.encrypt(pad(data, AES.block_size))
        logging.debug(f"Data encrypted. IV: {iv.hex()}, Encrypted Data: {encrypted_data.hex()}.")
        return iv + encrypted_data

    def unprotect(self, encrypted_data):
        """Decrypt data using AES encryption."""
        iv = encrypted_data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data[AES.block_size:]), AES.block_size)
        logging.debug(f"Data decrypted. IV: {iv.hex()}, Decrypted Data: {decrypted_data.hex()}.")
        return decrypted_data

    def set_parameters(self, bearer, direction):
        """Set the security parameters."""
        self.bearer = bearer
        self.direction = direction
        logging.debug(f"Security parameters set. Bearer: {bearer}, Direction: {direction}.")

    def generate_key(self):
        """Regenerate the encryption key."""
        self.key = os.urandom(16)
        logging.info("New encryption key generated.")
