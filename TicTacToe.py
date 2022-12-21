#shows the numbering system of the grid
def showGridNum():
    print('|1|2|3|')
    print('|4|5|6|')
    print('|7|8|9|')

#prints the current layout of the grid
def showGrid():
    print(f'|{grid[0]}|{grid[1]}|{grid[2]}|')
    print(f'|{grid[3]}|{grid[4]}|{grid[5]}|')
    print(f'|{grid[6]}|{grid[7]}|{grid[8]}|')

#processes players turn and checks for a victory
def playerTurn(player):
    playerNumbers = ["1","2"]
    playerLabels = ["x", "o"]
    usrInput = input("Player " + playerNumbers[player] + " enter position: ")
    try: #this forces a valid input
        if grid[int(usrInput) - 1] == '_': #this makes sure that the position is free
            grid[int(usrInput) - 1] = playerLabels[player]
        else:
            playerTurn(player)
    except:
        playerTurn(player)
    checkVictory()

#updates the values of the lines that will result in a victory
def updateLines():
    global hor1, hor2, hor3, ver1, ver2, ver3, diag1, diag2, victoryLines
    hor1 = [grid[0], grid[1], grid[2]]
    hor2 = [grid[3], grid[4], grid[5]]
    hor3 = [grid[6], grid[7], grid[8]]
    ver1 = [grid[0], grid[3], grid[6]]
    ver2 = [grid[1], grid[4], grid[7]]
    ver3 = [grid[2], grid[5], grid[8]]
    diag1 = [grid[0], grid[4], grid[8]]
    diag2 = [grid[6], grid[4], grid[2]]
    victoryLines = [hor1, hor2, hor3, ver1, ver2, ver3, diag1, diag2]

#checks if any of the lines are full
def checkVictory():
    global victory
    updateLines()
    for line in victoryLines:
        if len(set(line)) == 1 and line[0] != '_': #checks if all of the elements of a line are identical 
            victory = line[0]

#creates the grid and starts the game
def startGame():
    global grid, victory
    showGridNum()
    #list that represents the grid
    grid = ['_','_','_', #0,1,2 (by index)
            '_','_','_', #3,4,5
            '_','_','_'] #6,7,8
    victory = 'n'
    player1Turns = 0
    while(victory == 'n'):
        player1Turns = player1Turns + 1
        if player1Turns == 5:
            victory = 'd'
        playerTurn(0) #0 represents player 1
        showGrid()
        if victory == 'n':
            playerTurn(1) #1 represents player 2
            showGrid()
    if victory == 'x':
        print('Player 1 wins\n')
    elif victory == 'o':
        print('Player 2 wins\n')
    else: #victory == 'd'
        print("Draw\n")

if __name__ == "__main__":
    startGame()
