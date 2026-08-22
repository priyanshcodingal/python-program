import turtle

screen = turtle.Screen()
screen.bgcolor("red")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)

turtle.done()
