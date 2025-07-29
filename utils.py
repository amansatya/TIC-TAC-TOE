def print_board(board):
    for row in board:
        print(" | ".join(cell if cell else " " for cell in row))
        print("-" * 9)
