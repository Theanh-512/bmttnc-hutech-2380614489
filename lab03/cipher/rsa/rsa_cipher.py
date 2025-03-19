import base64
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os

class RSACipher:
    def __init__(self):
        self.private_key_path = "private.pem"
        self.public_key_path = "public.pem"

    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        with open(self.private_key_path, "wb") as priv_file:
            priv_file.write(private_key)
        with open(self.public_key_path, "wb") as pub_file:
            pub_file.write(public_key)

    def load_keys(self):
        if not os.path.exists(self.private_key_path) or not os.path.exists(self.public_key_path):
            self.generate_keys()
        with open(self.private_key_path, "rb") as priv_file:
            private_key = RSA.import_key(priv_file.read())
        with open(self.public_key_path, "rb") as pub_file:
            public_key = RSA.import_key(pub_file.read())
        return private_key, public_key

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        encrypted_bytes = cipher.encrypt(message.encode())
        return base64.b64encode(encrypted_bytes).decode()

    def decrypt(self, ciphertext_base64, key):
        cipher = PKCS1_OAEP.new(key)
        encrypted_bytes = base64.b64decode(ciphertext_base64)
        decrypted_bytes = cipher.decrypt(encrypted_bytes)
        return decrypted_bytes.decode()

    def sign(self, message, private_key):
        h = SHA256.new(message.encode())
        signature = pkcs1_15.new(private_key).sign(h)
        return base64.b64encode(signature).decode()

    def verify(self, message, signature_base64, public_key):
        h = SHA256.new(message.encode())
        signature = base64.b64decode(signature_base64)
        try:
            pkcs1_15.new(public_key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False
