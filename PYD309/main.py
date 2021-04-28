with open("in1.txt",mode="r") as s:
    li=list()
    while True:
        line=s.readline()
        if not line:
            break
        else:
            li.append(eval(line))
    o=li[0]
    print("Month    Amount")
    for i in range(li[2]):
        o=round(o+o*li[1]/1200,2)
        print(str(i+1)+"  "+str(o))