#
# File: Game.py
# Description: Module that controls the running of a game
# Author: William Darker
# Student ID: 110398100
# Email ID: darws001
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#
import Round
import Player

class Game():
    def __init__(self):
        self.__players = {}
        self.__rounds = []
        self.__gameType = None
    def selectGameType(self):
        # will select the game type
        print("Which game would you like to play? \n(o) Odd-or-Even \n(m) Maxi \n(b) Bunco")
        gameType = input(">")
        if gameType == "o":
            self.__gameType = OddOrEven(self)
        elif gameType == "m":
            self.__gameType = Maxi(self)
        elif gameType == "b":
            self.__gameType = Bunco(self)
        else:
            print("Invalid input")
            self.selectGameType()
    def registerPlayer(self, name):
        # will add a player to the game
        pass
    def bidChips(self, player, bid):
        # will bid chips
        pass
    def cashOutWinner(self, player):
        # will cash out the winner
        pass
    def invalidPlayer(self):
        # will handle an invalid player
        pass
    def nextRound(self):
        # will start the next round
        pass
    def endGame(self):
        # will end the game
        pass


class OddOrEven(Game):
    def __init__(self) -> None:
        pass


class Bunco(Game):
    def __init__(self) -> None:
        pass

class Maxi(Game):
    def __init__(self) -> None:
        pass