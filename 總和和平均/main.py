for q in range(2):
    with open('in'+str(q+1)+'.txt',mode='r') as s:
        o=list()
        while True:
            line = s.readline()
            if not line:
                break
            else:
                o.append(eval(line))
                su=sum(o)
        print(*o)
        print("Sum = " + str(float(su)))
        print("Average = " + str(round(su/len(o),1)))
        print()
