import pandas as pd
import numpy as np
import csv
import os
path=os.path.abspath('categories.tsv')
c=pd.read_csv(path,delimiter='\t',header=None)
c[1]=c[1].apply(lambda x:x.split('.'))

def func(x):
   
    a=""
    b=""
    z=""
    if(len(x)==2):
        a= (x[0]+'.'+x[1]) 
    elif(len(x)>2 and len(x)<4):
        a= (x[0]+'.'+x[1])
        b= (x[0]+'.'+x[1]+'.'+x[2]) 
    elif(len(x)==4):
        a= (x[0]+'.'+x[1])
        b= (x[0]+'.'+x[1]+'.'+x[2]) 
        
        z= (x[0]+'.'+x[1]+'.'+x[2]+'.'+x[3])
    if(len(a)!=0 and len(b)!=0 and len(z)!=0):
        return [a,b,z]
    elif(len(a)!=0 and len(b)!=0 and len(z)==0):
        return [a,b]
    elif(len(a)!=0 and len(b)==0 and len(z)==0):
        return [a]
    
c[2]=c[1].apply(lambda x:func(x))
l=[]
l=c[2].tolist()
fl=[i  for sub in l for i in sub]
out=[]
for x in fl:
    if x not in out:
        out.append(x)
out.append('subject')
out=sorted(out)
list=[]
for i in out:
    c=0
    for j in i:
        if j=='.':
            c=c+1
    list.append((i,c))

a1=[]
for i in list:
    if(i[1]==1):
        a1.append(i[0])
a=[]
for i in list:
    if(i[1]==0):
        a.append(i[0])    
        
a3=[]
for i in list:
    if(i[1]==3):
        a3.append(i[0])
a2=[]
for i in list:
    if(i[1]==2):
        a2.append(i[0])
sorted(a1)
sorted(a2)
sorted(a3)
sum=a+a1+a2+a3
df1=pd.DataFrame(sum)
dict = {x: index for index, x in enumerate(df1[0], start=10001)}
df1['id']=df1[0].map(dict)
df1['id']=df1['id'].apply(lambda x:'C'+str(x))
df1['id']=df1['id'].apply(lambda x:str(x[:1]+str(x[2:])))

df1=df1.rename(columns={0:'Categoty_Name','id':'Category_ID'})
df1.to_csv("category-ids.csv",index=False)