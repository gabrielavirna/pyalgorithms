import os
import random

def randomBytes(n):
    for i in range(n):
        yield random.getrandbits(8)


genFile = open('generate_file.txt','w')

rand = bytearray(randomBytes(1000000))
genFile.write(str(rand))
genFile.close()
