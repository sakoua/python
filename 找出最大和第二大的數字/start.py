for q in range(2):
    with open('in'+str(q+1)+'.txt', mode='r') as s:
        for w in range(int(s.readline())):
            b = s.readline()
            a = b.split()
            x = list()

            for i in a:
                if int(i) not in x:
                    x.append(int(i))
            x.sort()
            x.reverse()
            if len(x) == 1:
                print(str(x[0])+" "+str(x[0]))
            else:
                print(str(x[0])+" "+str(x[1]))
    print(' ')
