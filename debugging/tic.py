#Ce code permet de jouer au morpion

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Vérifie lignes
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    # Vérifie colonnes
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return True

    # Vérifie diagonales
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def is_full(board):
    # Vérifie s’il reste une case vide
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in range(3) or col not in range(3):
                print("Coordinates must be between 0 and 2. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player

        if check_winner(board):
            print_board(board)
            print(f"🎉 Player {player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("🤝 It's a tie!")
            break

        # Change player
        player = "O" if player == "X" else "X"

tic_tac_toe()
