''' problem 9 assignment 4
MCMC method
SAGAR DAM;  DNAP'''

import numpy as np
from matplotlib import pyplot as plt

def f(t):
    if(3<=t<=7):
        z=1.0
    else:
        z=0.0
    return z

n=10000
z=np.linspace(3.0,7.0,n+1)
x=[]
x0=4.50
x.append(4.50)
for i in range(n):
    y=x[0]+np.random.normal(loc=0.0,scale=1.0)
    if(f(y)/f(x[i])>=np.random.rand()):
        x.append(y)
    else:
        x.append(x[i])
s=np.arange(0,len(x),1)
plt.scatter(s,x,marker='x',color='orange')
plt.title('Markov chain')
plt.legend()
plt.show()
plt.hist(x,density='true',bins=np.arange(3.0,7.0,0.1))
plt.title('required histogram')
plt.legend()
plt.show()