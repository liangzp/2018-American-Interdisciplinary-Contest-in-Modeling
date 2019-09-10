#coding:utf-8

import pandas as pd
from gurobipy import *

map=pd.read_csv('Pareto.csv')
a=dict()
m=Model('Pareto')
for i in range(len(map)):
    a[i]=m.addVar(lb=1,vtype=GRB.INTEGER,name='Number_%d'%i)
m.update()

m.setObjective(quicksum((a[i]-map.iloc[i])*(a[i]-map.iloc[i]) for i in range(len(map))),GRB.MINIMIZE)
m.addConstr(quicksum(a[i] for i in range(len(map)))==183)
m.optimize()
print('obj:%d' % m.objVal)
for v in m.getVars():
    print('%s:%d' % (v.varName, v.x))
