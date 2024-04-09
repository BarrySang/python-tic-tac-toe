import sys

def tic_tac_toe():
    def print_board(board):
        for row in board:
            print(" | ".join(row))
            print("-" * 9)

    def check_winner(board):
        # Check rows
        for row in board:
            if row.count(row[0]) == len(row) and row[0] != ' ':
                return True

        # Check columns
        for col in range(len(board[0])):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
                return True

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
            return True
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
            return True

        return False

    while True:
        board = [["1", "2", "3"],
                 ["4", "5", "6"],
                 ["7", "8", "9"]]
        players = ['X', 'O']
        player_index = 0

        while True:
            print_board(board)
            print(f"Player {players[player_index]}'s turn")
            try:
                move = input("Enter a number (1-9) or 'q' to quit: ")
                if move.lower() == 'q':
                    print("Quitting the game...")
                    sys.exit()
                else:
                    move = int(move) - 1
                    if 0 <= move <= 8:
                        row = move // 3
                        col = move % 3
                        if board[row][col].isdigit():
                            board[row][col] = players[player_index]
                            if check_winner(board):
                                print_board(board)
                                print(f"Player {players[player_index]} wins!")
                                break
                            elif all(cell.isdigit() for row in board for cell in row):
                                print_board(board)
                                print("It's a tie!")
                                break
                            player_index = (player_index + 1) % 2
                        else:
                            print("That position is already taken!")
                    else:
                        print("Please enter a number between 1 and 9!")
            except ValueError:
                print("Please enter a valid number!")

        restart = input("Press 'r' to restart or 'q' to quit: ")
        if restart.lower() == 'q':
            print("Quitting the game...")
            sys.exit()

if __name__ == "__main__":
    tic_tac_toe()
