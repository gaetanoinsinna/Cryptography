import os
import string
from math import ceil

from Crypto.Cipher import AES

os.environ['PWNLIB_NOTERM'] = 'True'  # Configuration patch to allow pwntools to be run inside of an IDE
os.environ['PWNLIB_SILENT'] = 'True'

from pwn import *

from myconfig import HOST, PORT

if __name__ == '__main__':

    # message = """Here is the msg:{0} - and the sec:{1}""".format(input0, ecb_oracle_secret)
    # We have to understand the secret
    # |pre|pre|pre|pre|-|msg|msg|msg|msg|-|msg|msg|msg|{sec}|-|sec|sec|sec|sec|
    # comparing msg with the msg with the left shifted secret we understand char by char of the secret
    prefix = b'Here is the msg:'
    postfix = b' - and the sec:'
    print(len(prefix))
    print(len(postfix))

    #all the characters printable (256 available)
    for guess in string.printable:
        message = postfix + guess.encode()
        server = remote (HOST,PORT)
        server.send(message)
        ciphertext = server.recv(1024)
        server.close()
        if ciphertext[16:32] == ciphertext[32:48]:
            print("Found 1st char=" + guess)
            break

    secret = b''
    for i in range(AES.block_size):
        pad = (AES.block_size - i ) * b'A'
        for guess in string.printable:
            message = postfix + secret + guess.encode() + pad
            print(message)

            server = remote(HOST, PORT)
            server.send(message)
            ciphertext = server.recv(1024)
            server.close()

            if ciphertext[16:32] == ciphertext[48:64]:
                print("Found=" + guess)
                secret+= guess.encode()
                postfix = postfix[1:]
                break
    print(secret)