def namech():
    global inpval
    inpval=input("要處裡的資料:")
    
inpval=""
while True:
    typ=input("請輸入需要遮罩的類型:")
    if typ=="姓名":
        namech()
    if typ=="quit":
        break