teamplate_board = """CORDINATES
  1 2 3
1 _ _ _
1 _ _ _
1 _ _ _
"""

board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

print(teamplate_board)

def reqInput(player: int):
    user_input = input(f"Player {player}, Enter the coordinates of your move (xy): ")
    try:
        return int(user_input[0]), int(user_input[1])
    except:
        print("Invalid input")
        return reqInput(player)

def updateBoard(char: str, x: int, y: int):
    if x <= 3 and y <= 3:
        x = x - 1
        y = y - 1
        if board[x][y] == "_":
            board[x][y] = char
            return True

    print("Invalid move")
    newmove = reqInput(player)
    updateBoard(char, newmove[0], newmove[1])

def renderBoard():
    print("----------")
    for row in board:
        print("   ".join(row))
    print("----------")

def checkWin():
    for row in board:
        if row[0] == row[1] == row[2] != "_":
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "_":
            return True
    
    if board[0][0] == board[1][1] == board[2][2] != "_":
        return True
    
    if board[0][2] == board[1][1] == board[2][0] != "_":
        return True

player = 1
moves = 0
chars = ["X", "O"]

while True:
    renderBoard()

    x, y = reqInput(player)
    moves += 1
    updateBoard(chars[player - 1], x, y)

    if checkWin():
        renderBoard()
        print(f"Player {player} wins with {moves} moves!")
        break

    player = (player % 2) + 1