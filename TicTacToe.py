def ShowGrid(grid):
    print(f'|{grid[0]}|{grid[1]}|{grid[2]}|')
    print(f'|{grid[3]}|{grid[4]}|{grid[5]}|')
    print(f'|{grid[6]}|{grid[7]}|{grid[8]}|')

def PlayerTurn(player, grid, victory):
    players = ["A","B"]
    playerLabels = ["x", "o"]
    usrInput = input("Player " + players[player] + " enter position: ")
    try: #force a valid input
        if grid[int(usrInput) - 1] == '_': #check if the position is free
            grid[int(usrInput) - 1] = playerLabels[player]
        else:
            PlayerTurn(player, grid, victory)
    except:
        PlayerTurn(player, grid, victory)
    victory = CheckVictory(grid, victory)
    return grid, victory

def CheckVictory(grid, victory):
    hor1 = [grid[0], grid[1], grid[2]]
    hor2 = [grid[3], grid[4], grid[5]]
    hor3 = [grid[6], grid[7], grid[8]]
    ver1 = [grid[0], grid[3], grid[6]]
    ver2 = [grid[1], grid[4], grid[7]]
    ver3 = [grid[2], grid[5], grid[8]]
    diag1 = [grid[0], grid[4], grid[8]]
    diag2 = [grid[6], grid[4], grid[2]]
    victoryLines = [hor1, hor2, hor3, ver1, ver2, ver3, diag1, diag2]
    for line in victoryLines:
        if len(set(line)) == 1 and line[0] != '_': #check if all of the elements of a victory line are identical 
            return line[0]
    return victory

def StartGame():
    print('|1|2|3|')
    print('|4|5|6|')
    print('|7|8|9|')
    print("Player A is 'x', Player B is 'o'\n")
    grid = ['_','_','_',
            '_','_','_',
            '_','_','_']
    victory = 'n'
    playerATurns = 0
    while(victory == 'n'):
        playerATurns += 1
        if playerATurns == 5:
            victory = 'd'
        grid, victory = PlayerTurn(0, grid, victory) #0 represents player A
        ShowGrid(grid)
        if victory == 'n':
            grid, victory = PlayerTurn(1, grid, victory) #1 represents player B
            ShowGrid(grid)
    if victory == 'x':
        print('Player A wins\n')
    elif victory == 'o':
        print('Player B wins\n')
    else: #victory == 'd'
        print("Draw\n")

if __name__ == "__main__":
    StartGame()
