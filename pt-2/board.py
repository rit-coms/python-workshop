import turtle as t

def draw_square(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

def draw_row(size):
    for i in range(3):
        draw_square(size)
        t.forward(size)
    t.backward(3 * size)

def draw_board(size):
    for i in range(3):
        draw_row(size)
        t.right(90)
        t.forward(size)
        t.left(90)

def get_winner(board):
    # Check rows
    for row in board:
        values = set(row)
        if len(values) == 1:
            winner = values.pop()
            if winner == "":
                continue
            return winner
    
    # Check columns
    board_size = len(board)
    for col in range(board_size):
        values = set()
        for row in range(board_size):
            value = board[row][col]
            values.add(value)
        if len(values) == 1:
            winner = values.pop()
            if winner == "":
                continue
            return winner
    
    return "Bruh"
    

board = [
    ["", "x", "o"],
    ["", "", ""],
    ["o", "o", "o"],
]

board2 = [
    ["", "o", "x"],
    ["", "o", "x"],
    ["", "", "x"],
]

winner = get_winner(board)
print("Hello there")
print(winner)
print(get_winner(board2))

# draw_board(50)
# t.done()