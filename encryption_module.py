# encryption_module.py
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64

def pad(text):
    block_size = algorithms.AES.block_size // 8
    padding_size = block_size - (len(text) % block_size)
    return text + bytes([padding_size] * padding_size)

def encrypt_text(text, key, iv):
    text_bytes = pad(text.encode('utf-8'))
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')

    cipher = Cipher(algorithms.AES(key_bytes), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(text_bytes) + encryptor.finalize()

    # If using ECB mode, you can directly encode the ciphertext in base64
    encrypted_text = base64.b64encode(ciphertext).decode('utf-8')

    return encrypted_text


def decrypt_text(encrypted_text, key, iv):
    key_bytes = key.encode('utf-8')
    iv_bytes = iv.encode('utf-8')

    # Decode the base64 encoded ciphertext
    ciphertext = base64.b64decode(encrypted_text)

    cipher = Cipher(algorithms.AES(key_bytes), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    decrypted_text_bytes = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the decrypted text
    unpadder = padding.PKCS7(128).unpadder()
    decrypted_text = unpadder.update(decrypted_text_bytes) + unpadder.finalize()

    return decrypted_text.decode('utf-8')
