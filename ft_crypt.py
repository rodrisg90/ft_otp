from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import base64

def encrypt(date, key):
        date = pad(date.encode(),16)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return base64.b64encode(cipher.encrypt(date))

def decrypt(enc, key):
        enc = base64.b64decode(enc)
        cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        return unpad(cipher.decrypt(enc),16)
