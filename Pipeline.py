#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

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

''' Mean Squared Error '''
def rmse(y_test, y):
    return sp.sqrt(sp.mean((y_test - y) ** 2))

''' Comparer avec la moyenne, entre [0-1]. 1 représente une prédiction parfaite.'''
def R2(y_test, y_true):
    return 1 - ((y_test - y_true)**2).sum() / ((y_true - y_true.mean())**2).sum()

def R22(y_test, y_true):
    y_mean = np.array(y_true)
    y_mean[:] = y_mean.mean()
    return 1 - rmse(y_test, y_true) / rmse(y_mean, y_true)

plt.plot(x, y)
plt.scatter(x, y, s=5)
degree = [5,10]
y_test = []
y_test = np.array(y_test)


for d in degree:
    
    clf = Pipeline([('poly', PolynomialFeatures(degree=d)),
                    ('linear', LinearRegression(fit_intercept=False))])
    '''
    clf = Pipeline([('poly', PolynomialFeatures(degree=d)),
                    ('linear', linear_model.Ridge ())])
    '''
    clf.fit(x[:, np.newaxis],y)
    y_test = clf.predict(x[:, np.newaxis])

    print(clf.named_steps['linear'].coef_)
    print('rmse=%.2f, R2=%.2f, R22=%.2f, clf.score=%.2f' %(rmse(y_test, y),R2(y_test, y),R22(y_test, y),clf.score(x[:, np.newaxis], y)))    
    
    plt.plot(x, y_test, linewidth=2)

plt.grid()
plt.legend(['original values','5','10'], loc='upper right')
plt.show()
