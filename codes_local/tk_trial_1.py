from tkinter import *
import numpy as np

a=np
b=Tk()

b.title("hey")

array1=np.zeros(2,dtype=str)

def hj():
    for i in range(2):
        va=StringVar()

        en=Entry(b,textvariable=va).grid(row=1,column=2+i)
        vb=va.get()
        np.append(array1,vb)
        txt = en.get()
        print(txt)

def hjk():
    
       lbl=Label(b,text=np.array_str(array1)).grid(row=3,column=3)
        
    
btn=Button(b,text="hey",command=hj).grid(row=1,column=1)

bty=Button(b,text="Print",command=hjk).grid(row=1,column=30)
