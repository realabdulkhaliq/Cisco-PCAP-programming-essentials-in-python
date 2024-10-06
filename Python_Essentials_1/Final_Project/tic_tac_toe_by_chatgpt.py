import random

def display_board(board):
    # Display the current board status
    for row in board:
        print("+-------" * 3 + "+")
        print("|       " * 3 + "|")
        for col in row:
            print(f"|   {col}   ", end="")
        print("|")
        print("|       " * 3 + "|")
    print("+-------" * 3 + "+")

def enter_move(board):
    # Prompt the user to enter a move and update the board
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move)
            if 1 <= move <= 9:
                row, col = (move - 1) // 3, (move - 1) % 3
                if board[row][col] not in ['X', 'O']:
                    board[row][col] = 'O'
                    break
                else:
                    print("This spot is already taken!")
            else:
                print("Invalid number. Enter a number between 1 and 9.")
        else:
            print("Please enter a valid number.")

def make_list_of_free_fields(board):
    # Return a list of free positions (row, col) tuples
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free_fields.append((r, c))
    return free_fields

def victory_for(board, sign):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],  # row 1
        [board[1][0], board[1][1], board[1][2]],  # row 2
        [board[2][0], board[2][1], board[2][2]],  # row 3
        [board[0][0], board[1][0], board[2][0]],  # column 1
        [board[0][1], board[1][1], board[2][1]],  # column 2
        [board[0][2], board[1][2], board[2][2]],  # column 3
        [board[0][0], board[1][1], board[2][2]],  # diagonal 1
        [board[0][2], board[1][1], board[2][0]]   # diagonal 2
    ]
    return [sign, sign, sign] in win_conditions

def draw_move(board):
    # The computer randomly selects a free square
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'

def main():
    # Initialize board
    board = [[str(i + 1) for i in range(j, j + 3)] for j in range(0, 9, 3)]
    
    # The computer's first move (middle of the board)
    board[1][1] = 'X'

    while True:
        display_board(board)
        if victory_for(board, 'X'):
            print("The computer wins!")
            break
        elif not make_list_of_free_fields(board):
            print("It's a tie!")
            break
        enter_move(board)
        if victory_for(board, 'O'):
            display_board(board)
            print("You win!")
            break
        elif not make_list_of_free_fields(board):
            display_board(board)
            print("It's a tie!")
            break
        draw_move(board)

# Run the game
main()
