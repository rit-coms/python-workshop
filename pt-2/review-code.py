import turtle as t

SIDE_LENGTH = 50


def draw_square():
    t.forward(SIDE_LENGTH)
    t.right(90)
    t.forward(SIDE_LENGTH)
    t.right(90)
    t.forward(SIDE_LENGTH)
    t.right(90)
    t.forward(SIDE_LENGTH)
    t.right(90)


def draw_square2(side_length):
    t.forward(side_length)
    t.right(90)
    t.forward(side_length)
    t.right(90)
    t.forward(side_length)
    t.right(90)
    t.forward(side_length)
    t.right(90)


def draw_square3(side_length):
    for i in range(4):
        t.forward(side_length)
        t.right(90)


def draw_square4(side_length):
    i = 0
    while i < 4:
        t.forward(side_length)
        t.right(90)
        i += 1  # Same as i = i + 1


def draw_cool_shape():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    t.tracer(0)
    t.goto(0, 75)
    t.hideturtle()
    size = 350
    for i in range(300):
        t.pencolor(colors[i % len(colors)])
        draw_square2(size)
        t.right(5)
        size *= 0.99
    t.update()


# draw_cool_shape()
t.circle(100)
t.circle(-100)
t.done()
