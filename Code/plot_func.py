from math import e
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
num=0

def plot_beautiful(X,Y,anno):
    plt.plot(Y,linewidth=2.5)
    xmin, xmax = X.min(), X.max()
    ymin, ymax = Y.min(), Y.max()

    dx = (xmax - xmin) * 0.1
    dy = (ymax - ymin) * 0.1

    plt.xlim(xmin, xmax + dx)
    plt.ylim(ymin, ymax + dy)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.title(anno,fontsize=20)
    plt.show()

sns.set_style('white')
year=100

a=-3*50/float(2*year**3)
x_1=np.array([a*x**2+(-2)*a*year*x for x in range(1,year)])

x_2=[]
T=3/float(2)*(year-50)
a=1/T**2
for x in range(1,year):
    if(x<=T):
        x_2.append(a*x**2)
    else:
        x_2.append(1)
x_2=np.array(x_2)

x_3=np.array([1/float(100)*x for x in range(1,year)])

x_5=[]
halfyear=year/2
B=(50/float(halfyear)-4/float(3))/(2/float(3)*halfyear**2)
A=(B*halfyear**2+1)/halfyear**2
for x in range(1,year):
    if(x<=halfyear):
        x_5.append(A*x*x)
    else:
        x_5.append(B*(x-year)**2+1)
x_5=np.array(x_5)

plt.figure(figsize=(24,16), dpi=60)
ax=plt.subplot(221)
plot_beautiful(np.arange(0,year),x_1,r'Downshift: $\quad y=-\frac{3}{40000}x^2+\frac{3}{200}x$')
ax.set_ylabel(r'y',fontsize=20)
ax=plt.subplot(222)
plot_beautiful(np.arange(0,year),x_2,r'Upshift: $\quad y=\frac{1}{75^2}x^2(x\leq 75),\quad 1(75\leq x \leq 100)$')
ax.set_ylabel(r'y',fontsize=20)
ax=plt.subplot(223)
plot_beautiful(np.arange(0,year),x_3,r'Constant_speed: $\quad y=\frac{1}{100}x$')

ax.set_ylabel(r'y',fontsize=20)
ax.set_xlabel(r't',fontsize=20)

ax=plt.subplot(224)
plot_beautiful(np.arange(0,year),x_5,r'S: $\quad y=\frac{1}{5000}x^2(x \leq 50),\quad -\frac{(x-100)^2}{5000}+1(50\leq x \leq 100)$')
ax.set_ylabel(r'y',fontsize=20)
ax.set_xlabel(r't',fontsize=20)
plt.show()
