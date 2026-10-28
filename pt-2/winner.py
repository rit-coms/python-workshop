# This is a big, messy function. How would you improve it?
def get_winner(board):
    board_size = len(board)  # Assume square
    # If all slots are the same and != "", then we got a winner
    # Check row
    for row in board:
        row_set = set()  # Can't use {} because that would be an empty dict
        for val in row:
            row_set.add(val)
        if len(row_set) == 1:
            token = row_set.pop()
            if token != "":
                return token

    # Check col
    for col_i in range(board_size):
        # For each column, I need to look throuw
        col_set = set()
        for row_i in range(board_size):
            val = board[row_i][col_i]
            col_set.add(val)
        if len(col_set) == 1:
            token = col_set.pop()
            if token != "":
                return token

    # Check top-left to bot-right diagonal
    diag_set = set()
    for i in range(board_size):
        val = board[i][i]
        diag_set.add(val)
    if len(diag_set) == 1:
        token = diag_set.pop()
        if token != "":
            return token

    # Check top-right to bot-left diagonal
    diag_set = set()
    for i in range(board_size):
        val = board[i][board_size - i - 1]
        diag_set.add(val)
    if len(diag_set) == 1:
        token = diag_set.pop()
        if token != "":
            return token

    # No winners
    return None


board1 = [
    ["x", "", ""],
    ["", "x", ""],
    ["o", "o", "x"],
]

board2 = [
    ["", "x", "o"],
    ["", "o", ""],
    ["o", "", "x"],
]

board3 = [
    ["", "o", "o"],
    ["", "o", ""],
    ["x", "x", "x"],
]

board4 = [
    ["", "o", ""],
    ["", "o", "x"],
    ["x", "o", "x"],
]

board5 = [
    ["x", "", ""],
    ["", "x", ""],
    ["o", "", "o"],
]

for board in [board1, board2, board3, board4, board5]:
    print(get_winner(board))
