import turtle as t

t.speed(0)
t.bgcolor('white')
t.pencolor('purple')
def square(x,y):
    for j in range(42):
        t.forward(x)
        t.right(y)
for i in range(80):
    square(170,90)
    t.right(52)
    t.circle(50)
    t.right(50)
    t.hideturtle()
    t.done()

    # We can also do graphics and drawings with the help of python as we did through microsoft logo.
    # We have to select the color of the pen and tell it the directions to move