#TOSHA256
#Filip Rokita
#www.filiprokita.com

import hashlib

text=input("TEXT: ")

encoded=text.encode()
result=hashlib.sha256(encoded).hexdigest()

print("SHA256:",result)
input()