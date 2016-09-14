#parse paragraph data away from html data
#pass string of args that will apply to a strings text

'''
Identifiers:        (we're loking for these numbers)

\d = any number
\D = anything but a number
\s = space
\S = anything but a space
\w = any character
\W = anything but a charater
 . = any character, except for a new line
\. = a period
\b = the white space around words


Modifiers:           (we're looking for this amount of numbers)

{1,3} = we're expecting 1-3     \d{1-3}
    + = match 1 or more
    ? = match 0 or 1
    * = match 0 or more
    $ = match the end of a string
    ^ = match the beginning of a string
    | = either or      \d{1-3} | w{4,5}
    [] = range or 'variance'  [1-5a-qA-Z]
    {x} expecting 'x' amount


White space characters:

\n = new line
\s = space
\t = tab
\e = escape
\f = form feed
\r = return


DON'T FORGET!:

. + * ? [] $ ^ () {} | \

'''


import re

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

ageDict = {}

x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)