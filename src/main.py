import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("420x500")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.title = tk.Label(
            root,
            text="Tic-Tac-Toe",
            font=("Arial", 24, "bold")
        )
        self.title.pack(pady=10)

        self.turn_label = tk.Label(
            root,
            text="Player X Turn",
            font=("Arial", 16)
        )
        self.turn_label.pack()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        self.buttons = []

        for row in range(3):
            button_row = []
            for col in range(3):
                btn = tk.Button(
                    self.frame,
                    text="",
                    width=5,
                    height=2,
                    font=("Arial", 28, "bold"),
                    command=lambda r=row, c=col: self.play(r, c)
                )
                btn.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(btn)

            self.buttons.append(button_row)

        self.restart_btn = tk.Button(
            root,
            text="Restart Game",
            font=("Arial", 14),
            command=self.restart
        )
        self.restart_btn.pack(pady=15)

    def play(self, row, col):

        if self.board[row][col] != "":
            return

        self.board[row][col] = self.current_player
        self.buttons[row][col]["text"] = self.current_player

        if self.check_winner():

            messagebox.showinfo(
                "Winner",
                f"Player {self.current_player} Wins!"
            )

            self.disable_board()
            return

        if self.check_draw():

            messagebox.showinfo(
                "Draw",
                "Game ended in a draw!"
            )

            return

        self.current_player = "O" if self.current_player == "X" else "X"

        self.turn_label.config(
            text=f"Player {self.current_player} Turn"
        )

    def check_winner(self):

        b = self.board

        for row in b:
            if row[0] == row[1] == row[2] != "":
                return True

        for c in range(3):
            if b[0][c] == b[1][c] == b[2][c] != "":
                return True

        if b[0][0] == b[1][1] == b[2][2] != "":
            return True

        if b[0][2] == b[1][1] == b[2][0] != "":
            return True

        return False

    def check_draw(self):

        for row in self.board:
            if "" in row:
                return False

        return True

    def disable_board(self):

        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")

    def restart(self):

        self.current_player = "X"

        self.turn_label.config(
            text="Player X Turn"
        )

        self.board = [["" for _ in range(3)] for _ in range(3)]

        for row in self.buttons:
            for btn in row:
                btn.config(
                    text="",
                    state="normal"
                )


root = tk.Tk()

game = TicTacToe(root)

root.mainloop()