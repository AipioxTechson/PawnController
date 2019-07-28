from Game import *
from Players import *

def generateGrid(size,
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
