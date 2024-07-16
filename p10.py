import pandas as pd
import numpy as np
import csv
import networkx as nx
import itertools
import os
path=os.path.abspath('paths_unfinished.tsv')

t=open(path)
c=pd.read_csv(t,delimiter='\t',header=None)
c = c.drop([0,1,2,5],axis=1)
c[3]=c[3].apply(lambda x:x.split(';'))
c[3]=c[3].apply(lambda x:x[0])


patha=os.path.abspath('article-ids.csv')
arti=pd.read_csv(patha,header=None)



adi=arti[1]
adi.index=arti[0]
adi=adi.to_dict()

c.replace(to_replace="Long_peper",value="Long_pepper",inplace=True)
c.replace(to_replace="Adolph_Hitler",value="Adolf_Hitler",inplace=True)
c.replace(to_replace="_Zebra",value="Zebra",inplace=True)
c.replace(to_replace="Fats",value="Fatty_acid",inplace=True)
c.replace(to_replace="Podcast",value="podcasting",inplace=True)

def convert(x):
    if(x not in adi.keys()):
        return '666666'
    else:
        return adi[x]
    
c['si']=c[3].apply(lambda x:adi[x])
c['di']=c[4].apply(lambda x:convert(x))

c=c.drop([3,4],axis=1)



pathc=os.path.abspath('categories.tsv')
tk=open(pathc)
ck=pd.read_csv(tk,delimiter='\t',header=None)
ck[1]=ck[1].apply(lambda x:x.split('.'))

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
    
ck[2]=ck[1].apply(lambda x:func(x))

pathcat=os.path.abspath('category-ids.csv')
cati=pd.read_csv(pathcat,header=None)


cdi=cati[1]
cdi.index=cati[0]
cdi=cdi.to_dict()




def fu(x):
    l=[]
    for i in range(len(x)):
        l.append(cdi[x[i]])
        

    #l.append('C0001')
            
    return l
def fu1(x):
    return(adi[x])
    
            
ck['id']=ck[2].apply(lambda x:fu(x))


ck['aid']=ck[0].apply(lambda x:fu1(x))
ck=ck.drop([0,1,2],axis=1)
cols = ck.columns.tolist()
cols.insert(1, cols.pop(cols.index('id')))
ck = ck.reindex(columns= cols)
ck=ck.groupby('aid',as_index=False).agg({'id':'sum'})

#c=c.groupby(['aid']).agg({'id': lambda x: ",".join(x)},axis=1).reset_index()
ck['id']=ck['id'].apply(lambda x:x+['C0001'])
ck['id']=ck['id'].apply(lambda x:sorted(x))


dic={'aid':['A1211','A1232','A1601','A3254','A3850','A4546'],'id':[['C0001'],['C0001'],['C0001'],['C0001'],['C0001'],['C0001']]}
df2=pd.DataFrame(dic)
df3=pd.concat([ck,df2],ignore_index=True)
df3.sort_values(by=['aid'],inplace=True)

amc=df3['id']
amc.index=df3['aid']
amc=amc.to_dict()
c['csi']=c['si'].apply(lambda x:amc[x])
def getdes(x):
    if(x=='666666'):
        return ['C0001']
    else:
        return amc[x]
    
c['cdi']=c['di'].apply(lambda x:getdes(x))
c=c.drop(['si','di'],axis=1)

l=[]
def perm(u,v):
    for i in range(len(u)):
        for j in range(len(v)):
            l.append([u[i],v[j]])
            
c.apply(lambda x:perm(x['csi'],x['cdi']),axis=1)    

l.sort()
finlis=list(l for l,_ in itertools.groupby(l))

tf=open('paths_finished.tsv')
cf=pd.read_csv(tf,delimiter='\t',header=None)
cf = cf.drop([0,1,2,4],axis=1)
cf[3]=cf[3].apply(lambda x:x.split(';'))

cf['T']=cf[3].apply(lambda x:  len(x)==1)
cf['T']=cf['T'].astype(str)
cf = cf[~cf["T"].str.contains('True')]
cf=cf.drop(['T'],axis=1)

cf['fsi']=cf[3].apply(lambda x:x[0])
cf['fdi']=cf[3].apply(lambda x:x[len(x)-1])
cf = cf.drop([3],axis=1)

cf['fsi']=cf['fsi'].apply(lambda x:adi[x])
cf['fdi']=cf['fdi'].apply(lambda x:adi[x])

cf['fsi']=cf['fsi'].apply(lambda x:amc[x])
cf['fdi']=cf['fdi'].apply(lambda x:amc[x])
l=[]
cf.apply(lambda x:perm(x['fsi'],x['fdi']),axis=1)

l.sort()
unfinlis=list(l for l,_ in itertools.groupby(l))


mer=finlis+unfinlis

it=set(tuple(x) for x in mer)

mapfin={}
mapunfin={}
for i in it:
    mapfin[i]=0
    mapunfin[i]=0



def fingetpermco(u,v):
    for i in range(len(u)):
        for j in range(len(v)):
            
            p=u[i]
            q=v[j]
            s=(p,q)
            mapfin[s]+=1
    

def unfingetpermco(u,v):
    for i in range(len(u)):
        for j in range(len(v)):
            
            p=u[i]
            q=v[j]
            s=(p,q)
            mapunfin[s]+=1
            

cf.apply(lambda x:fingetpermco(x['fsi'],x['fdi']),axis=1)
c.apply(lambda x:unfingetpermco(x['csi'],x['cdi']),axis=1)
def getlist(dict):
    l=[]
    for key in dict.keys():
        l.append(key)
    return l

pairs=getlist(mapfin)

def getlistval(dict):
    l=[]
    for key in dict.values():
        l.append(key)
    return l

valuesfin=getlistval(mapfin)

valuesunfin=getlistval(mapunfin)

final=pd.DataFrame(pairs)
final['fin']=valuesfin
final['unfin']=valuesunfin
final.sort_values(by=[0,1],inplace=True)
final['perfin']=final.apply(lambda x:round((x['fin']/(x['fin']+x['unfin']))*100,2),axis=1)
final['unperfin']=final.apply(lambda x:round((x['unfin']/(x['fin']+x['unfin']))*100,2),axis=1)
final=final.drop(['fin','unfin'],axis=1)


final=final.rename(columns={0:'From_Category',1:'To_Category','perfin':'Percentage_of_finished_paths','unperfin':'Percentage_of_unfinished_paths'})
final.to_csv("categories-pairs.csv",index=False)



