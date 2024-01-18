from Crypto.Cipher import Salsa20

key = b'deadbeefdeadbeef'
cipher = Salsa20.new(key)

ciphertext = cipher.encrypt(b'The first part to encrypt')
ciphertext += cipher.encrypt(b'The second part to encrypt')


nonce = cipher.nonce
print(nonce)

decipher = Salsa20.new(key,nonce)
plaintext = decipher.decrypt(ciphertext)
print(plaintext.decode("utf-8"))