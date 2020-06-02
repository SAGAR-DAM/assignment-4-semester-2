''' Assignment 4 problem 2
linear congruential random number generator with numpy module
NAME: SAGAR DAM;  DNAP'''
#importing module
import numpy as np
from matplotlib import pyplot as plt

#generating random numbers
R=np.random.rand(10000,1)
print(R)

#plotting histogram and distribution
I=np.arange(1,10001)
plt.plot(I,R,'ro',markersize=0.7)
plt.title('density plot of random numbers with numpy module np.random.rand')
plt.xlabel('i')
plt.ylabel('xi')
plt.show()
plt.hist(R,range=(0.0, 1.0),bins=np.arange(0.0,1.0,0.01), density=True,color='green',edgecolor='red',rwidth=1.0)
plt.title('histogram of density with np.rand.rand')
plt.xlabel('x')
plt.ylabel('~n(x)')
plt.show()

#comparisn with true uniform distribuion
x=np.arange(0,1.1,0.1)
y=np.ones(len(x))
plt.hist(R,range=(0.0, 1.0),bins=np.arange(0.0,1.0,0.01),label='histogram', density=True,color='yellow',edgecolor='red',rwidth=1.0)
plt.plot(x,y,color='k',label='true uniform distribution')
plt.title('comparisn with true uniform distribution')
plt.legend()
plt.show()