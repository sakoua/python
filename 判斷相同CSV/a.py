import pandas as pd
import csv
f=open('AFINN-111_V5.csv',mode='r',encoding='utf8')
a=csv.reader(f)
fi=list(a)
li=[[],[]]
for i in range(len(fi)): 
    li[0].append(fi[i][0].strip())
    li[1].append(fi[i][1].strip())
fi=[]
while len(li[0])!=0:
    an=li[0][0]
    an1=li[1][0]
    li[0].pop(0)
    li[1].pop(0)
    if an in li[0]:
        fi.append([an,an1])
if len(fi[0])==0:
    print('沒有相同的')
else:
    df=pd.DataFrame(fi)
    df.to_csv("ans.csv",index=False,header=None)
