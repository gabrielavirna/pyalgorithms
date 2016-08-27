## global&local vars

x = 6
def example1():
    z = 5
    print(z)
##
def example2():
    print(x)
    print(x+6)
##   x+=6 doesn't work if x isn't global

def example3():
    global x
    print(x)
    x+=5
    print(x)

##
def example4():
    globx = x
    print(globx)
    globx+=5
    print(globx)

    return globx


example1()
example2()
example3()
x = example4()
print(x)