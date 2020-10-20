# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 19:29:56 2020

@author: Pooja Patidar
"""


#Q1
import matplotlib.pyplot as plt
import numpy as np

#part(a)
print('Q1')
l=1/57

x=np.linspace(0,endpoint=False,stop=48)
y=l*np.exp(-l*x)

plt.figure()
plt.plot(x, y)
plt.title('(a) PDF of wait time')
plt.xlabel('Wait Time')
plt.ylabel('Probability Density')
plt.show()

#part(b)
time1=1/60
p1=1 - np.exp(-l*time1)
print("(b)",p1)

time2=2/60
p2=(1 - np.exp(-l*time2))-(1 - np.exp(-l*time1))
print("(c)",p2)


#part 4
p3=np.exp(-l*time2)
print("(d)",p3)


#part 5
p4=(1 - np.exp(-l*2*time2))-(1 - np.exp(-l*2*time1))
print("(e)",p4)

 

#Q2
import pandas as pd
data=pd.read_csv("C:\\Users\\Pooja Patidar\\Downloads\\IC252_Lab8.csv").fillna(value=0)
print("Q2")
#part(a)
a=[]
for i in data['Status']:
    a.append(i)
for n,z in enumerate(a):
    if z=='Hospitalized' :
        a[n]=1
    if z=='Recovered' :
        a[n]=2
    if z=='Dead' :
        a[n]=3

p=[]
#part(b)
print("(B)")
#(a)
def correlation(x,y):
    xmean=0
    ymean=0
    xvar=0
    yvar=0
    covar=0
    for i in range(len(x)) :
        xmean+=(x[i]/len(x))
        ymean+=(y[i]/len(y))
    for j in range(len(x)):
        covar+=(((x[j]-xmean)*(y[j]-ymean))/(len(x)-1))
        xvar+=(((x[j]-xmean)**2)/(len(x)-1))
        yvar+=(((y[j]-ymean)**2)/(len(y)-1))
    return covar,covar/((xvar*yvar)**0.5)
x=a
y=[]
for j in data['Population']:
    y.append(j)   

ans=correlation(x,y)
p.append(ans[1])
print("(a)",ans[1])


#(b)
def correlation(x,y):
    xmean=0
    ymean=0
    xvar=0
    yvar=0
    covar=0
    for i in range(len(x)) :
        xmean+=(x[i]/len(x))
        ymean+=(y[i]/len(y))
    for j in range(len(x)):
        covar+=(((x[j]-xmean)*(y[j]-ymean))/(len(x)-1))
        xvar+=(((x[j]-xmean)**2)/(len(x)-1))
        yvar+=(((y[j]-ymean)**2)/(len(y)-1))
    return covar,covar/((xvar*yvar)**0.5)
x=a
y=[]
for j in data['SexRatio']:
    y.append(j)   

ans=correlation(x,y)
p.append(ans[1])
print("(b)",ans[1])

#(c)
def correlation(x,y):
    xmean=0
    ymean=0
    xvar=0
    yvar=0
    covar=0
    for i in range(len(x)) :
        xmean+=(x[i]/len(x))
        ymean+=(y[i]/len(y))
    for j in range(len(x)):
        covar+=(((x[j]-xmean)*(y[j]-ymean))/(len(x)-1))
        xvar+=(((x[j]-xmean)**2)/(len(x)-1))
        yvar+=(((y[j]-ymean)**2)/(len(y)-1))
    return covar,covar/((xvar*yvar)**0.5)
x=a
y=[]
for j in data['Literacy']:
    y.append(j*1000)  


ans=correlation(x,y)
p.append(ans[1])
print("(c)",ans[1])

#(d)       
def correlation(x,y):
    xmean=0
    ymean=0
    xvar=0
    yvar=0
    covar=0
    for i in range(len(x)) :
        xmean+=(x[i]/len(x))
        ymean+=(y[i]/len(y))
    for j in range(len(x)):
        covar+=(((x[j]-xmean)*(y[j]-ymean))/(len(x)-1))
        xvar+=(((x[j]-xmean)**2)/(len(x)-1))
        yvar+=(((y[j]-ymean)**2)/(len(y)-1))
    return covar,covar/((xvar*yvar)**0.5)
x=a
y=[]
for j in data['Age']:
    y.append(j)   

ans=correlation(x,y)
p.append(ans[1])
print("(d)",ans[1])

       
#(e)
def correlation(x,y):
    xmean=0
    ymean=0
    xvar=0
    yvar=0
    covar=0
    for i in range(len(x)) :
        xmean+=(x[i]/len(x))
        ymean+=(y[i]/len(y))
    for j in range(len(x)):
        covar+=(((x[j]-xmean)*(y[j]-ymean))/(len(x)-1))
        xvar+=(((x[j]-xmean)**2)/(len(x)-1))
        yvar+=(((y[j]-ymean)**2)/(len(y)-1))
    return covar,covar/((xvar*yvar)**0.5)
x=a
y=[]
for j in data['SmellTrend']:
    y.append(j)   

ans=correlation(x,y)
p.append(ans[1])
print("(e)",ans[1])

#(f)
def correlation(x,y):
    xmean=0
    ymean=0
    xvar=0
    yvar=0
    covar=0
    for i in range(len(x)) :
        xmean+=(x[i]/len(x))
        ymean+=(y[i]/len(y))
    for j in range(len(x)):
        covar+=(((x[j]-xmean)*(y[j]-ymean))/(len(x)-1))
        xvar+=(((x[j]-xmean)**2)/(len(x)-1))
        yvar+=(((y[j]-ymean)**2)/(len(y)-1))
    return covar,covar/((xvar*yvar)**0.5)
x=a
y=[]
for j in data['Gender']:
    y.append(j)   

ans=correlation(x,y)
p.append(ans[1])
print("(f)",ans[1])

#part(c)
print("(C)")
p.sort()
print("Age is correlate strongly to the Status by",p[5])