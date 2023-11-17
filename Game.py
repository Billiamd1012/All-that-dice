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

class Game:
    def __init__(self, players, gameType, minPlayers, maxPlayers, numDice):
        self._players = {}
        self.__rounds = []
        self.__gameType = gameType
        self.__minPlayers = minPlayers
        self.__maxPlayers = maxPlayers
        self._numDice = numDice
        self.allPlayers = players

    def selectPlayers(self):
        if self.__minPlayers == 1:
            print("What is the name of the player ?")
            name = input(">")
            self.registerPlayer(name)
        if self.__minPlayers > 1:
            print(f"How many players ({self.__minPlayers}-{self.__maxPlayers})?")
            numPlayers = input(">")
            for i in range(numPlayers):
                print("What is the name of player #" + str(i) + "?")
                name = input(">")
                self.registerPlayer(name)
    def registerPlayer(self, name):
        for player in self.allPlayers:
            if player.getName() == name:
                print(f"How many chips would you bid {name} (1-{player.getChips()})?")
                chips = int(input(">"))
                if chips > player.getChips():
                    print(f"Sorry, {name} doesn't have that many chips try entering a lower number")
                    self.registerPlayer(name)
                else:
                    try: 
                        chips = int(chips)
                        self._players[player] = chips
                        self.startRound()
                    except ValueError:
                        print("Please enter a number")
                        self.registerPlayer(name)
            else:                
                print(f"There is no player named {name}")

    def bidChips(self, player, bid):
        # will bid chips
        pass
    def cashOutWinner(self, player):
        # will cash out the winner
        pass
    def startRound(self):
        # will start the round
        print("Let the game begin")
        self.nextRound()

    def endGame(self):
        # will end the game
        pass
    def getGameType(self):
        return self.__gameType
    def numDice(self):
        return self._numDice
    def _checkStrength(self, strength):
        # will check the strength of the throw
        try:
            strength = int(strength)
            if strength < 1 or strength > 5:
                raise ValueError
            return strength
        except ValueError:
            print("Try entering a number between 1 and 5")
            return False
        except TypeError:
            print("Try entering a number")
            return False

class OddOrEven(Game):
    def __init__(self, players):
        gameType = "Odd or Even"
        numDice = 1
        minPlayers = 1
        maxPlayers = 1
        super().__init__(players, gameType, minPlayers, maxPlayers, numDice)
    
    def _playerGuess(self, player):
        print(f"Hey {player.getName()}, Odd (o) or Even (e)?")
        guess = input(">")
        if guess != "o" or guess != "e":
            print("Invalid input")
            self._playerGuess(player)
        return guess
    
    def _playerThrow(self):
        print("How strong will you throw (0-5)?")
        strength = input(">")
        strength = self._checkStrength(strength)
        if strength == False:
            self._playerThrow()
        return strength
        
    def nextRound(self):
        # will start the next round
        currentRound = Round.Round(self._numDice)
        for player in self._players.keys():
            guess = self._playerGuess(player)
            strength = self._playerThrow()
            currentRound.rollDice(self.numDice(), strength)
            currentRound.showFaces()
            dieValue = currentRound.showDice()[0]
            match guess:
                case "e":
                    if dieValue % 2 == 0:
                        print("You win!")
                        player.increaseChips(self._players[player])
                    else:
                        print("You lose!")
                        player.decreaseChips(self._players[player])
                case "o":
                    if dieValue % 2 == 1:
                        print("You win!")
                        player.increaseChips(self._players[player])
                    else:
                        print("You lose!")
                        player.decreaseChips(self._players[player])

class Bunco(Game):
    def __init__(self, players):
        gameType = "Bunco"
        numDice = 3
        minPlayers = 2
        maxPlayers = 4
        super().__init__(players, gameType, minPlayers, maxPlayers, numDice)

class Maxi(Game):
    def __init__(self, players):
        gameType = "Maxi"
        numDice = 2
        minPlayers = 3
        maxPlayers = 5
        super().__init__(players, gameType, minPlayers, maxPlayers, numDice)


# test case

players = [Player.Player("Will"), Player.Player("Bob"), Player.Player("Joe"), Player.Player("Bill")]

game = OddOrEven(players)
game.selectPlayers()