def ShowGrid(grid):
    print(f'|{grid[0]}|{grid[1]}|{grid[2]}|')
    print(f'|{grid[3]}|{grid[4]}|{grid[5]}|')
    print(f'|{grid[6]}|{grid[7]}|{grid[8]}|')

def PlayerAction(player, grid, victory):
    usrInput = input(player + ": ")
    try: #force a valid input
        if grid[int(usrInput) - 1] == '_': #check if the position is free
            grid[int(usrInput) - 1] = player
        else:
            PlayerAction(player, grid, victory)
    except:
        PlayerAction(player, grid, victory)
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
    grid = ['_','_','_',
            '_','_','_',
            '_','_','_']
    victory = 'n'
    playerTurn = 0
    while(victory == 'n'):
        playerTurn += 1
        if playerTurn == 5:
            victory = 'd'
        grid, victory = PlayerAction('x', grid, victory)
        ShowGrid(grid)
        if victory == 'n':
            grid, victory = PlayerAction('o', grid, victory)
            ShowGrid(grid)
    if victory == 'd':
        print("Draw\n")
    else:
        print(victory + " wins\n")
    StartGame()

if __name__ == "__main__":
    StartGame()
