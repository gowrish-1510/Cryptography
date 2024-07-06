from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("privatekey.pem","rb") as f:
    pvt_key= RSA.import_key(
        extern_key= f.read(),
        passphrase= "Pass"
    )

decrypted= PKCS1_OAEP.new(pvt_key)

with open("cipher.bin","rb") as f:
    decrpt_mssg= decrypted.decrypt(f.read())

print("Decrypted message using Private key is :",decrpt_mssg)