from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

mymessage= "I have signed this message".encode('utf-8')

with open('privatekey.pem',"rb") as f:
    pvt_key= RSA.import_key(
        extern_key= f.read(),
        passphrase= "Pass",
    )

sha_message= SHA256.new(mymessage)
signing_key= pkcs1_15.new(pvt_key)

signed_message= signing_key.sign(sha_message) ##Signing of SHA-256 encrypted message with private key of sender
##Here the same private key is used as the receiver's(privatekey.pem) just for simplicity

## verifying the signature using public key of sender
with open('publickey.pem','rb') as f:
    pub_key= RSA.import_key(f.read())

try:
    pkcs1_15.new(pub_key).verify(sha_message,signature= signed_message) ##verify signature
    print('Signature is Valid:')
except(ValueError,TypeError):
    print("Signature is not valid:")

## Demo of Man in the middle
modified_message= "I have not signed  this message".encode('utf-8') ##message is modified by third party
sha_modified= SHA256.new(modified_message)

attacker_key= RSA.generate(2048)
attacker_pvt_key= attacker_key.export_key()
false_sign= pkcs1_15.new(attacker_key) ##attacker attempting to create a false signature with his private key

attacker_sign= false_sign.sign(sha_modified) ##signed message ready to be sent to receiver

try:
    pkcs1_15.new(pub_key).verify(sha_modified,attacker_sign)  ##verifying authenticity
    print("Message is Authentic")
except(TypeError,ValueError):
    print("Authenticity is Compromised!")
