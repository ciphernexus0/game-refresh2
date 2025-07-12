def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return True
    for col in range(3):
        if all(board[row][col] == board[0][col] and board[0][col] != ' ' for row in range(3)):
            return True
    if all(board[i][i] == board[0][0] and board[0][0] != ' ' for i in range(3)) or \
       all(board[i][2 - i] == board[0][2] and board[0][2] != ' ' for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                return
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That spot is already taken. Try again.")

    print_board(board)
    print("It's a tie!")

tic_tac_toe()
