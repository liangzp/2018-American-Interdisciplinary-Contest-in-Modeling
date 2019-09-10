#coding:utf-8

from math import e
import seaborn as sns
sns.set_style('darkgrid')
#sns.despine()
#sns.set(color_codes=True)
year=150
def func(x):
    if x<0:
        return e**(g*x)
    else:
        return 1
a=-3*50/float(2*year**3)
x_1=[a*x**2+(-2)*a*year*x for x in range(1,year)]

x_2=[]
T=3/float(2)*(year-50)
a=1/T**2
for x in range(1,year):
    if(x<=T):
        x_2.append(a*x**2)
    else:
        x_2.append(1)

x_3=[1/float(100)*x for x in range(1,year)]

x_5=[]
halfyear=year/2
B=(50/float(halfyear)-4/float(3))/(2/float(3)*halfyear**2)
A=(B*halfyear**2+1)/halfyear**2
for x in range(1,year):
    if(x<=halfyear):
        x_5.append(A*x*x)
    else:
        x_5.append(B*(x-year)**2+1)

import matplotlib.pyplot as plt
fig=plt.figure()
ax={}
number=0
for k in [0.02,0.03,0.05]:
    for g in [0.003,0.005,0.015]:
        c_1 = [0.01]
        c_2 = [0.01]
        c_3 = [0.01]
        c_4 = [0.01]
        c_5 = [0.01]



        for i in range(1,year):
            c_1.append(k*(1-x_1[i-1])*(1-c_1[i-1])+func(x_1[i-1]-c_1[i-1])*c_1[i-1])
            c_2.append(k * (1 - x_2[i-1]) * (1 - c_2[i-1]) + func(x_2[i-1] - c_2[i-1]) * c_2[i-1])
            c_3.append(k * (1 - x_3[i-1]) * (1 - c_3[i-1]) + func(x_3[i-1] - c_3[i-1]) * c_3[i-1])
            c_5.append(k * (1 - x_5[i-1]) * (1 - c_5[i-1]) + func(x_5[i-1] - c_5[i-1]) * c_5[i-1])


        for i in range(1,year):
            c_4.append(k * (1 - c_4[i-1]) * (1 - c_4[i-1]) + func(c_4[i-1] - c_4[i-1]) * c_4[i-1])


        ax[number]=fig.add_subplot(331+number)
        plt.title('k=%.3f,g=%.3f'%(k,g))
        plt.plot(c_1,label='downshift',alpha=0.8)
        plt.plot(c_2,label='upshift',alpha=0.8)
        plt.plot(c_3,label='constant_speed',alpha=0.8)
        plt.plot(c_4,label='dynamic',alpha=0.8)
        plt.plot(c_5,label='S',alpha=0.8)
        if(number>=6):
            plt.xlabel('t')
        plt.ylabel('c')
        number=number+1

ax[8].legend(loc='lower center',shadow=True,bbox_to_anchor=(1.2, 1.4),borderaxespad = 0.)
plt.show()

