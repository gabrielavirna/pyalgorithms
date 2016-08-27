## def function_name(parameters name):

def example_fct():
    print('basic function')
    z = 3 + 9
    print(z)
###
def simple_addition(num1, num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)

example_fct()
simple_addition(5,3)
simple_addition(num2=3,num1=5)

###
def simple(num1,num2):
    pass

def simple(num1,num2=5):
    pass
    print(num1,num2)
simple(2)

###
def basic_window(width,height,font='TNR',
                 bgc='w',scrollbar=True):
    print(width,height,font,bgc)
basic_window(500,350)