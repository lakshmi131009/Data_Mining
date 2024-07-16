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
    if(len(x)==2):
        return a
    elif(len(x)>2 and len(x)<4):
        return b
    elif(len(x)==4):
        return z
    
c[2]=c[1].apply(lambda x:func(x))

cati=pd.read_csv('category-ids.csv',header=None)
arti=pd.read_csv('article-ids.csv',header=None)
adi=arti[1]
adi.index=arti[0]
adi=adi.to_dict()

cdi=cati[1]
cdi.index=cati[0]
cdi=cdi.to_dict()

def fu(x):
    return [cdi[x]]

def fu1(x):
    return adi[x]
     
            
c['id']=c[2].apply(lambda x:fu(x))
def fu1(x):
    return adi[x]
     

c['aid']=c[0].apply(lambda x:fu1(x))
c=c.drop([0,1,2],axis=1)
cols = c.columns.tolist()
cols.insert(1, cols.pop(cols.index('id')))
c = c.reindex(columns= cols)
c=c.groupby('aid',as_index=False).agg({'id':'sum'})
c['id']=c['id'].apply(lambda x:sorted(x))


dic={'aid':['A1211','A1232','A1601','A3254','A3850','A4546'],'id':['C0001','C0001','C0001','C0001','C0001','C0001']}
df2=pd.DataFrame(dic)
df3=pd.concat([c,df2],ignore_index=True)
df3.sort_values(by=['aid'],inplace=True)

df3=df3.rename(columns={'aid':'Article_ID','id':'Category_ID'})
df3.to_csv("article-categories.csv",index=False)
