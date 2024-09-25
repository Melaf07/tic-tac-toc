import random
def printBoard(board): #make the bourd
    print("\n")
    print(f"  {board[0]}   |   {board[1]}   |   {board[2]}   ")
    print('----------------------')
    print(f"  {board[3]}   |   {board[4]}   |   {board[5]}   ")
    print('----------------------')
    print(f"  {board[6]}   |   {board[7]}   |   {board[8]}   ")


def available(board, position):
    
    if board[position] == ' ':
        return True
    return False


#take player input
def playerInput(board):
    while True:
        inp = int(input(f"Enter a number 1-9 "))
        if inp >= 1 and inp <= 9 and board[inp-1] == " ":
            board[inp-1] = currentPlayer
            break
        else:
            print(f"Oops the spot has been taken!! ")
            printBoard(board)

def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != " ") or \
       (board[3] == board[4] == board[5] and board[3] != " ") or \
       (board[6] == board[7] == board[8] and board[6] != " "):
        winner = currentPlayer
        return True
def checkRow(board):
    global winner

    if (board[0] == board[3] == board[6] and board[0] != " ") or \
       (board[1] == board[4] == board[7] and board[1] != " ") or\
       (board[2] == board[5] == board[8] and board[2] != " "):
        winner = currentPlayer
        return True

def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0] != " ") or\
       (board[2] == board[4] == board[6] and board[2] != " "):
        winner = currentPlayer
        return True

def checkTie(board):
    global gameRunning
    if " " not in board:
        printBoard(board)
        print("Its a tie")
        gameRunning = False
        n =  input("do you want to play again?[Y/N]")
        if n.upper() == 'Y':
           tictactoc()
        else:
          return False

def checkWin():
 global gameRunning
 if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):      
     printBoard(board)
     print(f"The winner is {winner}")
     gameRunning = False
     n =  input("do you want to play again?[Y/N]")
     if n.upper() == 'Y':
         tictactoc()
     else:
       return False
     

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    position = random.randint(0, 8)
    while not available(board, position):
        position = random.randint(0, 8) 
    board[position] = currentPlayer
    print(f"Computer chose position {position + 1}")



def tictactoc():
    global board,gameRunning,currentPlayer, winner
    board = [' ',' ',' ',' ',' ',' ', ' ',' ',' ']
    winner = None
    gameRunning = True

    a = input("do you want to play with the computer or another player[C/P]")
    if a.upper() == 'C':
       n =  input("do you want to start the game?[Y/N]")
       if n.upper() == 'Y':
          cp = input("choose (X or O)").upper()
          currentPlayer = cp
          while gameRunning:
             printBoard(board)
             if currentPlayer == cp:  # Player's turn
                 playerInput(board)
             else:  # Computer's turn
                 computer(board)
             checkWin()
             checkTie(board)
             switchPlayer()
    else:    
      n =  input("do you want to start the game?[Y/N]")
      if n.upper() == 'Y':
         cp = input("choose (X or O)").upper()
         currentPlayer = cp
         while gameRunning:
            printBoard(board)
            playerInput(board)
            checkWin()
            checkTie(board)
            switchPlayer()

tictactoc()
