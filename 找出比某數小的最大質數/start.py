import math
for q in range(2):
    f = open(f'./in{str(q+1)}.txt')
    b = f.readline()
    for i in range(int(b)):
        a = f.readline()
        for o in range(int(a)-1, 1, -1):
            d = True
            for c in range(2, int(math.sqrt(o))):
                if int(o) % int(c) == 0:
                    d = False
                    continue
            if d == True:
                print(o)
                break
    print(" ")
