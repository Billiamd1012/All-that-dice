#
# File: AllThatDice.py
# Description: Entry point for the application that will control the menu and handle global variables
# Author: William Darker
# Student ID: 110398100
# Email ID: darws001
# This is my own work as defined by 
#    the University's Academic Misconduct Policy.
#
from Game import OddOrEven, Maxi, Bunco
import Player


class AllThatDice:
    def __init__(self):
        self.players = []
        self.__games = []
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
        for player in self.players:
            if player.getName() == name:
                print("Sorry, the name is already taken.\n")
                self.run()
        self.players.append(Player.Player(name))
        print("Welcome, " + name + "!\n")
        self.run()
    def showLeaderBoard(self):
        # will show the leaderboard
        print("=============================")
        print("Name       Played  Won  Chips")
        print("=============================")
        for player in self.players:
            # get games played and won
            gamesPlayed = 0
            gamesWon = 0
            for game in self.__games:
                if player in game[0]:
                    gamesPlayed += 1
                if player == game[1]:
                    gamesWon += 1
            print(player.getName() + " "*(11-len(player.getName())) + " "*(6-len(str(gamesPlayed))) + str(gamesPlayed) +" "*(5-len(str(gamesWon))) + str(gamesWon) + " "*(7-len(str(player.getChips())))+ str(player.getChips()))
        print("=============================")
        self.run()
    def playGame(self):
        # will start a game and register the players
        print("Which game would you like to play? \n(o) Odd-or-Even \n(m) Maxi \n(b) Bunco")
        gameType = input(">")
        if gameType == "o":
            if len(self.players) >= 1:
                self.__currentGame = OddOrEven(self.players)
                print("Let’s play the game of " + self.__currentGame.getGameType() + "!")
            else:
                print("Not enough players to play Odd or Even.")
                self.run()
        elif gameType == "m":
            if len(self.players) >= 3:
                self.__currentGame = Maxi(self.players)
                print("Let’s play the game of " + self.__currentGame.getGameType() + "!")
            else:
                print("Not enough players to play Maxi.")
                self.run()
        elif gameType == "b":
            if len(self.players) >= 2:
                self.__currentGame = Bunco(self.players)
                print("Let’s play the game of " + self.__currentGame.getGameType() + "!")
            else:
                print("Not enough players to play Bunco.")
                self.run()
        else:
            print("Invalid input")
        
        # register players
        self.__currentGame.selectPlayers()
        self.__games.append(self.__currentGame.getWinner())
        self.run()
    def quit(self):
        # will quit the application
        print("Thank you for playing All-That-Dice!")


my_all_that_dice = AllThatDice()
my_all_that_dice.run()
