#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scipy.interpolate as itp
import matplotlib.pyplot as plt
import numpy as np

lie=[]
for line in open("data/neight/20170127neight.txt"):
    line=line.replace('\n','')
    lie.append(line)

x=[]
y=[]
for i in range(len(lie)):
    x.append(i)
    y.append(lie[i])
x=np.array(x)
y=np.array(y,dtype=np.float64)
plot1=plt.plot(x, y, '-',label='original values')

dis=[3]
for d in dis:
    xvals=np.linspace(0,x[len(x)-1],len(x)/d)
    yinterp = itp.spline(x,y,xvals)
    print(xvals)
    print(yinterp)

    plot2=plt.plot(xvals, yinterp, linewidth=2)
plt.grid()
#plt.legend(['original values','3'], loc='upper right')
plt.show()