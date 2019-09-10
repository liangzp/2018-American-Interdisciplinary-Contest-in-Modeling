#coding:utf-8
import pandas as pd
import numpy as np
from math import sqrt
import copy
import math
step=1#how fast we choose
theta=1#adjusting factor
length=8#the amount of grid each side
direction_x=[-1,-1,-1,0,0,0,1,1,1]
direction_y=[-1, 0, 1, -1, 0, 1, -1, 0, 1]
percentage=1

def getNearby(x,y):
    nearbyValue=0
    for i in range(len(direction_x)):
        x_new=x+direction_x[i]
        y_new= y + direction_y[i]
        if((x_new<=length) and (x_new>=1) and (y_new<=length) and (y_new>=1)):
            nearbyValue=nearbyValue+1/(1+theta*sqrt(direction_x[i]**2+direction_y[i]**2)/value[x_new,y_new])
    return nearbyValue

def update():
    for i in range(1,length+1):
        for j in range(1,length+1):
            temp[i, j] = value[i, j]*getNearby(i, j)
    return temp

#prepare data
metadata=pd.read_csv('DublinSolve2.csv')

#set Location
metadata['x']=np.floor(metadata.Location/8)
metadata['y']=metadata.Location%8
metadata['x']=metadata['x'].astype('int')
metadata['y']=metadata['y'].astype('int')

map=np.zeros((length+2,length+2))
value=np.zeros((length+2,length+2))
value_temp=np.zeros((length+2,length+2))
for i in range(len(metadata)):
    x=metadata.iloc[i,3]+1
    y=metadata.iloc[i,4]+1
    map[x,y]=metadata.iloc[i,1]


#around
for i in range(length+2):
    for j in range(length+2):
        if(map[i,j]==0):
            map[i,j]=0.0000001
        value[i, j] = map[i,j]


#initial
print('initial')
temp=copy.copy(value)



stations=int(sum(metadata['Result'])*percentage)
print(stations)
#optimize
while(stations>0):
    temp = update()
    select=[-1,-1]
    select_value=-1
    for i in range(1,length+1):
        for j in range(1,length+1):
            if(temp[i,j]>select_value):
                select_value=temp[i,j]
                select=[i,j]

    #update
    value[select[0],select[1]]=value[select[0],select[1]]-1
    stations = stations - step
value=value[1:length+1,1:length+1]
map=map[1:length+1,1:length+1]
station_num=map-value

import seaborn as sns
import matplotlib.pyplot as plt
sns.set()
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(station_num, fmt="d",cmap='YlGnBu', ax=ax)
plt.show()