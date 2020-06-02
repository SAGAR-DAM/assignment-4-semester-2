''' Assignment 4 problem 1
linear congruential random number generator
NAME: SAGAR DAM;  DNAP'''
#importing mudules
import numpy as np
from matplotlib import pyplot as plt

#taking seed
a = 21356981
c = 1234567890
m = 9753113579
x = 1.325*np.pi
n = 10000
results = []

#generating random number
for i in range(n):
    x = (a*x+c)%m
    results.append(x/m)
print(results)
I=np.arange(1,10001)

#plotting
plt.plot(I,results,'ro',markersize=0.7)
plt.title('density plot of random numbers')
plt.xlabel('i')
plt.ylabel('xi')
plt.show()
plt.hist(results,range=(0.0, 1.0),bins=np.arange(0.0,1.1,0.01), density=True,color='green',rwidth=1.0)
plt.title('histogram of density')
plt.xlabel('x')
plt.ylabel('~n(x)')
plt.show()

#comparisn with true uniform distribuion
x=np.arange(0,1.1,0.1)
y=np.ones(len(x))
plt.hist(results,range=(0.0, 1.0),bins=np.arange(0.0,1.0,0.01),label='histogram', density=True,color='yellow',edgecolor='r',rwidth=1.0)
plt.plot(x,y,color='k',label='true uniform distribution')
plt.title('comparisn with true uniform distribution')
plt.legend()
plt.show()