x = [1,2,3,4,5,6,9,6,6]
y = ['Jane', 'Jessy', 'Kelly', 'Alice', 'Joe', 'Bob']
x.append(8)
print(x)

x.insert(6,7) # index[6],value:7
print(x)

x.remove(1)
print(x)

x.remove(x[2])
print(x)

print(x[3])

print(x[0:5])

print(x.index(3))

print(x.count(6)) # how many values of 6 are in the list

x.sort()
print(x)

y.sort()
print(y)