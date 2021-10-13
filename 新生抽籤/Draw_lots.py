import pandas as pd
import tkinter as tk
from tkinter import  font
import random
import numpy as np
from tkinter import messagebox
a=pd.read_csv("Draw_lots.csv",header=None)
First_grade=a[0].values
Second_grade=a[1].values
window = tk.Tk()
window.title('新生和學長姐相見歡')
window.geometry('800x800')
result=[]
Senpai="null"
First_grade_1 = tk.Label(window, text='學弟、妹',bg="#F0FF66",width=800, fg='#540AFF', font=('微軟正黑體', 40,font.BOLD),padx=30,pady=20)
First_grade_2 = tk.Label(window, text=f'{First_grade[0]}',fg='#000000', font=('微軟正黑體', 35),padx=30,pady=20)
Second_grade_1=tk.Label(window,text="抽出你的直屬學長、姐",bg="#F0FF66",width=800, fg='#540AFF',font=('微軟正黑體',35,font.BOLD),padx=30,pady=20)
Second_grade_2=tk.Label(window,text="",fg='#000000',font=('微軟正黑體',35),padx=30,pady=20)
First_grade_1.pack()
First_grade_2.pack()
Second_grade_1.pack()
Second_grade_2.pack()



def nextu():
    global result,First_grade,Senpai
    if Senpai=="null" or Senpai=="":
        messagebox.showwarning('警告', f'新生:{First_grade[0]} 還沒抽直屬學長')
    else:
        result.append([First_grade[0],Senpai])
        First_grade_2['text']=" "
        First_grade=np.delete(First_grade,0)
        if len(First_grade)==0:
            finsh()
        else:
            First_grade_2['text']=First_grade[0]
            Second_grade_2["text"]=""
            Senpai="null"
    
    
def dlots():
    global Senpai,Second_grade
    if Senpai =="null":
        rid=random.randint(0,(len(Second_grade)-1))
        Senpai=Second_grade[rid]
        Second_grade_2['text']=Senpai
        Second_grade=np.delete(Second_grade,rid)
    else:
         messagebox.showwarning('警告', f'新生:{First_grade[0]} 已抽直屬學長了')

def not_here():
    global Senpai,First_grade
    Msgbox=tk.messagebox.askquestion("警告",f"新生:{First_grade[0]}，今日確定缺席嗎?")
    if Msgbox=="yes":
        Senpai='缺席'
        result.append([First_grade[0],Senpai])
        Senpai='null'
        First_grade_2['text']=" "
        First_grade=np.delete(First_grade,0)
        if len(First_grade)==0:
            finsh()
        else:
            First_grade_2['text']=First_grade[0]
            Second_grade_2["text"]=""
            Senpai="null"


def finsh():
    MsgBox = tk.messagebox.askquestion('訊息','已經全部新生都抽完了，將自動新建名為:直屬學長')
    if MsgBox == 'yes':
        col=["一年級","直屬學長"]
        df=pd.DataFrame(result,columns=col)
        df.to_excel("直屬學長.xlsx",index=False,encoding="urf8",sheet_name='新生直屬學長抽籤結果')
        MsgBox2=tk.messagebox.askquestion("通知","檔案已建立完成")
        if MsgBox2 == "yes":
            window.destroy()





nextbutton=tk.Button(window,text="下一位",fg='#000000',font=("微軟正黑體",25,font.BOLD),command=nextu)
nextbutton.pack(side="left",ipadx=40, padx=40)
lots=tk.Button(window,text='抽籤',fg="#000000",font=("微軟正黑體",25,font.BOLD),command=dlots)
lots.pack(side='left', ipadx=40, padx=40)
nulln=tk.Button(window,text='缺席',fg="#000000",font=("微軟正黑體",25,font.BOLD),command=not_here)
nulln.pack(side='left',ipadx=40, padx=40)






window.mainloop()