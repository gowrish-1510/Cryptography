from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.hashes import SHA256

curve= ec.SECP256K1() ##curve used by Bitcoin
private_key= ec.generate_private_key(curve,default_backend())
public_key= private_key.public_key() ##deriving the public key from the private key


data= "Message to be signed".encode('utf-8')
signature= private_key.sign(data,ec.ECDSA(SHA256()))  ##signing message with private key

##verification
try:
    public_key.verify(signature,data,ec.ECDSA(SHA256()))
    print('Message is Authentic')
    print('public key length is:',public_key.key_size)
except(TypeError,ValueError):
    print('Message is tampered!')


