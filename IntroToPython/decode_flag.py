#!/usr/bin/python
#
#Code by: Gleydstone Pereira
#this script decode the flag of TryHackMe Intro to Python Challenge
#The flag has been encoded a total of 15 times. 5 times encoded using base 64, 5 times encoded using base 32, 5 times encoded using base 16
#The flag foi codificada 15 vezes = 5 vezes com base64, 5 vezes com base 32 e 5 vezes com base16

#import the library base64
import base64

#load file encodedflag.txt
encoded = open("encodedflag.txt", "rb").read()

#decode base16 5 times
i=0
while i <=4:
    a = base64.b16decode(encoded)
    encoded = a
    i+=1

#decode base32 5 times
j=0
while j <=4:
    b = base64.b32decode(encoded)
    encoded = b
    j+=1

#decode base16 5 times
k=0
while k <=4:
    c = base64.b64decode(encoded)
    encoded = c
    k+=1

#print flag decoded
print(encoded)
