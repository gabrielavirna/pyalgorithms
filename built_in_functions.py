import math

''' absolute value -> if you take any number,it's its distance from 0 '''
exNum1 = -5
exNum2 = 5
print(abs(exNum1))

if abs(exNum1)== abs(exNum2):
    print('These are the same')

''' help function '''
#help() # ex:time, press Ctrl+C to exit

''' maximum & minimum'''
exList = [5,3,7,1]
print(max(exList))
print(min(exList))

'''round down&up'''
x = 5.644
print(round(x))
print(math.floor(x))
print(math.ceil(x))

'''convert string to int/float, int to string'''
intMe = '55'
print(int(intMe))
print(float(intMe))

strMe = 77
print(str(strMe))

''''''