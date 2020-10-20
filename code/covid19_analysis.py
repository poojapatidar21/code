# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:25:46 2020

@author: Pooja Patidar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel('Covid19IndiaData_30032020.xlsx')

#------------------------------------------------------------------------------------------
#Problem 1(i)
ages={}
n=len(data)
for i in data['Age']:
    try:
        ages[i]+=(1/n)
    except:
        ages.update({i:1/n})

fig,ax=plt.subplots()
ax.set_yscale('log')
plt.xlabel('age of infected person')
plt.ylabel('Pmf')
ax.set_title('pmf vs age of infected person')
ax.stem(ages.keys(),ages.values(),use_line_collection=True)
ex=0
ex2=0
for i,j in ages.items():
    ex+=(i*j)
    ex2+=(i*i*j)
var=ex2-ex**2
print("q1(i)")
print("expected age of infected pateints   :",ex)
print("variance of pmf                     :",var)
#The variance seems high because of very large no. of cases at perticular age(38). 
#Based on the variance, we can infer that a widerange of age groups 
#are being affected around 38

#------------------------------------------------------------------------------------------
#Problem 1(ii)

age_dead={}
age_rec={}
for i in range(n):
    if data.loc[i]['StatusCode']=='Dead':
        try:
            age_dead[data.loc[i]['Age']]+=1
        except KeyError:
            age_dead.update({data.loc[i]['Age']:1})
    else:
        try:
            age_rec[data.loc[i]['Age']]+=1
        except KeyError:
            age_rec.update({data.loc[i]['Age']:1})

rc=sum(age_rec.values())
dc=sum(age_dead.values())
fig,ax=plt.subplots(1,2,figsize=(15,5))
ax[0].set_yscale('log')
plt.xlabel('age of infected')
plt.ylabel('Probability')
ax[0].set_title('Recovered')
ax[0].stem(age_rec.keys(),np.array(list(age_rec.values()))/rc,use_line_collection=True)
ax[1].set_yscale('log')
plt.xlabel('age of infected')
plt.ylabel('Probability')
ax[1].set_title('Dead')
ax[1].stem(age_dead.keys(),np.array(list(age_dead.values()))/dc,use_line_collection=True)

ex_rec=0
ex2_rec=0
for i,j in age_rec.items():
    ex_rec+=(i*j/rc)
    ex2_rec+=(i*i*j/rc)
var_rec=ex2_rec-ex_rec**2
print("\n q1(ii)")
print("expectation recover      :",ex_rec)
print("variance of pmf          :",var_rec)


ex_dead=0
ex2_dead=0
for i,j in age_dead.items():
    ex_dead+=(i*j/dc)
    ex2_dead+=(i*i*j/dc)
var_dead=ex2_dead-ex_dead**2

print("expectation dead         :",ex_dead)
print("variance of pmf          :",var_dead)
#Comparing the expectation values, we can say that COVID is lethal for 
#elder people(above 60 years)

#-----------------------------------------------------------------------------------------
#Problem 1(iii)
age_m={}
age_f={}
for i in range(n):
    if data.loc[i]['GenderCode0F1M']==0:
        try:
            age_f[data.loc[i]['Age']]+=1
        except:
            age_f.update({data.loc[i]['Age']:1})
    else:
        try:
            age_m[data.loc[i]['Age']]+=1
        except:
            age_m.update({data.loc[i]['Age']:1})
            
mc=sum(age_m.values())
fc=sum(age_f.values())
fig,ax=plt.subplots(1,2,figsize=(15,5))
ax[0].set_title('Male Patients')
plt.xlabel('age of infected')
plt.ylabel('Probability')
ax[0].set_yscale('log')
ax[0].stem(age_m.keys(),np.array(list(age_m.values()))/mc,use_line_collection=True)
ax[1].set_title('Female Patients')
plt.xlabel('age of infected')
plt.ylabel('Probability')
ax[1].set_yscale('log')
ax[1].stem(age_f.keys(),np.array(list(age_f.values()))/fc,use_line_collection=True)
plt.show()

ex_m=0
ex2_m=0
for i,j in age_m.items():
    ex_m+=(i*j/mc)
    ex2_m+=(i*i*j/mc)
var_m=ex2_m-ex_m**2
print("\n q1(iii)")
print("expected age of male      :",ex_m)
print("variance of pmf           :",var_m)

ex_f=0
ex2_f=0
for i,j in age_f.items():
    ex_f+=(i*j/fc)
    ex2_f+=(i*i*j/fc)
var_f=ex2_f-ex_f**2

print("expected age of female    :",ex_f)
print("variance of pmf           :",var_f)
#The expectation values for male and female patients are almost identical but
#variance of pmf, female have very high infected rate as compared to male

#-----------------------------------------------------------------------------------------
#Problem 2(i)

data=pd.read_excel('linton_supp_tableS1_S2_8Feb2020.xlsx',sheet_name=0)
inc={}

for i,j,k in zip(data['ExposureL'],data['Onset'],data['ExposureType']):
    if k=='Lives-works-studies in Wuhan' and pd.isnull(i):
        i=pd.Timestamp('2019-12-01')
    if not pd.isnull(i) and not pd.isnull(j):
        try:
           inc[int(str(j-i).split()[0])]+=1
        except:
            inc.update({int(str(j-i).split()[0]):1})
            
