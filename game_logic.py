from config import BOARD_SIZE
import random

class GameLogic:
    def __init__(self, player_symbol, computer_symbol):
        self.board = [["" for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.player_symbol = player_symbol
        self.computer_symbol = computer_symbol

    def is_valid_move(self, row, col):
        return self.board[row][col] == ""

    def make_move(self, row, col, symbol):
        self.board[row][col] = symbol

    def check_winner(self):
        b = self.board
        for i in range(BOARD_SIZE):
            if b[i][0] == b[i][1] == b[i][2] != "":
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != "":
                return b[0][i]

        if b[0][0] == b[1][1] == b[2][2] != "":
            return b[0][0]
        if b[0][2] == b[1][1] == b[2][0] != "":
            return b[0][2]

        return None

    def is_draw(self):
        return all(cell != "" for row in self.board for cell in row)

    def get_computer_move(self):
        empty_cells = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if self.board[r][c] == ""]
        return random.choice(empty_cells) if empty_cells else None
