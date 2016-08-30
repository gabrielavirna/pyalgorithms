# lists whithin lists,whitin lists...

x = [5,6,7,2] # 1-dimensional list
print(x)

y = [
    [5,6],[6,7],[7,2],[2,5]
    ] # 2-dim list
print(y)
print(y[1][0])

z = [
    [[5,6],[6,7]],
    [[7,2],[2,5]],
    [[6,4],[2,3]]
    ] # 3-dim list
print(z)
print(z[1][0][0])