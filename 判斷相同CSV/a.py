import pandas as pd
import csv
f=open('AFINN-111_V5.csv',mode='r',encoding='utf8')
a=csv.reader(f)
fi=list(a)
li=[[],[]]
fli=[[],[]]
for i in range(len(fi)):
    li[0].append(fi[i][0].strip())
    li[1].append(fi[i][1].strip())
fi=fi.clear()
while len(li[0])!=0:
    an=li[0][0]
    an1=li[1][0]
    li[0].pop(0)
    li[1].pop(0)
    if an in li:
        fli[0].append(an)
        fli[1].append(an1)
if len(fli[0])==0:
    print('沒有相同的')
else:
    df=pd.DataFrame(fli)
    df.to_csv("ans.csv")
