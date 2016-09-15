#python -m pip install --user matplotlib

from matplotlib import pyplot as plt
from matplotlib import style

'''Line charts'''

''' Styles:
'fivethirtyeight', 'dark_background', 'seaborn-darkgrid',''grayscale', 'ggplot', 'classic'
'''
#print(plt.style.available)

#style.use('ggplot')


'''Graphing'''
#plt.plot([5,6,7,8],[7,3,8,3])    #(x,y) variables
#plt.show()

x1 = [2,4,6,8]
y1 = [7,3,8,3]

x2 = [1,3,5,7]
y2 = [6,7,2,6]

#print(len(x1))                    # x should have same no of values as y
#print(len(y1))

#plt.plot(x1,y1)
#plt.plot(x2,y2)


'''Line charts'''
#plt.plot(x1,y1,'g',linewidth=5, label='Line1')
#plt.plot(x2,y2,'c',linewidth=10, label='Line2')

'''Scatter plots'''
#plt.scatter(x1,y1,color='c')
#plt.scatter(x2,y2,color='g')

'''Bar charts '''
plt.bar(x1,y1,color='c',align='center')
plt.bar(x2,y2,color='g',align='center')



'''Labels,Titles,Legends,Grids'''
plt.title('Epic Chart')

plt.xlabel('X axis')
plt.ylabel('Y axis')

#plt.legend()

#plt.grid(True, color='g')

plt.show()


