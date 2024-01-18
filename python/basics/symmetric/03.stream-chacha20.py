from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import base64

plaintext = b'HelloHelloHelloHelloHelloHello!!'

# Encryption
key = get_random_bytes(ChaCha20.key_size)
cipher = ChaCha20.new(key=key)
ciphertext = cipher.encrypt(plaintext)

print("Ciphertext:", ciphertext)

# Decryption
decipher = ChaCha20.new(key=key)
decrypted_plaintext = decipher.decrypt(ciphertext)

print("Decrypted plaintext:", decrypted_plaintext.decode("utf"))
