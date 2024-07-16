import pandas as pd
import numpy as np
import networkx as nx

import os
path=os.path.abspath('shortest-path-distance-matrix.txt')

f=open(path,"r")
content=f.read()
colist=content.split("\n")
a=[]
for l in colist:
    
    
    b=[]
    for c in l:
        
         b.append(c)
    
    a.append(b)

              

            
df=pd.DataFrame(columns=["Nodes","Edges","Diameter"])


G=nx.DiGraph()
G.add_nodes_from(range(0,4604))

for i in range(4604):
    for j in range(4604):
        if(a[i][j]=='1'):
            G.add_edge(i,j)
        
ed=[]
nodes=[]
dia=[]

cc=nx.kosaraju_strongly_connected_components(G)

for i in cc:
    sb=G.subgraph(i)
    nodes.append(sb.number_of_nodes())
    ed.append(sb.number_of_edges())
    dia.append(nx.diameter(sb,e=None,usebounds=False))
    
df["Nodes"]=nodes
df["Edges"]=ed
df["Diameter"]=dia
df.to_csv("graph-components.csv",index=False)