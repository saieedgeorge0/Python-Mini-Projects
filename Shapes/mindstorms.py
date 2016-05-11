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

    for i in range(1:5):
        george.forward(100)
        george.right(90)

    mary = turtle.Turtle()
    mary.shape("arrow")
    mary.color("blue")
    mary.circle(100)

    window.exitonclick()

draw_shapes()
