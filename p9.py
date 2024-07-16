import pandas as pd
import numpy as np
import csv
import networkx as nx
t=open('categories.tsv')
c=pd.read_csv(t,delimiter='\t',header=None)
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
    
            
c['id']=c[2].apply(lambda x:fu(x))


c['aid']=c[0].apply(lambda x:fu1(x))
c=c.drop([0,1,2],axis=1)
cols = c.columns.tolist()
cols.insert(1, cols.pop(cols.index('id')))
c = c.reindex(columns= cols)
c=c.groupby('aid',as_index=False).agg({'id':'sum'})

#c=c.groupby(['aid']).agg({'id': lambda x: ",".join(x)},axis=1).reset_index()
c['id']=c['id'].apply(lambda x:x+['C0001'])
c['id']=c['id'].apply(lambda x:sorted(x))


dic={'aid':['A1211','A1232','A1601','A3254','A3850','A4546'],'id':[['C0001'],['C0001'],['C0001'],['C0001'],['C0001'],['C0001']]}
df2=pd.DataFrame(dic)
df3=pd.concat([c,df2],ignore_index=True)
df3.sort_values(by=['aid'],inplace=True)

def acon(x):
    x=x.replace('A','')
    x=int(x)-1
    
    return x

df3['aid']=df3['aid'].apply(lambda x:acon(x))

acdi=df3['id']
acdi.index=df3['aid']
acdi=acdi.to_dict()

hp={}
hpall={}
sp={}
spall={}

for i in range(1,147):
    cat='C'+str(i).zfill(4)
    hp[cat]=0
    hpall[cat]=0
    sp[cat]=0
    spall[cat]=0

def articalid(x):
    l=[]
    for i in range(len(x)):
        
        for ca in acdi[x[i]]:
            spall[ca]+=1
            if(ca not in l):
                l.append(ca)
                sp[ca]+=1
                
def harticalid(x):
    l=[]
    for i in range(len(x)):
        
        for ca in acdi[x[i]]:
            hpall[ca]+=1
            if(ca not in l):
                l.append(ca)
                hp[ca]+=1
                



tp=open('paths_finished.tsv')
cp=pd.read_csv(tp,delimiter='\t',header=None)
cp = cp.drop([0,1,2,4],axis=1)
cp['data']=cp[3].apply(lambda x:x.split(';'))
cp = cp.drop([3],axis=1)


cp['l']=cp['data'].apply(lambda x:len(x))
cp['T']=cp['data'].apply(lambda x:  len(x)==1)
cp['T']=cp['T'].astype(str)
cp = cp[~cp["T"].str.contains('True')]
cp = cp.drop(['T'],axis=1)

fp=open("shortest-path-distance-matrix.txt","r")
content=fp.read()
colist=content.split("\n")
a=[]
for l in colist:
    
    
    b=[]
    for j in l:
        
         b.append(j)
    
    a.append(b)






G=nx.DiGraph()
G.add_nodes_from(range(0,4604))

for i in range(4604):
    for j in range(4604):
        if(a[i][j]=='1'):
            G.add_edge(i,j)

def func1(x):
    
    li=[]
    co=0
    
    for i in range(len(x)):
        if(x[i]!='<'):
            li.append(x[i])
            co+=1
            
        else:
            li.pop(co-1)
            co-=1
            
            
    return li
    


cp['from']=cp['data'].apply(lambda x:func1(x)) 
cp = cp.drop(['data'],axis=1)
ta=open('articles.tsv')
dfa = pd.read_csv(ta,delimiter="\t",header=None)
dict = {x: index for index, x in enumerate(dfa[0], start=0)}

def f(x):
    li=[]
    for i in range(len(x)):
        li.append(dict[x[i]])
                  
    return li
cp['id']=cp['from'].apply(lambda x:f(x))  
#c = c.drop(['from'],axis=1)
cp=cp.drop(2395)
def cal(s,d):
    return nx.shortest_path(G,s,d)

cp['try']=cp['id'].apply(lambda x:cal(x[0],x[len(x)-1]))
#cp = cp.drop(['from'],axis=1)

kk=cp['try'].apply(lambda x:articalid(x))
kk2=cp['id'].apply(lambda x:harticalid(x))

fin=pd.DataFrame(list(hp.items()))
fin['ha']=pd.DataFrame(list(hpall.values()))
fin['sp']=pd.DataFrame(list(sp.values()))
fin['spall']=pd.DataFrame(list(spall.values()))


fin=fin.rename(columns={0:'Category_ID',1:'Number_of_human_paths_traversed','ha':'Number_of_human_times_traversed',
                        'sp':'Number_of_shortest_paths_traversed',
                        'spall':'Number_of_shortest_times_traversed'
                       })

cols = fin.columns.tolist()
cols.insert(4, cols.pop(cols.index('Number_of_shortest_paths_traversed')))

fin = fin.reindex(columns= cols)
cols = fin.columns.tolist()
cols.insert(4, cols.pop(cols.index('Number_of_shortest_times_traversed')))

fin = fin.reindex(columns= cols)
fin.to_csv('category-subtree-paths.csv',index=False)
