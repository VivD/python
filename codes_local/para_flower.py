import turtle

def draw_para(some_turtle):    
    for i in range (0, 2):                    
        some_turtle.forward(250)
        some_turtle.right(130)
        some_turtle.forward(250)
        some_turtle.right(50)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    
    brad = turtle.Turtle()
    brad.color("yellow")
    brad.shape("turtle")
    brad.speed(5000)
    for n in range (1, 61):
        draw_para(brad)
        brad.right(360/60)

    brad.right(90)
    brad.forward(500)
        
    window.exitonclick()

draw_art()
