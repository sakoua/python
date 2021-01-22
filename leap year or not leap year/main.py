for q in range(2):
    with open('in' + str(q + 1) + '.txt', mode='r') as s:
        d=eval(s.readline())
        if (d % 4==0 and d%100!=0 or d%400==0):
            print(str(d)+" is a leap year")
        else:
            print(str(d) + " is a not leap year")
