for q in range(2):
    with open("in"+str(q+1)+".txt",mode='r') as s:
                print('{:x}'.format(eval(s.readline())))
    print()