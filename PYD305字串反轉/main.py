for q in range(2):
    with open("in"+str(q+1)+".txt",mode='r') as s:
        a=list(str(s.readline()))
        a.reverse()
        print("".join(a))
    print()