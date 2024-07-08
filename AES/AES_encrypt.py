from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256, HMAC
from Crypto.Protocol.KDF import PBKDF2

message= "Hey there What's up?!".encode('utf-8')
mysalt= get_random_bytes(16) ##generating a 16-byte random salt

key= PBKDF2("mypass",salt= mysalt, dkLen=16) ##generating a key of 16-bytes
cipher= AES.new(key,AES.MODE_CTR) ##CTR mode involves XOR operation of key with data

cipher_text= cipher.encrypt(message)
hmac= HMAC.new(key,digestmod= SHA256) ##for verifying integrity of message in future
hmac.update(cipher_text)
hmac_tag= hmac.digest() ##return binary encrypted form of the MAC tag

with open('encrypted.bin',"wb") as f:
    f.write(mysalt)
    f.write(cipher.nonce)  # Write the nonce used in AES CTR mode
    f.write(hmac_tag)
    f.write(cipher_text)

with open("key.bin","wb") as f:
    f.write(key)