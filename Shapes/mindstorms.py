import turtle
import _tkinter

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    george = turtle.Turtle()
    george.forward(100)

    window.exitonclick()

draw_square()
