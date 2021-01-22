ma={"+","-","*","/","//","%"}
with open("in1.txt",mode="r") as s:
    o=list()
    while True:
        line=s.readline()
        if not line:
            break
        else:
            if line in ma:
                if(line=="+"):
                    print(o[0]+o[1])
                elif(line=='-'):
                    print(o[0] - o[1])
                elif(line=='*'):
                    print(o[0] * o[1])
                elif(line=='/'):
                    print(o[0] / o[1])
                elif(line=='//'):
                    print(o[0] // o[1])
                else:
                    print(o[0]%o[1])
            else:
                o.append(eval(line))