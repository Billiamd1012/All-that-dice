#
# File: Round.py
# Description: Module that controls the running of a round within a game
# Author: William Darker
# Student ID: 110398100
# Email ID: darws001
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#
import Die

class Round():
    def __init__(self, numDice):
        self.__dice = []
        self.__dieValues = []
        self.__numDice = numDice
        for i in range(self.__numDice):
            self.__dice.append(Die.Die())
    def rollDice(self):
        # will roll the dice
        for die in self.__dice:
            die.roll()
    def showDice(self,strength):
        self.__clearRound()
        # will show the dice
        for die in self.__dice:
            dieFinal = die.getValue() + strength
            if dieFinal > 6:
                dieFinal = dieFinal - 6
            self.__dieValues.append(dieFinal)
        return self.__dieValues
    def showFaces(self):
        # will show the die faces
        dieFaces = ""
        for value in self.__dieValues:
            match value:
                case 1:
                    dieFaces += "⚀"
                case 2:
                    dieFaces += "⚁"
                case 3:
                    dieFaces += "⚂"
                case 4:
                    dieFaces += "⚃"
                case 5:
                    dieFaces += "⚄"
                case 6:
                    dieFaces += "⚅"
        return dieFaces
    def __clearRound(self):
        # will clear the round
        self.__dieValues = []

