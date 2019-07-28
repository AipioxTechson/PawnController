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



total,gamemode = 0,0
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
    
    
player1, player2 = None, None
grid,p1_pieces,p2_pieces = generateGrid(total,"X","Y")
s = Game(player1,player2,grid)
s.printState()
