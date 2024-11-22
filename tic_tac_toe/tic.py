import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def button_click(row, col):
    if board[row][col] == "" and not game_over:
        board[row][col] = current_player.get()
        buttons[row][col].config(text=current_player.get())
        check_winner()

        # Switch player
        if current_player.get() == "X":
            current_player.set("O")
        else:
            current_player.set("X")

# Function to check if someone has won
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != "":
            end_game(f"{board[row][0]} wins!")
            return
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            end_game(f"{board[0][col]} wins!")
            return
    if board[0][0] == board[1][1] == board[2][2] != "":
        end_game(f"{board[0][0]} wins!")
        return
    if board[0][2] == board[1][1] == board[2][0] != "":
        end_game(f"{board[0][2]} wins!")
        return
    if all(board[row][col] != "" for row in range(3) for col in range(3)):
        end_game("It's a tie!")
        return

# Function to end the game and display the winner
def end_game(message):
    global game_over
    game_over = True
    messagebox.showinfo("Game Over", message)
    restart_button.grid(row=4, column=0, columnspan=3)

# Function to restart the game
def restart_game():
    global game_over
    game_over = False
    current_player.set("X")
    for row in range(3):
        for col in range(3):
            board[row][col] = ""
            buttons[row][col].config(text="")
    restart_button.grid_forget()

# Initialize the Tkinter window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize game variables
current_player = tk.StringVar()
current_player.set("X")
game_over = False

# Create a 3x3 grid of buttons
board = [["" for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text="", width=10, height=3, font=("Arial", 24),
                                      command=lambda r=row, c=col: button_click(r, c))
        buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

# Restart button
restart_button = tk.Button(root, text="Restart", width=30, height=2, font=("Arial", 14), command=restart_game)

# Start the Tkinter event loop
root.mainloop()
