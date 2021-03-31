from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


root=Tk()
root.title("ENGINE DESIGN")
root.geometry("600x600")


##taking no. of inputs
lbl=Label(root,text="no. of values ").grid(row=1,column=1)

va1=IntVar()

array=[]

en1= Entry(root, textvariable=va1,width=10).grid(row=1, column=2)

def hallo():
     array=[va1.get()]
     lbl=Label(root,text=array).grid(row=2,column=2)
    
button=Button(root,text="print",command=hallo,bg="green").grid(row=1,column=3)
lbl=Label(root,text="Entered Value is=").grid(row=2,column=1)
    


##taking inputs for speed of engine in RPM
va2=[]
en2=[]

def hi2():
    for i in range(va1.get()):
        va2.append(IntVar())
        en2.append(Entry(root,textvariable=va2[i],width=10).grid(row=4+i,column=1))
        
btn=Button(root,text="SPEED VALUES",command=hi2).grid(row=3,column=1)

array2=[]
def print2():
     array2=[]
     for i in range(va1.get()):
              array2.append(va2[i].get())
    
     lb=Label(text=array2).grid(row=4,column=2)






## takin inputs for torque for accelaration position of 100%
va3=[]
en3=[]

def hi3():
    for i in range(va1.get()):
        va3.append(IntVar())
        en3.append(Entry(root,textvariable=va3[i],width=10).grid(row=4+i,column=5))
        
btn=Button(root,text="torque values for 100% accelaration",command=hi3).grid(row=3,column=5)

lbl=Label(root,text="Entered Values are=").grid(row=3,column=51+va1.get())

array3=[]
def print3():
     for i in range(va1.get()):
              array2.append(va2[i].get())
    
              lb=Label(text=array2[i]).grid(row=3,column=51+i+va1.get())

     for i in range(va1.get()):
              array3.append(va3[i].get())

              lb=Label(text=array3[i]).grid(row=4,column=51+i+va1.get())


brn=Button(root,text="PRINT",command=print3,bg="green").grid(row=5,column=50+va1.get())






#plotting the tabel
def plot1():
     labl=Label(text="speed").grid(row=50+va1.get(),column=1)
     for i in range(va1.get()):
            array2.append(va2[i].get())
            lb=Label(text=array2[i]).grid(row=25+i+va1.get(),column=2)
            
            array3.append(va3[i].get())
            lb=Label(text=array3[i]).grid(row=25+i+va1.get(),column=10)

            lb=Label(text=array3[i]*.05).grid(row=25+i+va1.get(),column=3)
            lb=Label(text=array3[i]*.1).grid(row=25+i+va1.get(),column=4)
            lb=Label(text=array3[i]*.2).grid(row=25+i+va1.get(),column=5)
            lb=Label(text=array3[i]*.3).grid(row=25+i+va1.get(),column=6)
            lb=Label(text=array3[i]*.4).grid(row=25+i+va1.get(),column=7)
            lb=Label(text=array3[i]*.5).grid(row=25+i+va1.get(),column=8)
            lb=Label(text=array3[i]*.6).grid(row=25+i+va1.get(),column=9)



           
     lbl=Label(text="5%").grid(row=21  ,column=3  )
     lbl=Label(text="10%").grid(row= 21 ,column= 4 )
     lbl=Label(text="20%").grid(row=21  ,column= 5 )
     lbl=Label(text="30%").grid(row= 21 ,column= 6 )
     lbl=Label(text="40%").grid(row= 21 ,column= 7 )
     lbl=Label(text="50%").grid(row= 21 ,column= 8 )
     lbl=Label(text="60%").grid(row= 21 ,column= 9 )
     lbl=Label(text="100%").grid(row= 21 ,column= 10 )

btn=Button(text="TABEL",command=plot1).grid(row=5,column=51+va1.get())

def plot2():
     
    array4=[5,10,20,30,40,50,60,100]

    data=[array4,array3,array2]

    x, y, z = zip(*data)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.bar(x,y,z)
    plt.show()



btn=Button(text="graph",command=plot2).grid(row=8,column=51+va1.get())
    
root.mainloop()
