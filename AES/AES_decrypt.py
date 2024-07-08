import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256, HMAC
from Crypto.Protocol.KDF import PBKDF2

with open("encrypted.bin","rb") as f:
    salt= f.read(16)
    nonce= f.read(8)
    hmac_tag= f.read(32)
    cipher_text= f.read()

with open("key.bin","rb") as f:
    key= f.read()

mykey= PBKDF2("mypass",salt,dkLen=16)
print(mykey==key)  ##check the key generated using nonce is correct or not

# Check if the generated key matches the stored key
if mykey != key:
    print('Key is tampered')
    sys.exit(1)

# Create HMAC object and update with the cipher text
hmac = HMAC.new(mykey, digestmod=SHA256)
hmac.update(cipher_text) ##Creating MAC tag for verification

##check for man in middle attack
try:
    hmac.verify(hmac_tag) ##verifying authenticity using the imported hmac tag and created one
    print('Message is authentic!')
except(TypeError,ValueError):
    print('Warning! Message is tampered')
    sys.exit(1)

cipher= AES.new(mykey,AES.MODE_CTR,nonce=nonce)
decrypted_mssg= cipher.decrypt(cipher_text)
print('Decrypted message is ',decrypted_mssg.decode('utf-8'))


