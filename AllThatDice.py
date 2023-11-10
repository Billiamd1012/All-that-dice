#
# File: AllThatDice.py
# Description: Entry point for the application that will control the menu and handle global variables
# Author: William Darker
# Student ID: 110398100
# Email ID: darws001
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#
import Game
import Player


class AllThatDice():
    def __init__(self):
        self.__players = []
        self.__previousGames = []
        self.__currentGame = None
        self.runText = "What would you like to do?\n (r) register a new player\n (s) show the leader board\n (p) play a game\n (q) quit"
        print("Welcome to All-That-Dice!\nDeveloped by Alan Turing\nCOMP 1048 Object-Oriented Programming")
    def run(self):
        # will start the appilcation
        print(self.runText)
        startSelection = input(">")
        match startSelection:
            case "r":
                print("What is the name of the new player?")
                name = input(">")
                self.registerPlayer(name)
            case "s":
                self.showLeaderBoard()
            case "p":
                self.playGame()
            case "q":
                self.quit()
            case _:
                print("Invalid input")
                self.run()
    def registerPlayer(self, name):
        # will register a player with the application
        for player in self.__players:
            if player.getName() == name:
                print("Sorry, the name is already taken.\n")
                self.run()
        self.__players.append(Player.Player(name))
        print("Welcome, " + name + "!\n")
        self.run()
    def showLeaderBoard(self):
        # will show the leaderboard
        pass
    def playGame(self):
        self.__currentGame = Game.Game()
    def quit(self):
        # will quit the application
        pass


my_all_that_dice = AllThatDice()
my_all_that_dice.run()
