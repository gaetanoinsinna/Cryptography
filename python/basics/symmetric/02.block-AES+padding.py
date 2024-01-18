from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from Crypto.Util.Padding import pad, unpad
import base64

print("AES key size are:", AES.key_size)

key = get_random_bytes(AES.key_size[2])
iv = get_random_bytes(AES.block_size)

print ("KEY:", key)
print("IV:", iv)

# ALINED WITHOUT PADDING
data = b"These data are to be encrypted!!"
print(len(data),"-> these are aligned")

enc = AES.new(key,AES.MODE_CBC,iv)
encrypted_data = enc.encrypt(data)
print(encrypted_data)

dec = AES.new(key,AES.MODE_CBC,iv)
decrypted_data = dec.decrypt(encrypted_data)
print(decrypted_data)

# TO BE ALIGNED

data = b'Not aligned'
print(len(data))
enc = AES.new(key,AES.MODE_CBC,iv)
padded_data = pad(data,AES.block_size)
encrypted_data = enc.encrypt(padded_data)

print(base64.b64encode(encrypted_data).decode())

dec = AES.new(key,AES.MODE_CBC,iv)
decrypted_data = dec.decrypt(encrypted_data)
padded_decrypted = unpad(decrypted_data,AES.block_size)
print(padded_decrypted)
assert(padded_decrypted==data)

