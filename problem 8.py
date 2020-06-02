''' Assignment 4 problem 8
Evaluating volume of 2d and 10d spheres using Monte Carlo method
NAME: SAGAR DAM;  DNAP'''
import numpy as np
from matplotlib import pyplot as plt

#evaluating volume of 2d circle using Monte carlo method
n=10000000
n1=0
for i in range(n):
    x1=np.random.random()
    x2=np.random.random()
    if(x2**2<=1-x1**2):
        n1=n1+1
a=4*n1/n
print('area of the unit circle in 2d using monte carlo method: ',a,' unit')
print('true area of unit circle: ',np.pi,' unit')
print()
print()

#evaluating volume of 10d sphere
n1=0
for i in range(n):
    x0=np.random.random()
    x1=np.random.random()
    x2=np.random.random()
    x3=np.random.random()
    x4=np.random.random()
    x5=np.random.random()
    x6=np.random.random()
    x7=np.random.random()
    x8=np.random.random()
    x9=np.random.random()
    if(x9**2<=1-x0**2-x1**2-x2**2-x3**2-x4**2-x5**2-x6**2-x7**2-x8**2):
        n1=n1+1
a=2**10*n1/n
print('volume of the unit circle in 10d using monte carlo method: ',a,' unit')
a=(np.pi)**5/120
print('the true volume of unit sphere in 10d: ',a,' unit')
print()
print()
print('here I have used ',n,' random numbers for both calcuaions')