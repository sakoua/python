with open("in1.txt",mode="r") as s:
    a=eval(s.readline())
    if(a>=80 and a<=100):
        print("A")
    elif(a>=70):
        print("B")
    elif(a>=60):
        print("C")
    else:
        print("D")