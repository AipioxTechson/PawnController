class Game:
    """Responsible for holding the state of the Game.
    
    Functions:
    isWin()
    nextMove()
    printState()
    
    """

    def __init__(self,player1: "Player" ,player2: "Player", grid = []):
        self.grid = grid
        self.turn = 0
        self.player_one = player1
        self.player_two = player2
    
    def isWin(self):
        pass
    
    def nextMove(self):
        pass
    
    def printState(self):
        pass
                
            
        