#
# File: Die.py
# Description: Module that controls the rolling and displaying of a die
# Author: William Darker
# Student ID: 110398100
# Email ID: darws001
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#
import random

class Die():
    def roll(self):
        # will roll the die
        self.__value = random.randint(1, 6)
    def getValue(self):
        # will return the value of the die
        return self.__value