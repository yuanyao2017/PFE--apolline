#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import cgi
from influxdb import InfluxDBClient

client = InfluxDBClient('apolline.lille.inria.fr', '8086', 'Apolline', 'PC2A', 'apolline')

form=cgi.FieldStorage()
stime=form.getvalue('start')
ftime=form.getvalue('finifsh')

"""
stime=str(sys.argv[1])+" "+str(sys.argv[2])
ftime=str(sys.argv[3])+" "+str(sys.argv[4])
"""
results = client.query('select * from "events.stats.rasp8" where time >\'%s\' and time <\'%s\';'%(stime,ftime))
points = list(results.get_points())

x=[]
y=[]
def readData():
    for i in range(len(points)):
        x.append(i)
        y.append(points[i]['CO2'])
    return x,y

x,y=readData() 
   
plt.plot(x,y,'-',label='original values')
plt.grid()
plt.savefig('result.png')
plt.show()