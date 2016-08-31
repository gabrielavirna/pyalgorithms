# standard libraries
'''get current working dir'''
'''make/rename/remove a directory'''


import os
import time

curWorkDir = os.getcwd()
print(curWorkDir)

os.mkdir('newDir')

time.sleep(2)
os.rename('newDir','newDir2')

time.sleep(2)
os.rmdir('newDir2')

