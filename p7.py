import pandas as pd
import numpy as np
import os
path=os.path.abspath('finished-paths-back.csv')

w = pd.read_csv(path)

path2=os.path.abspath('finished-paths-no-back.csv')
wo = pd.read_csv(path2)
h=list(w['Human_Path_Length'])
s=list(w['Shortest_Path_Length'])

ce=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
c10=0
c11=0
for i in range(len(h)) :
    if((h[i]-s[i])==0):
        ce+=1
    elif((h[i]-s[i])==1):
        c1+=1
    elif((h[i]-s[i])==2):
        c2+=1
    elif((h[i]-s[i])==3):
        c3+=1
    elif((h[i]-s[i])==4):
        c4+=1
    elif((h[i]-s[i])==5):
        c5+=1
    elif((h[i]-s[i])==6):
        c6+=1
    elif((h[i]-s[i])==7):
        c7+=1
    elif((h[i]-s[i])==8):
        c8+=1
    elif((h[i]-s[i])==9):
        c9+=1
    elif((h[i]-s[i])==10):
        c10+=1
    elif((h[i]-s[i])>=11):
        c11+=1
        
lis=[]
lis.append(round((((ce)/len(h))*100),3))
lis.append(round((((c1)/len(h))*100),3))
lis.append(round((((c2)/len(h))*100),3))
lis.append(round((((c3)/len(h))*100),3))
lis.append(round((((c4)/len(h))*100),3))
lis.append(round((((c5)/len(h))*100),3))
lis.append(round((((c6)/len(h))*100),3))
lis.append(round((((c7)/len(h))*100),3))
lis.append(round((((c8)/len(h))*100),3))
lis.append(round((((c9)/len(h))*100),3))
lis.append(round((((c10)/len(h))*100),3))
lis.append(round((((c11)/len(h))*100),3))
        
pw=pd.DataFrame(lis)
pw=pw.T

h2=list(wo['Human_Path_Length'])
s2=list(wo['Shortest_Path_Length'])
ce=0
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
c10=0
c11=0
for i in range(len(h2)) :
    if((h2[i]-s2[i])==0):
        ce+=1
    elif((h2[i]-s2[i])==1):
        c1+=1
    elif((h2[i]-s2[i])==2):
        c2+=1
    elif((h2[i]-s2[i])==3):
        c3+=1
    elif((h2[i]-s2[i])==4):
        c4+=1
    elif((h2[i]-s2[i])==5):
        c5+=1
    elif((h2[i]-s2[i])==6):
        c6+=1
    elif((h2[i]-s2[i])==7):
        c7+=1
    elif((h2[i]-s2[i])==8):
        c8+=1
    elif((h2[i]-s2[i])==9):
        c9+=1
    elif((h2[i]-s2[i])==10):
        c10+=1
    elif((h2[i]-s2[i])>=11):
        c11+=1

lis=[]
lis.append(round((((ce)/len(h))*100),3))
lis.append(round((((c1)/len(h))*100),3))
lis.append(round((((c2)/len(h))*100),3))
lis.append(round((((c3)/len(h))*100),3))
lis.append(round((((c4)/len(h))*100),3))
lis.append(round((((c5)/len(h))*100),3))
lis.append(round((((c6)/len(h))*100),3))
lis.append(round((((c7)/len(h))*100),3))
lis.append(round((((c8)/len(h))*100),3))
lis.append(round((((c9)/len(h))*100),3))
lis.append(round((((c10)/len(h))*100),3))
lis.append(round((((c11)/len(h))*100),3))
pwo=pd.DataFrame(lis)
pwo=pwo.T

pw=pw.rename(columns={0:'Equal_Length',1:'Larger_by_1',2:'Larger_by_2',
                      3:'Larger_by_3',4:'Larger_by_4',5:'Larger_by_5',
                      6:'Larger_by_6',7:'Larger_by_7',8:'Larger_by_8',
                      9:'Larger_by_9',10:'Larger_by_10',
                      11:'Larger_by_more_than_10'})
                      
                      
pwo=pwo.rename(columns={0:'Equal_Length',1:'Larger_by_1',2:'Larger_by_2',
                      3:'Larger_by_3',4:'Larger_by_4',5:'Larger_by_5',
                      6:'Larger_by_6',7:'Larger_by_7',8:'Larger_by_8',
                      9:'Larger_by_9',10:'Larger_by_10',
                      11:'Larger_by_more_than_10'})               
                      


                      
pw.to_csv("percentage-paths-back.csv",index=False)
pwo.to_csv("percentage-paths-no-back.csv",index=False)
