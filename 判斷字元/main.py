import re
for q in range(3):
    with open("in"+str(q+1)+".txt",mode='r') as s:
        a=s.readline()
        if(re.search("\W",a)==None):
            if(str.isdigit(a)==True):
                print(str(a)+" is a number.")
            else:
                print(str(a) + " is an alphabet.")
        else:
            print(str(a) + " is a symbol.")
    print()