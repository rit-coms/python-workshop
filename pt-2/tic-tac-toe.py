import turtle as t

SQUARE_SIZE = 100
MARKER_THICKNESS = 10
DEFAULT_THICKNESS = 2
TOP_LEFT_COORDS = (-1.5 * SQUARE_SIZE, 1.5*SQUARE_SIZE)


def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.right(90)


def draw_row():
    SQUARES = 3
    for _ in range(SQUARES):
        draw_square(SQUARE_SIZE)
        t.forward(SQUARE_SIZE)
    t.backward(3 * SQUARE_SIZE)

def draw_board():
    for _ in range(3):
        draw_row()
        t.right(90)
        t.forward(SQUARE_SIZE)
        t.left(90)
    t.left(90)
    t.forward(3 * SQUARE_SIZE)
    t.right(90)

def draw_board2():
    x = t.xcor()
    y = t.ycor()
    for i in range(3):
        for j in range(3):
            t.penup()
            t.goto(x + i * SQUARE_SIZE, y - j * SQUARE_SIZE)
            t.pendown()
            draw_square(SQUARE_SIZE)

    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_o(size):
    mult = 0.75
    x = t.xcor()
    y = t.ycor()

    # Move to out circle start
    t.penup()
    t.goto(x + size / 2, y - size * ((1 - mult) / 2))

    # Draw circle
    t.width(MARKER_THICKNESS)
    t.pendown()
    t.circle(-size * mult / 2)

    # Return turtle to initial state
    t.width(DEFAULT_THICKNESS)
    t.penup()
    t.goto(x, y)


def draw_x(size):
    mult = 0.8
    offset = size * (1 - mult)
    x = t.xcor()
    y = t.ycor()
    t.width(MARKER_THICKNESS)

    # Draw top-left -> bottom-right
    t.penup()
    t.goto(x + offset, y - offset)
    t.pendown()
    t.goto(x + size - offset, y - size + offset)

    # Draw top-right -> bottom-left
    t.penup()
    t.goto(x + size - offset, y - offset)
    t.pendown()
    t.goto(x + offset, y + offset - size)
    
    # Return to original state
    t.penup()
    t.goto(x, y)
    t.width(DEFAULT_THICKNESS)
    t.pendown()


def main():
    t.speed(0)
    t.width(DEFAULT_THICKNESS)
    t.penup()
    t.goto(TOP_LEFT_COORDS[0], TOP_LEFT_COORDS[1])
    t.pendown()
    draw_board2()
    draw_o(SQUARE_SIZE)
    t.forward(SQUARE_SIZE)
    draw_x(SQUARE_SIZE)
    t.done()


main()
