import turtle
import Tkinter as TK
import _tkinter

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("red")

    george = turtle.Turtle()
    george.shape("turtle")
    george.color("yellow")
    george.speed(2)
    draw_square(george)

    i = 1
    while i<72:
        george.right(5)
        draw_square(george)
        i+=1

    window.exitonclick()

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

draw_shapes()
