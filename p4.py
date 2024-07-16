import pandas as pd
import numpy as np
import os
path=os.path.abspath("shortest-path-distance-matrix.txt")

f=open(path,"r")
content=f.read()
colist=content.split("\n")
a=[]
for l in colist:
    
    
    b=[]
    for c in l:
        
         b.append(c)
    
    a.append(b)

lis=[]
for i in range(0,4604):
    for j in range(0,4604):
        if(a[i][j]=='1'):
            lis.append([i+10001,j+10001])
df=pd.DataFrame(lis,columns=['s','d'])

df['s']=df['s'].apply(lambda x:'A'+str(x))
df['s']=df['s'].apply(lambda x:str(x[:1]+str(x[2:])))
df['d']=df['d'].apply(lambda x:'A'+str(x))
df['d']=df['d'].apply(lambda x:str(x[:1]+str(x[2:])))
df.sort_values(by=['s','d'],inplace=True)
df=df.rename(columns={'s':'From_ArticleID','d':'To_ArticleID'})
df.to_csv("edges.csv",index=False)