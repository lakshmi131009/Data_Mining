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

patha=os.path.abspath('articles.tsv')
t=open(patha)
df = pd.read_csv(t,delimiter="\t",header=None)
dict = {x: index for index, x in enumerate(df[0], start=0)}
#df['id']=df[0].map(dict)


paths=os.path.abspath('shortest-path-distance-matrix.txt')
f=open(paths,"r")
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
c = c.drop(['data','w','l'],axis=1)



pathcc=os.path.abspath('categories.tsv')
tl=open(pathcc)
cl=pd.read_csv(tl,delimiter='\t',header=None)
cl[1]=cl[1].apply(lambda x:x.split('.'))

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
    
cl[2]=cl[1].apply(lambda x:func(x))

cati=pd.read_csv('category-ids.csv',header=None)
arti=pd.read_csv('article-ids.csv',header=None)

cdi=cati[1]
cdi.index=cati[0]
cdi=cdi.to_dict()

adi=arti[1]
adi.index=arti[0]
adi=adi.to_dict()


def fu(x):
    l=[]
    for i in range(len(x)):
        l.append(cdi[x[i]])
        

    
            
    return l
def fu1(x):
    return(adi[x])
    
            
cl['id']=cl[2].apply(lambda x:fu(x))


cl['aid']=cl[0].apply(lambda x:fu1(x))
cl=cl.drop([0,1,2],axis=1)
cols = cl.columns.tolist()
cols.insert(1, cols.pop(cols.index('id')))
cl = cl.reindex(columns= cols)
cl=cl.groupby('aid',as_index=False).agg({'id':'sum'})

#c=c.groupby(['aid']).agg({'id': lambda x: ",".join(x)},axis=1).reset_index()
cl['id']=cl['id'].apply(lambda x:x+['C0001'])
cl['id']=cl['id'].apply(lambda x:sorted(x))


dic={'aid':['A1211','A1232','A1601','A3254','A3850','A4546'],'id':[['C0001'],['C0001'],['C0001'],['C0001'],['C0001'],['C0001']]}
df2=pd.DataFrame(dic)
df3=pd.concat([cl,df2],ignore_index=True)
df3.sort_values(by=['aid'],inplace=True)

def acon(x):
    x=x.replace('A','')
    x=int(x)-1
    
    return x

df3['aid']=df3['aid'].apply(lambda x:acon(x))


amc=df3['id']
amc.index=df3['aid']
amc=amc.to_dict()

c['s']=c['s'].apply(lambda x:amc[x])
c['d']=c['d'].apply(lambda x:amc[x])

def perm(u,v):
    l=[]
    for i in range(len(u)):
        for j in range(len(v)):
            l.append([u[i],v[j]])
    return l
            
c['pair']=c.apply(lambda x:perm(x['s'],x['d']),axis=1)

listf=[]
def splitpair(x,count):
    for i in x:
        listf.append([i,count])
    
c.apply(lambda x:splitpair(x['pair'],x['wo']),axis=1)


listfsp=[]
def splitpairsp(x,count):
    for i in x:
        listfsp.append(int(count))
        
c.apply(lambda x:splitpairsp(x['pair'],x['path']),axis=1)


dataf=pd.DataFrame(listf)
dataf['sp']=listfsp

dataf=dataf.rename(columns={0:'sd',1:'hum'})
dataf['source']=dataf['sd'].apply(lambda x:x[0])
dataf['dest']=dataf['sd'].apply(lambda x:x[1])
dataf=dataf.drop(['sd'],axis=1)
dataf.sort_values(by=['source','dest'],inplace=True)
dataf=dataf.groupby(['source','dest'],as_index=False).agg({'hum':np.mean,'sp':np.mean})
dataf['ratio']=dataf.apply(lambda x:round(x['hum']/x['sp'],3),axis=1)
dataf=dataf.drop(['hum','sp'],axis=1)

dataf=dataf.rename(columns={'source':'From_Category','dest':'To_Category','ratio':'Ratio_of_human_to_shortest'})
dataf.to_csv("category-ratios.csv",index=False)