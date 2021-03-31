from tkinter import *

root = Tk()
variables = []
entries = []

for i in range(2):
    va = StringVar()
    en = Entry(root, textvariable=va)
    en.grid(row=1, column=i)
    c  = va.get()
    variables.append(c)
    entries.append(en)

def hallo():

    labl = Label(text=variables).grid(row=30,column=30)
    print(variables)

button=Button(root,text="print",command=hallo).grid(row=12,column=0)

root.mainloop()
