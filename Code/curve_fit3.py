#coding:utf-8

from gurobipy import *
import numpy as np
from math import log

f1=100-0.36
def func(f,a,b):
    return -477*a/(8.72)*(-(b+100)/100*(log(100-f1)-log(100-f))+b/100*(log(f1)-log(f)))

t=np.array([5,10,15,20])
f2=100-np.array([1.33,3.04,5.50,8.12])
m=Model('curve_fit0')
a=m.addVar(lb=0,name='a')
b=m.addVar(lb=0,name='b')
m.update()
m.setObjective(sum([(func(f2[i],a,b)-t[i])*(func(f2[i],a,b)-t[i]) for i in range(len(f2))]),GRB.MINIMIZE)
m.optimize()
print('obj:%d' % m.objVal)
for v in m.getVars():
    print('%s:%d' % (v.varName, v.x))
