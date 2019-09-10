#coding:utf-8
import numpy as np
import pandas as pd

data=pd.read_csv('DublinSolve2.csv')
data['current']=0
data2=pd.DataFrame(data.sort_values(by='Result',ascending=False).values,columns=['Demand','Result','Location','current'])
percent=0.9
toBuild=int(247*percent)

for i in range(min(toBuild,49)):
    data2.iloc[i,3]=1
    toBuild=toBuild-1

k=0
while(toBuild>0):
    data2.iloc[k, 3]=int(min(data2.iloc[k,1]-1,toBuild)+data2.iloc[k, 3])
    toBuild=toBuild-(data2.iloc[k, 3]-1)
    k=k+1

data2['current']=data2['current'].astype('int')
data2['x']=np.floor(data2.Location/8)
data2['y']=data2.Location%8
data2['x']=data2['x'].astype('int')
data2['y']=data2['y'].astype('int')

map0=np.zeros((8, 8))
print(map0)
for i in range(len(data2)):
    x=data2.iloc[i,4]
    y=data2.iloc[i,5]
    z=data2.iloc[i,3]
    map0[x, y]=z
    print(x,y)
    print(z)
    print(map0[x, y])

import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(map0, fmt="d", cmap='YlGnBu', ax=ax)

plt.show()

# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# fig=plt.figure(figsize=(12,6))
# ax=fig.gca(projection="3d")
# ax.contourf(data2.iloc[:,4], data2.iloc[:,5], data2.iloc[:,3], rstride=1, cstride=1, cmap=plt.cm.hot)