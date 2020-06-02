''' Assignment 4 problem 7
Chi square test
NAME: SAGAR DAM;  DNAP'''

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

#input the observed data
score=np.array([2,3,4,5,6,7,8,9,10,11,12])#possible scores in dice test
ex=np.array([4,8,12,16,20,24,20,16,12,8,4])#expected count for scores 2,3,4,...
y1=np.array([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13])#observed score: 1
y2=np.array([3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5])#observed score: 2

#calculation for first observed data
V=0
for i in range(len(y1)):
    V=V+(y1[i]-ex[i])/ex[i]
c=(1.0 - stats.chi2.cdf(V, 10.0))*100
print("value of Chi square statistic for first observed data: ",V)
print("probaility that value of Chi sq variable is greater than ",V," is: ",c)
if(0<=c<1 or 99<c<=100):
    print("first observed data is NOT SUFFICIANTLY RANDOM")
elif(1<=c<5 or 95<c<=99):
    print("first observed data is SUSPECT")
elif(5<=c<10 or 90<c<=95):
    print("First observed data are ALMOST SUSPECT")
else:
    print("First observed data are SUFFICIENTLY RANDOM")
    
print()
print()

#calculartion for 2nd observed data
V=0
for i in range(len(y2)):
    V=V+(y2[i]-ex[i])/ex[i]
c=(1.0 - stats.chi2.cdf(V, 10.0))*100
print("value of Chi square statistic for second observed data: ",V)
print("probaility that value of Chi sq variable is greater than ",V," is: ",c)
if(0<=c<1 or 99<c<=100):
    print("second observed data is NOT SUFFICIANTLY RANDOM")
elif(1<=c<5 or 95<c<=99):
    print("second observed data is SUSPECT")
elif(5<=c<10 or 90<c<=95):
    print("second observed data are ALMOST SUSPECT")
else:
    print("second observed data are SUFFICIENTLY RANDOM")
    
#plotting
plt.plot(score,y1,color='k',label='first observed data')
plt.plot(score,y2,'g',label='2nd observed data')
plt.plot(score,ex,'r',label='expected distribution')
plt.plot(score,ex,'ro')
plt.grid()
plt.xlabel('value of score in two dice throwing test for 144 times')
plt.ylabel('count of score')
plt.suptitle('observed vs expected data of two dice throwing test for 144 times')
plt.title('not included in question')
plt.legend()
plt.show()