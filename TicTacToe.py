class TicTacToe():
    def __init__(self) -> None:
        print('|1|2|3|')
        print('|4|5|6|')
        print('|7|8|9|')
        self.grid = ['_','_','_',
                     '_','_','_',
                     '_','_','_']
        self.victory = 'n'
        self.playerTurnCount = 0
    
    def playGame(self) -> None:
        while(self.victory == 'n'):
            if self.playerTurnCount == 4:
                self.victory = 'd'

            self.playerAction('x')
            self.checkVictory()
            self.showGrid()
            if self.victory == 'n':
                self.playerAction('o')
                self.checkVictory()
                self.showGrid()
            
            self.playerTurnCount += 1
    
    def displayWinner(self) -> None:
        print("Nobody wins\n") if self.victory == 'd' else print(self.victory + " wins\n")
    
    def playerAction(self, player:str) -> None:
        usrInput = input(player + ": ")
        if (usrInput in ("1", "2", "3", "4", "5", "6", "7", "8", "9")) and (self.grid[int(usrInput) - 1] == '_'):
            self.grid[int(usrInput) - 1] = player
        else:
            self.playerAction(player)
    
    def checkVictory(self) -> None:
        hor1 = [self.grid[0], self.grid[1], self.grid[2]]
        hor2 = [self.grid[3], self.grid[4], self.grid[5]]
        hor3 = [self.grid[6], self.grid[7], self.grid[8]]
        ver1 = [self.grid[0], self.grid[3], self.grid[6]]
        ver2 = [self.grid[1], self.grid[4], self.grid[7]]
        ver3 = [self.grid[2], self.grid[5], self.grid[8]]
        diag1 = [self.grid[0], self.grid[4], self.grid[8]]
        diag2 = [self.grid[6], self.grid[4], self.grid[2]]
        victoryLines = [hor1, hor2, hor3, ver1, ver2, ver3, diag1, diag2]

        for line in victoryLines:
            if len(set(line)) == 1 and line[0] != '_': #check if all of the elements of a victory line are identical 
                self.victory = line[0]
                return 
    
    def showGrid(self) -> None:
        print(f'|{self.grid[0]}|{self.grid[1]}|{self.grid[2]}|')
        print(f'|{self.grid[3]}|{self.grid[4]}|{self.grid[5]}|')
        print(f'|{self.grid[6]}|{self.grid[7]}|{self.grid[8]}|')

if __name__ == "__main__":
    while True:
        ticTacToe = TicTacToe()
        ticTacToe.playGame()
        ticTacToe.displayWinner()