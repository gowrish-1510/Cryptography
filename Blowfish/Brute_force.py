from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
from Blowfish_demo import encryption,decryption

with open("4_letter_words.txt","rb") as f:
    words= f.read().lower().split()

def Brute_Force(cipher_text):
    for text in words:
        try:
            decrpt_mssg= decryption(cipher_text,text)
            if(decrpt_mssg):
                return decrpt_mssg,text
            
        except(TypeError,ValueError):
            continue
    return None,None

### Demo of Brute force attack
key= "apex"  ## Creating a weak key of only 4 bytes
data= "Can you decrypt my message without my key?".encode('utf-8')
cipher_text= encryption(data,key.encode('utf-8'))

decrpt_mssg,brute_key= Brute_Force(cipher_text)
if(decrpt_mssg and brute_key):
    print('Message decrypted after Brute force is ',decrpt_mssg.decode('utf-8'))
    print('Key is',brute_key)

else:
    print('Key not found!')