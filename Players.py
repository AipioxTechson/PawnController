class Player:
    '''Responsible for creating the Abstract Player
    Variables:
    Token
    pieces
    grid
    playerNumber
    Functions:
    getToken()
    getPieces()
    getAvailableMoves(Piece)
    nextMove()
    processData()
    
    '''
    def __init__(self,Token,pieces,grid,player_number):
        self.Token = Token
        self.pieces = pieces
        self.grid = grid
        self.player_number = player_number
    
    def getToken(self):
        return self.Token
    
    def getPieces(self):
        return self.pieces
    
    def getAvailableMoves(self,Piece):
        #TODO:Finish function
        return []
    
    def nextMove(self):
        pass
    
    def processData(self):
        #Responsible for updating Data
        pass
    
    
    
class HumanPlayer(Player):
    '''Responsible for handling Human input for Player
    Subclass to Player
    '''
    def __init__(self,Token,pieces,grid,player_number):
        Player.__init__(self,Token,pieces,grid,player_number)
        
        
    def processData(self,winValue):
        if winValue:
            print("Congrats! " + self.Token + " wins!")
        else:
            print("Sorry! " + self.Token + " lost!")
        
        
class ComputerPlayer(Player):
    '''Responsible for handling ComputerInput for Player
    Subclass to Player
    '''
    def __init__(self,Token,pieces,grid,player_number):
        Player.__init__(self,Token,pieces,grid,player_number)