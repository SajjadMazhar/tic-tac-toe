board = list(range(1, 10))


def GameBoard():
    game = f"""

    {board[0]} | {board[1]} | {board[2]}
    ---------
    {board[3]} | {board[4]} | {board[5]}
    ---------
    {board[6]} | {board[7]} | {board[8]}

    """
    print(game)


GameBoard()
name1=input("enter your name player 1: ")
name2=input("enter your name player 2:")

# Player one move input..
def moves1():
    while True:
        write = int(input(f"{name1}, Where to place your move: "))
        if board[write - 1] == 'O' or board[write - 1] == 'X':
            print("The position has already been occupied!")
        else:
            board[write - 1] = 'X'
            GameBoard()
            break


# Player two move input..
def moves2():
    while True:
        write = int(input(f"{name2}, Where to place your move: "))
        if board[write - 1] == 'O' or board[write - 1] == 'X':
            print("The position has already been occupied!")
        else:
            board[write - 1] = 'O'
            GameBoard()
            break


turn = 0
while True:

    moves1()
    turn += 1
    if ((board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (
            board[2] == 'X' and board[4] == 'X' and board[6] == 'X') or  # x wins
            (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (
                    board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or  # = wins
            (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (
                    board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or  # + wins
            (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (
                    board[2] == 'X' and board[5] == 'X' and board[8] == 'X')):  # || wins
        print(f"{name1} wins")
        break

    if turn == 9:
        print("No one wins!")
        break
    else:
        moves2()
        turn += 1
        if ((board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (
                board[2] == 'O' and board[4] == 'O' and board[6] == 'O') or  # x wins
                (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (
                        board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or  # = wins
                (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (
                        board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or  # + wins
                (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (
                        board[2] == 'O' and board[5] == 'O' and board[8] == 'O')):  # || wins
            print(f"{name2} wins")
            break
        else:
            continue
