c=list(map(int,input().split()))
for aaa in range(int(input())):
    a=0;b=0
    x=list(map(int,input().split()))
    ans=c.copy()
    for i in range(4):
        if ans[i]==x[i]:
            a+=1
            ans[i]=111
            x[i]=222
    
    for i in range(4):
        if x[i] in ans:
            b+=1
            ans[ans.index(x[i])]=444
            x[i]=333
    print("{0}A{1}B".format(a,b))