''' Assignment 4 problem 6
generating gaussian data from uniform random numbers using Rejection method
NAME: SAGAR DAM;  DNAP'''
import numpy as np
from matplotlib import pyplot as plt

#generating random numbers and rejecting according to given distribution
y=[]
for i in range(1000000):
    x1=4*np.random.random()
    x2=np.random.rand()*np.sqrt(2/np.pi)
    if(x2<=np.sqrt(2/np.pi)*np.exp(-x1**2/2)):
        y.append(x1)

#generating true distribution
x=np.arange(0.0,4.01,0.01)
ytrue=np.exp(-x**2/2)*(np.sqrt(2/np.pi))

#plotting
binn=np.arange(0.0,4.1,0.1)
plt.plot(x,ytrue,'k',label='true given gaussian distribution')
plt.hist(y,range=(0.0, 4.0),density=True ,bins=binn,color='orange',rwidth=1.0,label='histogram of gaussian data')
plt.suptitle('plotting the histogram of gaussian data from 1000000 uniform random numbers using rejection method')
plt.title('(And comparisn with true gaussian data P(x)~sqrt(2/pi)*exp(-x^2/2))')
plt.legend()
plt.show()