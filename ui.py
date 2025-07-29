import tkinter as tk
from tkinter import messagebox
import config
from game_logic import GameLogic

class SymbolSelectorUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Choose Your Symbol")
        self.window.geometry("400x300")
        self.window.configure(bg="#f0f0f0")

        label = tk.Label(self.window, text="Choose your symbol", font=("Arial", 20), bg="#f0f0f0")
        label.pack(pady=30)

        btn_frame = tk.Frame(self.window, bg="#f0f0f0")
        btn_frame.pack(pady=10)

        self.x_button = tk.Button(btn_frame, text="X", font=("Arial", 28), width=6, height=2,
                                  command=lambda: self.start_game("X"))
        self.x_button.grid(row=0, column=0, padx=20)

        self.o_button = tk.Button(btn_frame, text="O", font=("Arial", 28), width=6, height=2,
                                  command=lambda: self.start_game("O"))
        self.o_button.grid(row=0, column=1, padx=20)

    def start_game(self, player_symbol):
        config.PLAYER_SYMBOL = player_symbol
        config.COMPUTER_SYMBOL = "O" if player_symbol == "X" else "X"
        self.window.destroy()
        game = TicTacToeUI()
        game.run()

    def run(self):
        self.window.mainloop()


class TicTacToeUI:
    def __init__(self):
        self.logic = GameLogic(config.PLAYER_SYMBOL, config.COMPUTER_SYMBOL)
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - You vs Computer")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.build_grid()

    def build_grid(self):
        for row in range(3):
            for col in range(3):
                btn = tk.Button(self.window, text="", width=8, height=4,
                                font=("Arial", 24), command=lambda r=row, c=col: self.player_turn(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def player_turn(self, row, col):
        if not self.logic.is_valid_move(row, col):
            return

        self.logic.make_move(row, col, config.PLAYER_SYMBOL)
        self.buttons[row][col]["text"] = config.PLAYER_SYMBOL

        if self.check_game_end(): return

        self.window.after(500, self.computer_turn)

    def computer_turn(self):
        move = self.logic.get_computer_move()
        if move:
            row, col = move
            self.logic.make_move(row, col, config.COMPUTER_SYMBOL)
            self.buttons[row][col]["text"] = config.COMPUTER_SYMBOL
            self.check_game_end()

    def check_game_end(self):
        winner = self.logic.check_winner()
        if winner:
            msg = "You win!" if winner == config.PLAYER_SYMBOL else "Computer wins!"
            messagebox.showinfo("Game Over", msg)
            self.window.quit()
            return True
        elif self.logic.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.window.quit()
            return True
        return False

    def run(self):
        self.window.mainloop()