inc_values=sum(inc.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
plt.xlabel('no. of days')
plt.ylabel('Probability')
ax.set_title('pmf vs incubation period of wuhan')
ax.stem(inc.keys(),np.array(list(inc.values()))/inc_values,use_line_collection=True)

ex=0
ex2=0
for i,j in inc.items():
    ex+=(i*j/inc_values)
    ex2+=(i*i*j/inc_values)
var=ex2-ex**2
print("\n q2(i)")
print("expected period of incubatio      :",ex)
print("variance of pmf                   :",var)
 
#-----------------------------------------------------------------------------------------
#Problem 2(ii)

nonwuhan=data[(data['ExposureType']!='Lives-works-studies in Wuhan')]
inc_nw={}

for i,j in zip(nonwuhan['ExposureL'],nonwuhan['Onset']):
    if not pd.isnull(i) and not pd.isnull(j):
        try:
           inc_nw[int(str(j-i).split()[0])]+=1
        except:
            inc_nw.update({int(str(j-i).split()[0]):1})
            
inc_nw_val=sum(inc_nw.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
plt.xlabel('no. of days')
plt.ylabel('Probability')
ax.set_title('pmf vs incubation period of non-wuhan')
ax.stem(inc_nw.keys(),np.array(list(inc_nw.values()))/inc_nw_val,use_line_collection=True)

ex=0
ex2=0
for i,j in inc_nw.items():
    ex+=(i*j/inc_nw_val)
    ex2+=(i*i*j/inc_nw_val)
var=ex2-ex**2
print("\n q2(ii)")
print("expected period of incubation non-wuhan  :",ex)
print("variance of pmf                          :",var)
#Wuhan Residents have a longer incubation period as compared to
#Non-Wuhan Residents


#-----------------------------------------------------------------------------------------
#Problem 2(iii)
dead=pd.read_excel('linton_supp_tableS1_S2_8Feb2020.xlsx',sheet_name=1)
daysho={}

for i in range(len(dead)):
    if not pd.isnull(dead.loc[i]['Hospitalization/Isolation']) and not pd.isnull(dead.loc[i]['Onset']):
        ds=int(str(dead.loc[i]['Hospitalization/Isolation']-dead.loc[i]['Onset']).split()[0])
        try:
            daysho[ds]+=1
        except:
            daysho.update({ds:1})

dc=sum(daysho.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_title('Onset - Hospitalization for Dead Patients')
ax.stem(daysho.keys(),np.array(list(daysho.values()))/dc,use_line_collection=True)

ex=0
ex2=0
for i,j in daysho.items():
    ex+=(i*j/dc)
    ex2+=(i*i*j/dc)
var=ex2-ex**2
print("\n q2(iii)")
print("expectation (H-O) for dead   :",ex)
print("variance (H-O) for dead      :",var)


daysdo={}

for i in range(len(dead)):
    if not pd.isnull(dead.loc[i]['Death']) and not pd.isnull(dead.loc[i]['Onset']):
        ds=int(str(dead.loc[i]['Death']-dead.loc[i]['Onset']).split()[0])
        try:
            daysdo[ds]+=1
        except:
            daysdo.update({ds:1})

dc=sum(daysdo.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_title('Onset - Death')
ax.stem(daysdo.keys(),np.array(list(daysdo.values()))/dc,use_line_collection=True)

ex=0
ex2=0
for i,j in daysdo.items():
    ex+=(i*j/dc)
    ex2+=(i*i*j/dc)
var=ex2-ex**2
print("expectation (X-O)            :",ex)
print("variance (X-O)               :",var)


dayshd={}

for i in range(len(dead)):
    if not pd.isnull(dead.loc[i]['Hospitalization/Isolation']) and not pd.isnull(dead.loc[i]['Death']):
        ds=int(str(dead.loc[i]['Death']-dead.loc[i]['Hospitalization/Isolation']).split()[0])
        try:
            dayshd[ds]+=1
        except:
            dayshd.update({ds:1})

dc=sum(dayshd.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_title('Hospitalization - Death')
ax.stem(dayshd.keys(),np.array(list(dayshd.values()))/dc,use_line_collection=True)

ex=0
ex2=0
for i,j in dayshd.items():
    ex+=(i*j/dc)
    ex2+=(i*i*j/dc)
var=ex2-ex**2
print("expectation (X-H)            :",ex)
print("variance (X-H)               :",var)


# The random variable Onset-Death = Onset-Hospitalizaton + Hospitalization-Death

dayshol={}

for i in range(len(data)):
    if not pd.isnull(data.loc[i]['DateHospitalizedIsolated']) and not pd.isnull(data.loc[i]['Onset']):
        ds=int(str(data.loc[i]['DateHospitalizedIsolated']-data.loc[i]['Onset']).split()[0])
        try:
            dayshol[ds]+=1
        except:
            dayshol.update({ds:1})

dcl=sum(dayshol.values())
fig,ax=plt.subplots()
ax.set_yscale('log')
ax.set_title('Onset - Hospitalization for Living Patients')
ax.stem(dayshol.keys(),np.array(list(dayshol.values()))/dcl,use_line_collection=True)

ex=0
ex2=0
for i,j in dayshol.items():
    ex+=(i*j/dcl)
    ex2+=(i*i*j/dcl)
var=ex2-ex**2
print("expectation (H-O) for living :",ex)
print("variance (H-O) for living    :",var)
#Those who survived have lesser expectation of O - H, i.e. they were 
#immediately joined in a hospital after onset of symptoms
