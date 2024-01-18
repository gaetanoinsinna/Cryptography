from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes

if __name__ == '__main__':
    key_size = AES.key_size[2]
    key = get_random_bytes(key_size)
    print(key)