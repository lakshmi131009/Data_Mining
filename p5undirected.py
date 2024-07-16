import pandas as pd
import numpy as np
import networkx as nx
f=open("shortest-path-distance-matrix.txt","r")
content=f.read()
colist=content.split("\n")
a=[]
for l in colist:
    
    
    b=[]
    for c in l:
        
         b.append(c)
    
    a.append(b)

m=[[0 for i in range(4604)] for j in range(4604)]

for i in range(4604):
    for j in range(4604):
         if a[i][j]=='1':
                
                m[i][j]=1
                m[j][i]=1
                

                
di={}
for i in range(len(m)):
    b=[]
    for j in range(len(m)):
        if(m[i][j]==1):
            b.append(j)
    di[i]=b
            
df=pd.DataFrame(columns=["Nodes","Edges"])


G=nx.Graph()
G.add_nodes_from(range(0,4604))

for i in range(4604):
    for j in range(4604):
        if(m[i][j]==1):
            G.add_edge(i,j)
        
import sys
sys.setrecursionlimit(5000)


color={}
parent={}
trav_time={}
dfs_traversal_output=[]

for node in di.keys():
    color[node]="W"
    parent[node]=None
    trav_time[node]=[-1,-1]

time=0
cou=0
c=0
comp=[]
edges=[]
def dfs_util(u):
    global time
    
    
    color[u]="G"
    
    trav_time[u][0]=time
    dfs_traversal_output.append(u)
    time+=1
    
    for v in di[u]:
        if color[v]=="W":
            
            parent[v]=u
            dfs_util(v)
    color[u]="B"
    trav_time[u][1]=time
    time+=1


for i in range(4604):
    if(color[i]=='W'):
        
        dfs_util(i)
        
        for i in range(len(dfs_traversal_output)):
            k=dfs_traversal_output[i]
            for j in range(len(dfs_traversal_output)):
                l=dfs_traversal_output[j]
                
                if(m[k][l]==1):
                    c+=1
        #print(len(dfs_traversal_output),int(c/2))
        comp.append(len(dfs_traversal_output))
        edges.append(int(c/2))
        
        dfs_traversal_output=[]
        c=0
        
        
        cou+=1
        
df["Nodes"]=comp
df["Edges"]=edges
dia=[]
cc=nx.connected_components(G)

for i in cc:
    sb=G.subgraph(i)
    dia.append(nx.diameter(sb,e=None,usebounds=False))
df["Diameter"]=dia
df.to_csv("graph-components-undirected.csv",index=False)