''' Assignment 4 problem 5
generating gaussian data from uniform random numbers using Box Mullar method
NAME: SAGAR DAM;  DNAP'''
import numpy as np
from matplotlib import pyplot as plt

#generating random numbers
x1 = np.random.rand(10000)
x2 = np.random.rand(10000)

#generating Gaussian data
y1 = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)
y2 = np.sqrt(-2*np.log(x1)) * np.sin(2*np.pi*x2)

#true exponential for comparisn
x=np.arange(-4.0,4.01,0.01)
y=np.exp(-x**2/2)/(np.sqrt(2*np.pi))

#plotting
binn=np.arange(-4.0,4.1,0.1)
plt.plot(x,y,'k',label='true gaussian distribution')
plt.hist(y1,range=(-4.0, 4.0),density=True ,bins=binn,color='orange',rwidth=1.0,label='histogram of gaussian data')
plt.suptitle('plotting the histogram of gaussian data from uniform random numbers using Box Mullar method')
plt.title('(And comparisn with true gaussian data)')
plt.legend()
plt.show()