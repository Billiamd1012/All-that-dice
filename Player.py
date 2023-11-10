#
# File: Player.py
# Description: Module that controls the running of a player
# Author: William Darker
# Student ID: 110398100
# Email ID: darws001
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#

class Player():
    def __init__(self, name):
        self.__name = name
        self.__chips = 100
    def getName(self):
        return self.__name
    def getChips(self):
        return self.__chips
    def increaseChips(self, amount):
        self.__chips += amount
    def decreaseChips(self, amount):
        if self.__chips - amount < 0:
            return False
        self.__chips -= amount