import tkinter as tk
from tkinter import messagebox
import random

currentPlayer = "X"
computer_symbol = "O"
current_turn = "Player"
game_mode = "2 Players"  
board = {i: " " for i in range(9)}  
buttons = []  

def create_board():
    global buttons
    buttons = []  
    for i in range(9):
        button = tk.Button(board1, text=" ", width=10, height=3, font=("Arial", 24),
                           command=lambda i=i: playerInput(i))  # Capture `i` properly
        button.grid(row=(i // 3), column=i % 3)
        buttons.append(button)

def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            for idx in combination:
                buttons[idx].config(bg="lightgreen")  
            return True
    return False

def choose_game_mode(mode):
    global game_mode
    game_mode = mode
    reset_game()

def reset_game():
    for i in range(9):
        board[i] = " "
    for button in buttons:
        button.config(text=" ", state="normal", bg="SystemButtonFace")  

def ask_restart():
    restart = messagebox.askyesno("Game Over", "Do you want to restart the game?")
    if restart:
        reset_game()  
    else:
        window.destroy()  

def choose_symbol(S):
    global currentPlayer, computer_symbol
    currentPlayer = S
    computer_symbol = "O" if S == "X" else "X"

def start_game():
    global current_turn
    create_board()  
    current_turn = "Player" if currentPlayer == "X" else "Player 2"
    reset_game()  

def playerInput(i):
    global current_turn
    if board[i] == " ":
        board[i] = currentPlayer if current_turn == "Player" else computer_symbol
        buttons[i].config(text=board[i])

        if check_winner():
            disable_buttons()
            messagebox.showinfo("Game Over", f"{current_turn} wins!")
            ask_restart()  

        elif all(value != " " for value in board.values()):
            disable_buttons()
            messagebox.showinfo("Game Over", "It's a draw!")
            ask_restart()  
        else:
            if game_mode == "2 Players":
                current_turn = "Player 2" if current_turn == "Player" else "Player"
            else:
                if current_turn == "Player":
                    current_turn = "Computer"
                    computer_move()
                    current_turn = "Player"

def computer_move():
    # Helper functions for move selection
    def find_winning_move(symbol):
        for combination in [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]:
            values = [board[i] for i in combination]
            if values.count(symbol) == 2 and values.count(" ") == 1:
                return combination[values.index(" ")]
        return None

    move = find_winning_move(computer_symbol)
    if move is not None:
        playerInput(move)
        return
    available_moves = [i for i in range(9) if board[i] == " "]
    if available_moves:
        move = random.choice(available_moves)
        playerInput(move)

window = tk.Tk()
window.title("Tic Tac Toe")

board1 = tk.Frame(window)
board1.grid(row=3, column=0, columnspan=4)  

tk.Label(window, text="Choose Game Mode:").grid(row=0, column=0, columnspan=2)
tk.Button(window, text="2 Players", command=lambda: choose_game_mode("2 Players")).grid(row=0, column=2)
tk.Button(window, text="Computer", command=lambda: choose_game_mode("Computer")).grid(row=0, column=3)

tk.Label(window, text="Choose Symbol:").grid(row=1, column=0, columnspan=2)
tk.Button(window, text="X", command=lambda: choose_symbol("X")).grid(row=1, column=2)
tk.Button(window, text="O", command=lambda: choose_symbol("O")).grid(row=1, column=3)

tk.Button(window, text="Start Game", command=start_game).grid(row=2, column=0, columnspan=4)  # Call start_game on click

window.mainloop()
