from arc4 import ARC4
import base64

secret = '****'

def encrypt(password):
    # type:(str)->str
    arc4 = ARC4(secret.encode())
    encyptBytes = arc4.encrypt(password.encode())
    urlsafeEncrypt = base64.urlsafe_b64encode(encyptBytes).decode()
    return urlsafeEncrypt

# print(encrypt("test"))