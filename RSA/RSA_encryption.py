from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

data="My name is John Doe from XYZ university".encode('utf-8')

with open("publickey.pem","rb") as f:
    pub_key= RSA.import_key(f.read())

cipher= PKCS1_OAEP.new(key= pub_key) ##generating cipher from public key
cipher_text= cipher.encrypt(data)

with open("cipher.bin","wb") as f:
    f.write(cipher_text)
