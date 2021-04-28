for q in range(2):
    with open("in"+str(q+1)+".txt",mode='r') as s:
        a=eval(s.readline())
        for i in range(a):
            o=""
            for w in range(a):
                d=(w+1)*(i+1)
                o+=str(w+1)+"*"+str(i+1)+"="+str(d)+" "
            print(o)
        print()