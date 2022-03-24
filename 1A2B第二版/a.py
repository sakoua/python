output = open("out.txt", mode='w')
for i in range(1, 3):
    with open(f"in{i}.txt", mode='r') as n:
        finans=list(map(int,n.readline().split()))
        for q in range(eval(n.readline())):
            tt=list(map(int,n.readline().split()))
            a,b=0,0
            visited,visitedid=[],[]
            for i,(x,y) in enumerate(zip(finans,tt)):
                if x==y:
                    a+=1
                    visited.append(x)
                    visitedid.append(i)
            for i in visited:
                tt.remove(i)
            for i,itme in enumerate(finans):
                if i in visitedid:
                    continue
                if itme in tt:
                    b+=1
            print(f"{a}A{b}B",file=output)
        print(" ",file=output)