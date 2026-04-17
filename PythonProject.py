import tkinter as tk

current_player = "X"
board = [""] * 9
score_x = 0
score_o = 0
rounds_to_win = 2

# Check winner
def check_winner():
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a,b,c in win_positions:
        if board[a] == board[b] == board[c] and board[a] != "":
            return (a,b,c)
    return None

# Button click
def button_click(index):
    global current_player, score_x, score_o

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player, bg="#ff6f00", fg="black")

        win = check_winner()
        if win:
            highlight_winner(win)

            if current_player == "X":
                score_x += 1
            else:
                score_o += 1

            update_score()
            disable_buttons()

            if score_x == rounds_to_win:
                show_winner_screen("Player X")
            elif score_o == rounds_to_win:
                show_winner_screen("Player O")
            else:
                status_label.config(text=f"🎉 {current_player} wins this round!")

        elif "" not in board:
            status_label.config(text="It's a Draw!")
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"{current_player}'s Turn")

# Highlight winner
def highlight_winner(win):
    for i in win:
        buttons[i].config(bg="#00e676", fg="black")

def disable_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def restart_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    status_label.config(text="X's Turn")

    for btn in buttons:
        btn.config(text="", state="normal", bg="#1e293b", fg="black")

def update_score():
    score_label.config(text=f"X: {score_x}   O: {score_o}")

# BIG WINNER SCREEN
def show_winner_screen(winner):
    win_window = tk.Toplevel(root)
    win_window.attributes('-fullscreen', True)
    win_window.config(bg="#ffe600")

    tk.Label(win_window, text=f"🏆 {winner} Wins!",
             font=("Arial", 60, "bold"),
             bg="#ffe600", fg="black").pack(expand=True)

    tk.Button(win_window, text="Play Again",
              command=lambda: reset_all(win_window),
              bg="#00c853", fg="black",
              font=("Arial", 25, "bold"),
              width=20).pack(pady=40)

def reset_all(win_window):
    global score_x, score_o
    score_x = 0
    score_o = 0
    update_score()
    restart_game()
    win_window.destroy()

# MAIN WINDOW FULLSCREEN
root = tk.Tk()
root.title("Tic Tac Toe")
root.attributes('-fullscreen', True)
root.config(bg="#0f172a")

# MAIN FRAME (CENTER EVERYTHING)
main_frame = tk.Frame(root, bg="#0f172a")
main_frame.pack(expand=True)

# Title (BIG)
tk.Label(main_frame, text="TIC TAC TOE",
         font=("Arial", 50, "bold"),
         bg="#0f172a", fg="#ff3b3b").pack(pady=20)

# Score
score_label = tk.Label(main_frame, text="X: 0   O: 0",
                       font=("Arial", 30, "bold"),
                       bg="#0f172a", fg="#00f5ff")
score_label.pack(pady=10)

# Grid
frame = tk.Frame(main_frame, bg="#0f172a")
frame.pack(pady=20)

# BIG BUTTONS
buttons = []
for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 50, "bold"),
                    width=3, height=1,
                    bg="#1e293b", fg="black",
                    activebackground="#ff9800",
                    relief="flat", bd=10,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3, padx=20, pady=20)
    buttons.append(btn)

# Status
status_label = tk.Label(main_frame, text="X's Turn",
                        font=("Arial", 28, "bold"),
                        bg="#0f172a", fg="#ffe600")
status_label.pack(pady=20)

# Restart button
tk.Button(main_frame, text="Restart Round",
          command=restart_game,
          bg="#ff1744", fg="black",
          font=("Arial", 20, "bold"),
          width=20).pack(pady=20)

# Exit (optional)
tk.Button(main_frame, text="Exit",
          command=root.destroy,
          bg="#ffffff", fg="black",
          font=("Arial", 16, "bold"),
          width=10).pack(pady=10)

root.mainloop()