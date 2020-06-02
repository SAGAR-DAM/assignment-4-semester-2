''' Assignment 4 problem 3
calculating time for random number generating
NAME: SAGAR DAM;  DNAP'''
import timeit
import numpy as np
from matplotlib import pyplot as plt

mysetup='''
import numpy as np
from matplotlib import pyplot as plt
'''
#calculating time for code without numpy module
mycode1='''
a = 21356981
c = 1234567890
m = 9753113579
x = 1.325*np.pi
n = 10000
results = []
for i in range(n):
    x = (a*x+c)%m
    results.append(x/m)
'''

t1=timeit.timeit(setup=mysetup,stmt = mycode1, number = 1000)
print("time taken for 10000 random numbers without numpy module: ",t1/1000)

#calculating time for code with numpy module

mycode2='''
R=np.random.rand(10000,1)
'''

t2=timeit.timeit(setup=mysetup,stmt = mycode2, number = 1000)
print("time taken for 10000 random numbers with numpy module: ",t2/1000)