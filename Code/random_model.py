#coding:utf-8

from math import e
import numpy as np

year=150
def func(x):
    if x<0:
        return e**(g*x)
    else:
        return 1
x_1=[-3/float(40000)*x**2+3/float(200)*x for x in range(1,year)]

x_2=[]
T=3/2*(year-50)
a=1/T**2
for x in range(1,year):
    if(x<=T):
        x_2.append(a*x**2)
    else:
        x_2.append(1)

x_3=[1/float(100)*x for x in range(1,year)]

x_5=[]
halfyear=year/2
for x in range(1,year):
    if(x<=halfyear):
        x_5.append(1/halfyear**2*x*x)
    else:
        x_5.append(-(x-year)**2/halfyear**2+1)

import matplotlib.pyplot as plt
fig=plt.figure(1)
ax={}
number=0
sigma=0.008
for k in [0.01,0.02,0.03]:
    for g in [0.003,0.005,0.008]:
        rand=np.random.normal(0,sigma)
        c_1 = [0.01]
        c_2 = [0.01]
        c_3 = [0.01]
        c_4 = [0.01]
        c_5 = [0.01]



        for i in range(1,year):
            c_1.append(min(k*(1-x_1[i-1])*(1-c_1[i-1])+func(x_1[i-1]-c_1[i-1])*c_1[i-1]+rand,1))
            c_2.append(min(k * (1 - x_2[i-1]) * (1 - c_2[i-1]) + func(x_2[i-1] - c_2[i-1]) * c_2[i-1]+rand,1))
            c_3.append(min(k * (1 - x_3[i-1]) * (1 - c_3[i-1]) + func(x_3[i-1] - c_3[i-1]) * c_3[i-1]+rand,1))
            c_5.append(min(k * (1 - x_5[i-1]) * (1 - c_5[i-1]) + func(x_5[i-1] - c_5[i-1]) * c_5[i-1]+rand,1))


        for i in range(1,year):
            c_4.append(min(k * (1 - c_4[i-1]) * (1 - c_4[i-1]) + func(c_4[i-1] - c_4[i-1]) * c_4[i-1]+rand,1))


        ax[number]=fig.add_subplot(331+number)
        plt.title('k=%.3f,g=%.3f'%(k,g))
        plt.plot(c_1,label='quadric')
        plt.plot(c_2,label='convex')
        plt.plot(c_3,label='static')
        plt.plot(c_4,label='dynamic')
        plt.plot(c_5,label='logistics')
        number=number+1

ax[8].legend(loc='lower center',shadow=True,bbox_to_anchor=(1.2, 1.4),borderaxespad = 0.)
plt.show()