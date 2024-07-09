from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad

key= get_random_bytes(16) ##Always choose a long key for Blowfish
data= "Message for encryption".encode('utf-8')

##Encryption
def encryption(data,key):
    cipher= Blowfish.new(key,Blowfish.MODE_CBC)
    padded_data= pad(data,Blowfish.block_size)
    encrypted_data= cipher.encrypt(padded_data)

    cipher_text= cipher.iv + encrypted_data ##helps to randomize encryption process
   ## print(len(cipher.iv)) ##get length of iv
    return cipher_text

##Decryption
def decryption(cipher_text,key):
    iv = cipher_text[:8]
    cipher = cipher_text[8:]

    # Create Blowfish cipher
    decry_cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)

    # Decrypt and unpad data
    padded_data = decry_cipher.decrypt(cipher)
    data = unpad(padded_data, Blowfish.block_size)

    return data

cipher_text= encryption(data,key)
## print('cipher text is ',cipher_text)
decrypt_mssg= decryption(cipher_text,key)
print('Decrypted message is ',decrypt_mssg)


