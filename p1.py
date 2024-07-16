import pandas as pd
import numpy as np
import os
path=os.path.abspath('articles.tsv')
df = pd.read_csv(path,delimiter="\t",header=None)
dict = {x: index for index, x in enumerate(df[0], start=10001)}
df['id']=df[0].map(dict)
df['id']=df['id'].apply(lambda x:'A'+str(x))
df['id']=df['id'].apply(lambda x:str(x[:1]+str(x[2:])))

df=df.rename(columns={0:'Article_Name','id':'Article_ID'})
df.to_csv("article-ids.csv",index=False)