import pandas as pd
import tkinter as tk
from tkinter import font
import random
import numpy as np

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
Second_grade_1=tk.Label(window,text="抽出你的直屬學長、姐",fg='#000000',font=('微軟正黑體',35),padx=30,pady=20)
Second_grade_2=tk.Label(window,text="",fg='#000000',font=('微軟正黑體',35),padx=30,pady=20)
First_grade_1.pack()
First_grade_2.pack()
Second_grade_1.pack()
Second_grade_2.pack()



def nextu():
    result.append([First_grade[0],Senpai])
    First_grade_2['text']=" "
    First_grade=First_grade.pop(0)
    print(First_grade)
    First_grade_2['text']=First_grade[0]
    
    
def dlots():
    rid=random.randint(0,len(Second_grade))
    Senpai=Second_grade[rid]
    Second_grade_2['text']=Senpai
    Second_grade.remove(Senpai)
    



nextbutton=tk.Button(window,text="下一位",fg='#000000',font=("微軟正黑體",25,font.BOLD),command=nextu)
nextbutton.pack(side="left",ipadx=40, padx=40)
lots=tk.Button(window,text='抽籤',fg="#000000",font=("微軟正黑體",25,font.BOLD),command=dlots)
lots.pack(side='left', ipadx=40, padx=40)
nulln=tk.Button(window,text='缺席',fg="#000000",font=("微軟正黑體",25,font.BOLD))
nulln.pack(side='left',ipadx=40, padx=40)






window.mainloop()