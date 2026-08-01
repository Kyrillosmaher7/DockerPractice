import tkinter as tk
from tkinter import messagebox


class TicTacToe:

    def __init__(self, root):

        self.root = root
        self.root.title("Tic-Tac-Toe v2")
        self.root.geometry("750x750")
        self.root.resizable(False, False)

        # Colors
        self.bg_color = "#1e1e2f"
        self.button_color = "#2d2d44"
        self.text_color = "#ffffff"
        self.x_color = "#00d4ff"
        self.o_color = "#ff4d6d"
        self.win_color = "#4caf50"

        self.root.configure(bg=self.bg_color)


        # Game data
        self.current_player = "X"

        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

        self.scores = {
            "X": 0,
            "O": 0,
            "Draw": 0
        }


        # Title
        self.title_label = tk.Label(
            root,
            text="Tic-Tac-Toe",
            font=("Arial", 28, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )

        self.title_label.pack(pady=15)


        # Score board

        self.score_label = tk.Label(
            root,
            text=self.get_score_text(),
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.text_color
        )

        self.score_label.pack()


        # Turn label

        self.turn_label = tk.Label(
            root,
            text="Player X Turn",
            font=("Arial", 18),
            bg=self.bg_color,
            fg=self.x_color
        )

        self.turn_label.pack(pady=10)


        # Board

        self.frame = tk.Frame(
            root,
            bg=self.bg_color
        )

        self.frame.pack()


        self.buttons = []

        for row in range(3):

            button_row = []

            for col in range(3):

                btn = tk.Button(
                    self.frame,
                    text="",
                    width=5,
                    height=2,
                    font=("Arial", 30, "bold"),
                    bg=self.button_color,
                    fg=self.text_color,
                    activebackground="#444466",
                    command=lambda r=row, c=col:
                    self.play(r, c)
                )

                btn.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5
                )

                button_row.append(btn)

            self.buttons.append(button_row)



        # Restart buttons

        self.restart_btn = tk.Button(
            root,
            text="Restart Game",
            font=("Arial", 15),
            width=15,
            command=self.restart,
            bg="#6c63ff",
            fg="white"
        )

        self.restart_btn.pack(pady=15)


        self.reset_score_btn = tk.Button(
            root,
            text="Reset Scores",
            font=("Arial", 13),
            width=15,
            command=self.reset_scores,
            bg="#ff9800",
            fg="white"
        )

        self.reset_score_btn.pack()



    def play(self,row,col):

        if self.board[row][col] != "":
            return


        self.board[row][col] = self.current_player

        self.buttons[row][col]["text"] = self.current_player


        if self.current_player == "X":

            self.buttons[row][col]["fg"] = self.x_color

        else:

            self.buttons[row][col]["fg"] = self.o_color



        if self.check_winner():

            self.scores[self.current_player] += 1

            self.highlight_winner()

            self.update_score()

            messagebox.showinfo(
                "Winner",
                f"Player {self.current_player} Wins!"
            )

            self.disable_board()

            return



        if self.check_draw():

            self.scores["Draw"] += 1

            self.update_score()

            messagebox.showinfo(
                "Draw",
                "Game Draw!"
            )

            return



        self.current_player = (
            "O"
            if self.current_player == "X"
            else "X"
        )


        self.turn_label.config(
            text=f"Player {self.current_player} Turn",
            fg=
            self.x_color
            if self.current_player == "X"
            else self.o_color
        )



    def check_winner(self):

        b = self.board


        for row in b:

            if row[0] == row[1] == row[2] != "":
                return True


        for col in range(3):

            if (
                b[0][col]
                ==
                b[1][col]
                ==
                b[2][col]
                != ""
            ):
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



    def highlight_winner(self):

        # highlight all winning buttons
        for row in self.buttons:

            for btn in row:

                if btn["text"] == self.current_player:

                    btn.config(
                        bg=self.win_color
                    )



    def disable_board(self):

        for row in self.buttons:

            for btn in row:

                btn.config(
                    state="disabled"
                )



    def restart(self):

        self.board = [
            ["","",""],
            ["","",""],
            ["","",""]
        ]

        self.current_player = "X"


        for row in self.buttons:

            for btn in row:

                btn.config(
                    text="",
                    state="normal",
                    bg=self.button_color
                )


        self.turn_label.config(
            text="Player X Turn",
            fg=self.x_color
        )



    def get_score_text(self):

        return (
            f"X: {self.scores['X']}    "
            f"O: {self.scores['O']}    "
            f"Draw: {self.scores['Draw']}"
        )



    def update_score(self):

        self.score_label.config(
            text=self.get_score_text()
        )



    def reset_scores(self):

        self.scores = {
            "X":0,
            "O":0,
            "Draw":0
        }

        self.update_score()



if __name__ == "__main__":

    root = tk.Tk()

    game = TicTacToe(root)

    root.mainloop()