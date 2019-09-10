#coding:utf-8
from gurobipy import *
from math import e


k=0.1
g=0.01

def fun(x):
    if e<=0:
        return e(g*x)
    else:
        return 1
year=100
c={}
c[0]=0.01
x={}
m=Model('DevelopModel')

#add variables
for i in range(year):
    x[i]=m.addVar(lb=0,name='x_%d'%i)
m.update()

for i in range(1,year):
    c[i]=k*(1-x[i-1])*(1-c[i-1])+fun(x[i-1]-c[i-1])*c[i-1]
m.setObjective(c[year],GRB.MAXIMIZE)

