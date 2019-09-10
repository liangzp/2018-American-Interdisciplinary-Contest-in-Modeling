#coding:utf-8
import numpy as np
from math import log
from scipy.optimize import curve_fit
import pandas as pd
f1=0.36
def func(f,a,b):
    return -477/(8.72*a)*(-(b+100)/100*map(log,(100-f1)/(100-f))+b/100*map(log,f1/f))
t=[5,10,15,20]
f2=[1.33,3.04,5.50,8.12]

popt,pcov=curve_fit(func,f2,t)
print(popt)