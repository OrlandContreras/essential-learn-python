from random import randrange


def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def make_list_of_free_fields(board):
    free = []  # the list is empty initially
    for row in range(3):  # iterate through rows
        for col in range(3):  # iterate through columns
            if board[row][col] not in ["O", "X"]:
                free.append((row, col))
    return free


def enter_move(board):
    ok = False  # fake assumption, we need it to enter the while loop
    while not ok:
        move = input("Enter your move: ")
        ok = (
            len(move) == 1 and move >= "1" and move <= "9"
        )  # is the length of the move correct?
        if not ok:
            print("Bad move! - repeat your input")  # no, it isn't -> retry
            continue
        move = int(move) - 1  # cell's number from 0 to 8
        row = move // 3  # cell's row
        col = move % 3  # cell's column
        cell_value = board[row][col]
        ok = cell_value not in ["O", "X"]  # is the cell free?
        if not ok:
            print("Cell is occupied! Choose another one!")  # no, it is -> retry
            continue
    board[row][col] = "O"  # set the free cell with "O"


def victory_for(board, cell_value):
    if cell_value == "X":
        who = "me"
    elif cell_value == "O":
        who = "you"
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == board[rc][1] == board[rc][2] == cell_value:
            return who
        if board[0][rc] == board[1][rc] == board[2][rc] == cell_value:
            return who
        if board[rc][rc] != cell_value:
            cross1 = False
        if board[2 - rc][2 - rc] != cell_value:
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = "X"


board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # make an empty board
board[1][1] = "X"  # set the middle square to X
free = make_list_of_free_fields(board)
human_turn = True  # which turn is it now?

while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        human = victory_for(board, "O")
    else:
        draw_move(board)
        human = victory_for(board, "X")
    if human != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if human == "you":
    print("You won!")
elif human == "me":
    print("I won")
else:
    print("Tie!")
