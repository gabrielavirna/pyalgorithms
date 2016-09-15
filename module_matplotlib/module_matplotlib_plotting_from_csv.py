from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('module_matplotlib_csv_exampleFile.csv',
                 unpack='True',
                 delimiter=',')

plt.plot(x,y)

plt.title('Epic chart')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.show()


#print(x)
#print(y)

