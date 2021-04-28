for q in range(2):
    with open("in"+str(q+1)+".txt",mode='r') as s:
        o=list()
        while True:
            line=s.readline()
            if not line:
                break
            else:
                o.append(eval(line))
        if(o[0]+o[1]>o[2] and o[0]>abs(o[1]-o[2])):
            print(sum(o))
        else:
            print("Invalid")
        print()