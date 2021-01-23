with open('C://Users/Tina/desktop/python/pyd108/in1.txt',mode='r') as s:
    o=list()
    while True:
        line=s.readline()
        if not line:
            break
        else:
            o.append(eval(line))
    d=((o[2]-o[0])**2+(o[3]-o[1])**2)**0.5
    print("("+str(o[0])+"，"+str(o[1])+")")
    print("("+str(o[2])+"，"+str(o[3])+")")
    print("Distance = "+str(round(d,4)))

