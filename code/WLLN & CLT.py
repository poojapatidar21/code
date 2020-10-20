# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:39:25 2020

@author: Pooja Patidar
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
%matplotlib inline

# Question 1 
def exp(l):
    data = np.random.exponential(1, l)
    return data

def unif(l):
    data = np.random.uniform(1, 2, l)
    return data

def bern(l):
    data = np.random.binomial(1, 0.2, l)
    return data

def plotMean(x,y):
    plt.style.use('ggplot')
    plt.plot([str(i) for i in x],y)
    plt.scatter([str(i) for i in x],y)
    for i_x, i_y in zip(np.arange(7), y):
        plt.text(round(i_x-0.4), round(i_y+0.05,2), '{}'.format(round(i_y,2)),size = 12)

m = [10, 100, 500, 1000, 5000, 10000, 50000]

plt.title('Verification of WLLN')
plt.xlabel('Sample Size')
plt.ylabel('Sample Distribution')

# (a) Exponential Distribution
y1 = [sum(exp(i))/i for i in m]
plotMean(m, y1)

# (b) Uniform Distribution
y2 = [sum(unif(i))/i for i in m]
plotMean(m, y2)

# (c) Normal Distribution
y3 = [sum(bern(i))/i for i in m]
plotMean(m, y3)

plt.legend(['Exponential','Uniform','Binomial'], fontsize = 12, loc='best', bbox_to_anchor=(0.5, 0., 0.5, 0.5))
plt.show()

#  Question 2 
sampleSize = 10000
def plotDist(n, func, dist):
    dataSet = []
    y = [0] * sampleSize
    x = [0] * sampleSize
    for i in range(n):
        data = func(sampleSize)
        dataSet.append(data)
    for i in range(sampleSize):
        for j in range(n):
            y[i] += dataSet[j][i]
        y[i] = round(y[i]/n, 2)
        
    maxX = 0
    for i in range(sampleSize):
        x[i] = y.count(y[i])
        if(x[i] > maxX):
            maxX = x[i]
    
    x = [i/maxX for i in x]
    x1 = np.linspace(min(y), max(y), 10000)
    varY = np.var(y)**0.5
    meanY = sum(y)/10000
    data = ss.norm.pdf(x1, meanY, varY)
    maxD = max(data)
    data = [i/maxD for i in data]
    plt.plot(x1, data, color = 'blue', linewidth = 2, label = ('\u03BC = '+ str(round(meanY, 5)) +'\n\u03C3 = ' + str(round(varY, 5))))
    plt.scatter(y, x)
    plt.title('n = '+str(n)+', Distribution = '+ dist)
    plt.ylabel('Sample data of '+ dist +' Dist.')
    plt.legend(fontsize = 13)
    plt.show()
    
sampleSizeList = [1, 2, 4, 8, 16, 32]

# (a) Exponential
for i in sampleSizeList:
    plotDist(i, exp, 'Exponential')
    
# (b) Uniform
for i in sampleSizeList:
    plotDist(i, unif, 'Uniform')
    
# (c) Bernoulli
for i in sampleSizeList:
    plotDist(i, bern, 'Bernoulli')









