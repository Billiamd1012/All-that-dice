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
    def selectGameType(self, gameType):
        # will select the game type
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