a=eval(input("請輸入小於100的數字:"))
for i in range(1,a+1):
    for o in range(i):
        print("{:>4}".format((o+1)*i),end="")
    if i !=a:
        print("")