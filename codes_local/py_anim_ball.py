import time

from tkinter import*

screen=Tk()
drawingboard=Canvas(screen,width =400,height=400,bg='white' )
drawingboard.pack()
ball1=drawingboard.create_oval(10,20,30,40,fill='red')
ball2=drawingboard.create_oval(10,20,30,40,fill='blue')
ball3=drawingboard.create_oval(10,20,30,40,fill='green')

x=5
y=3
a=2
b=-5
p=2
q=-7

while True:
    
    drawingboard.move(ball1,x,y)
    drawingboard.move(ball2,a,b)
    drawingboard.move(ball3,p,q)
    destiny=drawingboard.coords(ball3)
    if destiny[1]>=400:
        q=-q*0.5
    if destiny[1]<=0:
        q=-q*0.5
    if destiny[2]>=400:
        p=-p*0.5
    if destiny[2]<=0:
        p=-p*0.5
    
    place=drawingboard.coords(ball2)
    if place[1]>=400:
        b=-b*0.5
    if place[1]<=0:
        b=-b*0.5
    if place[2]>=400:
        a=-a*0.5
    if place[2]<=0:
        a=-a*0.5
   
    
    position=drawingboard.coords(ball1)
    if position[2]>=400:
        x=-x*0.5    
    if position[2]<=0:
        x=-x*0.5
    if position[1]>=400:
        y=-y*0.5
    if position[1]<=0:
        y=-y*0.5

   
    
    screen.update()
    time.sleep(0.02)



    
    
screen.mainloop()
