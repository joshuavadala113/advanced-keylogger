from cryptography.fernet import Fernet
import config

def encrypt_log(path):
    key = config.ENCRYPTION_KEY
    f = Fernet(key)
    with open(path, 'rb') as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(path, 'wb') as file:
        file.write(encrypted_data)
