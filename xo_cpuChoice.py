import random

print("Welcome to Tic Tac Toe")
print("----------------------")

possibleNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3

def printGameBoard():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print(f" {gameBoard[x][y]} |", end="")
    print("\n+---+---+---+")

def modifyArray(num, turn):
    row = (num - 1) // cols
    col = (num - 1) % cols
    gameBoard[row][col] = turn

def checkForWinner(board):
    # Check rows and columns
    for i in range(rows):
        if all([cell == 'X' for cell in board[i]]) or all([board[j][i] == 'X' for j in range(cols)]):
            print("X has won!")
            return 'X'
        if all([cell == 'O' for cell in board[i]]) or all([board[j][i] == 'O' for j in range(cols)]):
            print("O has won!")
            return 'O'
    # Check diagonals
    if all([board[i][i] == 'X' for i in range(rows)]) or all([board[i][cols-i-1] == 'X' for i in range(rows)]):
        print("X has won!")
        return 'X'
    if all([board[i][i] == 'O' for i in range(rows)]) or all([board[i][cols-i-1] == 'O' for i in range(rows)]):
        print("O has won!")
        return 'O'
    return None

def isDraw(board):
    return all(isinstance(cell, str) for row in board for cell in row)

def getWinningMove(board, turn):
    for num in possibleNumbers:
        row = (num - 1) // cols
        col = (num - 1) % cols
        original = board[row][col]
        board[row][col] = turn
        if checkForWinner(board) == turn:
            board[row][col] = original
            return num
        board[row][col] = original
    return None

def getBlockMove(board, turn):
    opponent = 'X' if turn == 'O' else 'O'
    return getWinningMove(board, opponent)

def getCpuMove(board):
    # Check if we can win
    move = getWinningMove(board, 'O')
    if move:
        return move
    
    # Check if we need to block
    move = getBlockMove(board, 'O')
    if move:
        return move
    
    # Take the center if available
    if 5 in possibleNumbers:
        return 5
    
    # Take a corner if available
    for move in [1, 3, 7, 9]:
        if move in possibleNumbers:
            return move
    
    # Take any side if available
    for move in [2, 4, 6, 8]:
        if move in possibleNumbers:
            return move
    
    # Fallback to random
    return random.choice(possibleNumbers)

leaveLoop = False
turnCounter = 0

while not leaveLoop:
    printGameBoard()
    if turnCounter % 2 == 0:
        numberPicked = int(input("\nChoose a number [1-9]: "))
        if numberPicked in possibleNumbers:
            modifyArray(numberPicked, 'X')
            possibleNumbers.remove(numberPicked)
            turnCounter += 1
        else:
            print("Invalid input. Please try again.")
    else:
        cpuChoice = getCpuMove(gameBoard)
        print("\nCpu choice:", cpuChoice)
        modifyArray(cpuChoice, 'O')
        possibleNumbers.remove(cpuChoice)
        turnCounter += 1
    
    winner = checkForWinner(gameBoard)
    if winner:
        printGameBoard()
        print(f"\nGame over! {winner} wins! Thank you for playing :)")
        break
    
    if isDraw(gameBoard):
        printGameBoard()
        print("\nGame over! It's a draw! Thank you for playing :)")
        break
