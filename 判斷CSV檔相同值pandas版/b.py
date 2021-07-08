import pandas as pd
import numpy as np
a=pd.read_csv("AFINN-111_V5.csv",header=None)
a[0]=a[0].str.strip()
o=a[0].values
o1=a[1].values
AFI=[]
while len(o)!=0:
    an=o[0]
    an1=o1[0]
    o=np.delete(o,0)
    o1=np.delete(o1,0)
    if an in o:
        AFI.append([an,an1])
if len(AFI)==0:
    print('沒有相同的')
else:
    df=pd.DataFrame(AFI)
    df.to_csv("ans1.csv",index=False,header=None)
