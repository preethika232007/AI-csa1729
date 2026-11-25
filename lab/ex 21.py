board = [' ' for _ in range(9)]

def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

def victory(icon):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] == icon:
            return True
    return False

while True:
    print_board()
    choice = int(input("Player X, enter position (1-9): "))
    if board[choice-1] == ' ':
        board[choice-1] = 'X'
    else:
        print("Position already taken!")
        continue

    if victory('X'):
        print_board()
        print("X Wins!")
        break

    if ' ' not in board:
        print("It's a Draw!")
        break

    print_board()
    choice = int(input("Player O, enter position (1-9): "))
    if board[choice-1] == ' ':
        board[choice-1] = 'O'
    else:
        print("Position already taken!")
        continue

    if victory('O'):
        print_board()
        print("O Wins!")
        break