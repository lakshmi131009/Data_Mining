import pandas as pd
import numpy as np
import os
path=os.path.abspath('paths_finished.tsv')

t=open(path)
c=pd.read_csv(t,delimiter='\t',header=None)
c = c.drop([0,1,2,4],axis=1)
c['data']=c[3].apply(lambda x:x.split(';'))
c = c.drop([3],axis=1)
c['l']=c['data'].apply(lambda x:len(x))
c['T']=c['data'].apply(lambda x:  len(x)==1)
c['T']=c['T'].astype(str)
c = c[~c["T"].str.contains('True')]
c = c.drop(['T'],axis=1)


def func1(x):
    count=0
    for i in range(len(x)):
        if(x[i]=="<"):
            count+=1
    return count
    
    

c['w']=c['data'].apply(lambda x:func1(x))    
c['wo']=(c['l']-2*c['w'])-1
c['l']=c['l']-1
path=os.path.abspath('articles.tsv')

t=open(path)
df = pd.read_csv(t,delimiter="\t",header=None)
dict = {x: index for index, x in enumerate(df[0], start=0)}
#df['id']=df[0].map(dict)

f=open("shortest-path-distance-matrix.txt","r")
content=f.read()
colist=content.split("\n")
a=[]
for l in colist:
    
    
    b=[]
    for co in l:
        b.append(co)
        
    
    a.append(b)

lis=[]
def fu(x):
     return dict[x]
    
     
           
        
            
c['s']=c['data'].apply(lambda x:fu(x[0]))
c['d']=c['data'].apply(lambda x:fu(x[len(x)-1]))
c=c.drop(2395)
si=list(c.s)
di=list(c.d)

for i in range(0,len(si)):
    m=si[i]
    n=di[i]
    if(a[m][n]!="_" and a[m][n]!="0"):
        lis.append(a[m][n])
        
c['path']=lis
c = c.drop(['data','w','s','d'],axis=1)



#c.apply(pd.to_numeric)
#c=c.dropna()

w=c.copy()
wo=c.copy()
w = w.drop(['wo'],axis=1)
wo=wo.drop(['l'],axis=1)
w=w.apply(pd.to_numeric)
wo=wo.apply(pd.to_numeric)
w['ratio']=round((w['l']/w['path']),2)
wo['ratio']=round((wo['wo']/w['path']),2)

w=w.rename(columns={'l':'humanpath'})
wo=wo.rename(columns={'wo':'humanpath'})

wo=wo.rename(columns={'humanpath':'Human_Path_Length','path':'Shortest_Path_Length','ratio':'Ratio'})
w=w.rename(columns={'humanpath':'Human_Path_Length','path':'Shortest_Path_Length','ratio':'Ratio'})

w.to_csv("finished-paths-back.csv",index=False)
wo.to_csv("finished-paths-no-back.csv",index=False)