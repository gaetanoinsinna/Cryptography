from pwn import *
from math import ceil
from Crypto.Cipher import AES 

from attacks.ECB.myconfig import HOST,PORT

BLOCK_SIZE = AES.block_size
BLOCK_SIZE_HEX = 2*BLOCK_SIZE

server = remote(HOST,PORT)

start_str = "This is what I received: "

#We have a string of length len(start_str). We divide it for BLOCK_SIZE
#Assume start_str len = 17 and BLOCK_SIZE = 4
#ceil(17/4) = 5 * BLOCK_SIZE = 40 - 17 = 23 <= PADDING
pad_len = ceil(len(start_str)/BLOCK_SIZE)*BLOCK_SIZE - len(start_str)


#We send to the server a message composed by all 'A's of 2 block length + padding
# |x|x|x|A| |A|A|A|A| |A|A|A|x| <- at least 2 blocks + padding 
msg = b"A"*(2*AES.block_size+pad_len)

server.send(msg)

ciphertext = server.recv(1024)
ciphertext_hex = ciphertext.hex()
server.close()

# '//' is floor division 
for i in range(0,int(len(ciphertext_hex)//BLOCK_SIZE_HEX)):
    #the ':' means from -> to
    print(ciphertext_hex[i*BLOCK_SIZE_HEX:(i+1)*BLOCK_SIZE_HEX])

#if from the second block to the third is equal to third to fourth it's ECB
if ciphertext[2*BLOCK_SIZE:3*BLOCK_SIZE] == ciphertext[3*BLOCK_SIZE:4*BLOCK_SIZE]:
    print("ECB")
else: 
    print("CBC")

