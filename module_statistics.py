import statistics
#import statistics as s --> x = s.mean(example_list)
#from statistics import *  ## x = variance(example_list)
#from statistics2 import mean,stdev,variance ##x = mean(example_list)
#from statistics import mean as m, variance as v, stdev as st ## x = m(example_list)
#import variance as v ## x = v(example_list)

example_list = [3,5,6,2,1,78,90,23,42]
x = statistics.mean(example_list)
y = statistics.stdev(example_list)
z = statistics.variance(example_list)

print(x)
print(y)
print(z)
