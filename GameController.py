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

def playGame(gamemode,C1Mode,C2Mode,Training,Token1,Token2):
    grid,p1_pieces,p2_pieces = generateGrid(total,Token1,Token2)
    #Sets up Gamemode
    if gamemode == 1:
        player1 = HumanPlayer(Token1,p1_pieces,grid,1)
        player2 = HumanPlayer(Token2,p2_pieces,grid,2)
    elif gamemode == 2:
        player1 = HumanPlayer(Token1,p1_pieces,grid,1)
        player2 = ComputerPlayer(Token2,p2_pieces,grid,2,C1Mode,Training)
    else:
        player1 = ComputerPlayer(Token1,p1_pieces,grid,1,C1Mode,Training)
        player2 = ComputerPlayer(Token2,p2_pieces,grid,2,C2Mode,Training)
        
    CurrentGame = Game(player1,player2,grid,Training)
    while (not CurrentGame.isWin()):
        if not Training:
            CurrentGame.printState()
        
        newMove,player = CurrentGame.nextMove()
        CurrentGame.ApplyMove(newMove,player)
    return CurrentGame
        
        
total,gamemode, playAgain, C1Mode,C2Mode, Training,amountOfTraining = 0,0, True, None, None, False, 0
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
    
print("What gamemode?: (1) PvP (2) PvC (3) CvC")
try:
    gamemode = int(input())
except ValueError:
    gamemode = 1
    
if gamemode < 0 or gamemode > 3:
    gamemode = 1
    
if gamemode ==2 or gamemode == 3:
    C1Mode = input("What ComputerPlayer1 Mode? Addition, Subtraction, Mixed\n")
    if C1Mode != "Addition" and C1Mode != "Subtraction" and C1Mode !="Mixed":
        C1Mode = "Addition"
if gamemode == 3:
    
    C2Mode = input("What ComputerPlayer2 Mode? Addition, Subtraction, Mixed\n")
    if C2Mode != "Addition" and C2Mode != "Subtraction" and C2Mode !="Mixed":
        C2Mode = "Subtraction"
    response = input("Do you want to train the bot? Y|N")
    if response == "Y":
        Training = True
        try:
            amountTraining = int(input("How many Rounds?"))
        except:
            amountTraining = 10
        if amountTraining < 0:
            amountTraining = 10
        
if Training:
    for i in range(amountTraining):
        playGame(gamemode,C1Mode,C2Mode,True,Token1,Token2)
while playAgain and not Training:
    CurrentGame = playGame(gamemode,C1Mode,C2Mode,False,Token1,Token2)
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
    
        
