from Crypto.PublicKey import RSA
from Crypto import Random

mykey= RSA.generate(2048) ##generate keys with 2048 bits

with open("privatekey.pem","wb") as f:
    private_key= mykey.export_key(
     passphrase="Pass", ##password
     pkcs=8, ## pcks #8 :Private-Key Information Syntax Standard
    )
    f.write(private_key)

with open("publickey.pem","wb") as f:
    public_key=mykey.public_key().export_key()
    f.write(public_key)
