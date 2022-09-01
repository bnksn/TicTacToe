#shows the numbering system of the grid
def showGridNum():
    print('-------')
    print('|1|2|3|')
    print('-------')
    print('|4|5|6|')
    print('-------')
    print('|7|8|9|')
    print('-------')

#prints the current layout of the grid
def showGrid():
    print('-------')
    print(f'|{tttGrid.one}|{tttGrid.two}|{tttGrid.three}|')
    print('-------')
    print(f'|{tttGrid.four}|{tttGrid.five}|{tttGrid.six}|')
    print('-------')
    print(f'|{tttGrid.seven}|{tttGrid.eight}|{tttGrid.nine}|')
    print('-------')

#processes player 1's turn and checks for a victory
def player1Turn():
    usrInput = input("Player 1 enter position: ")
    try: #this forces a valid input
        if getattr(tttGrid, num2words[int(usrInput)]) == '_': #this makes sure that the position is free
            setattr(tttGrid, num2words[int(usrInput)], 'x')
        else:
            player1Turn()
    except:
        player1Turn()
    checkVictory()

#processes player 2's turn and checks for a victory
def player2Turn():
    usrInput = input("Player 2 enter position: ")
    try: #this forces a valid input
        if getattr(tttGrid, num2words[int(usrInput)]) == '_': #this makes sure that the position is free
            setattr(tttGrid, num2words[int(usrInput)], 'o')
        else:
            player2Turn()
    except:
        player2Turn()
    checkVictory()

#updates the values of the lines that will result in a victory
def updateLines():
    global hor1, hor2, hor3, ver1, ver2, ver3, diag1, diag2, victoryLines
    hor1 = [tttGrid.one, tttGrid.two, tttGrid.three]
    hor2 = [tttGrid.four, tttGrid.five, tttGrid.six]
    hor3 = [tttGrid.seven, tttGrid.eight, tttGrid.nine]
    ver1 = [tttGrid.one, tttGrid.four, tttGrid.seven]
    ver2 = [tttGrid.two, tttGrid.five, tttGrid.eight]
    ver3 = [tttGrid.three, tttGrid.six, tttGrid.nine]
    diag1 = [tttGrid.one, tttGrid.five, tttGrid.nine]
    diag2 = [tttGrid.seven, tttGrid.five, tttGrid.three]
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
    global tttGrid, victory
    showGridNum()
    tttGrid = Grids()
    victory = 'n'
    while(victory == 'n'):
        player1Turn()
        showGrid()
        if victory == 'n':
            player2Turn()
            showGrid()
    if victory == 'x':
        print('Player 1 wins')
    else:
        print('Player 2 wins')
    print('')

#dictionary that allows a conversion between an integer and the spelling of that integer
num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

#class that represents the grid
class Grids:
    def __init__(self):
        self.one = '_'
        self.two = '_'
        self.three = '_'
        self.four = '_'
        self.five = '_'
        self.six = '_'
        self.seven = '_'
        self.eight = '_'
        self.nine = '_'

while(True):
    startGame()