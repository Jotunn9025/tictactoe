import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.configure(background='#6330a1')
        self.current_player = "X"
        self.player_colors = {"X": "#589456", "O": "#b34646"}
        self.board = [" "]*9
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Times New Roman", 30), width=8, height=4,
                                   command=lambda rows=i, cols=j: self.make_move(rows, cols))
                button.grid(row=i, column=j, padx=15, pady=15)
                button.configure(bg='#444d87')
                self.buttons.append(button)
    def make_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            player_color = self.player_colors[self.current_player]
            self.buttons[index].config(text=self.current_player, fg=player_color)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    def check_winner(self):
        winning_positions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                             (0, 3, 6), (1, 4, 7), (2, 5, 8),
                             (0, 4, 8), (2, 4, 6))
        for pos in winning_positions:
            if self.board[pos[0]] == self.board[pos[1]] == self.board[pos[2]] != " ":
                return True
        return False
    def reset_game(self):
        self.current_player = "X"
        self.board = [" "]*9
        for button in self.buttons:
            button.config(text="")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
