# lists & tuples are both lists but:
#tuple = immutable - cannot be changed,
# list = mutable can be modified ->add,change,remove,reorder values

# tuple
x = 5,2,6,2
y = (5,6,2,6)
#list
z = [5,6,2,6]

''''''
print(x[1])
print(y[3])
print(z[0])

''''''
def exampleFunc():
    return 15,6,7

x,y,z = exampleFunc()
print(x,y,z)



