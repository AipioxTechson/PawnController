from Game import *
from Players import *

def generateGrid(size,player_one_t,player_two_t):
    grid = []
    p1_pieces = []
    p2_pieces = []
    for row in range(size):
        grid_column = []
        for column in range(size):
            if row == 0:
                piece = Piece(row,column,player_one_t)
                grid_column.append(piece)
                p1_pieces.append(piece)
            elif row == size - 1:
                piece = Piece(row,column,player_two_t)
                grid_column.append(piece)
                p2_pieces.append(piece)
            else:
                grid_column.append(Piece(row,column," "))
        grid.append(grid_column)
    return (grid,p1_pieces,p2_pieces)



total,gamemode, playAgain = 0,0, True
player1, player2, player1Score, player2Score = None, None, 0,0
Token1, Token2 = "X", "Y"

#Asks for Input
print("Welcome to nPawn!")
print("How many Pawns?")
try:
    total = int(input())
except ValueError:
    total = 3

if total < 2:
    total = 3
    
print("What gamemode?: (1) PvP (2) PvC")
try:
    gamemode = int(input())
except ValueError:
    gamemode = 1
    
if gamemode < 0 or gamemode >= 3:
    gamemode = 1
    

while playAgain:
    grid,p1_pieces,p2_pieces = generateGrid(total,Token1,Token2)
    
    #Sets up Gamemode
    if gamemode == 1:
        player1 = HumanPlayer(Token1,p1_pieces,grid,1)
        player2 = HumanPlayer(Token2,p2_pieces,grid,2)
    else:
        player1 = HumanPlayer(Token1,p1_pieces,grid,1)
        player2 = ComputerPlayer(Token2,p2_pieces,grid,2)
        
    #Main Game
    CurrentGame = Game(player1,player2,grid)
    while (not CurrentGame.isWin()):
        CurrentGame.printState()
        
        newMove,player = CurrentGame.nextMove()
        CurrentGame.ApplyMove(newMove,player)
    
    if CurrentGame.getWinner().player_number == 1:
        player1Score += 1
    else:
        player2Score += 1
        
    print("Current Score: "+" X: "+str(player1Score) +" Y: " + str(player2Score))
    validInput = False
    while not validInput:
        print("Do you want to play again? Y/N")
        againInput = input()
        if againInput == "Y":
            validInput = True
            playAgain = True
        elif againInput == "N":
            validInput = True
            playAgain = False
    
        
