#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import math
from influxdb import InfluxDBClient
client = InfluxDBClient('apolline.lille.inria.fr', '8086', 'Apolline', 'PC2A', 'apolline')
#all datas
results = client.query('select * from "events.stats.rasp8" where time >%s and time < %s;'%('\'2017-01-27 08:00:00.000\'','\'2017-01-27 17:30:00.000\''))
points = list(results.get_points())

def readData():
    s=""
    for point in points:
        s=s+str(point['CO2'])+"\n"
    return s
    
def storeData():
    result = readData()
    res=open("data/day/20170127day.txt", "w")
    res.write(result)
    res.close
storeData()
'''    
#max
resultMax = client.query('SELECT max(CO2) FROM "events.stats.bureau107";')
resultMax=list(resultMax.get_points())
print("the max CO2 is %d at %s"%(resultMax[0]['max'],resultMax[0]['time']))


#min
resultMin = client.query('SELECT min(CO2) FROM "events.stats.bureau107";')
resultMin=list(resultMin.get_points())
print("the min CO2 is %d at %s"%(resultMin[0]['min'],resultMin[0]['time']))

#avg
n,t=0,0
for point in points:
    n+=1
    t+=point['CO2']    
avg=float(t/n)
print("the avg temperature is %f"%(avg))

#print("Result: {0}".format(result))

#STDEVP
dev=0
for point in points:
    dev=math.pow((point['CO2']-avg),2)
stdevp=float(dev/n)
print("the fluctuation(variance) of temperature is %f"%(stdevp))
'''  
    