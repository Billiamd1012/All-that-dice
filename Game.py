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
            self.setPlayer(name)
        if self.__minPlayers > 1:
            print(f"How many players ({self.__minPlayers}-{self.__maxPlayers})?")
            try:
                numPlayers = int(input(">"))
                if numPlayers > self.__maxPlayers or numPlayers < self.__minPlayers:
                    raise TypeError
            except ValueError:
                print("Please enter a number")
                self.selectPlayers()
            except TypeError:
                print(f"Please enter a number between {self.__minPlayers} and {self.__maxPlayers}")
                self.selectPlayers()
            playerCount = 1
            while playerCount < numPlayers + 1:
                print("What is the name of player #" + str(playerCount) + "?")
                name = input(">")
                if self.setPlayer(name):
                    playerCount += 1
        self.startRound()
    def setPlayer(self, name):
        for player in self.allPlayers:
            if player.getName() == name:
                self._players[player] = self.bidChips(player)
                return True              
        print(f"There is no player named {name}")
        return False

    def bidChips(self, player):
        # will bid chips
        name = player.getName()
        print(f"How many chips would you bid {name} (1-{player.getChips()})?")
        try:
            chips = int(input(">"))
            if chips > player.getChips():
                raise TypeError
            if chips < 1:
                raise LookupError
            return chips
        except ValueError:
            print("Please enter a number")
            self.bidChips(player)
        except TypeError:
            print(f"Sorry, {name} doesn't have that many chips try entering a lower number")
            self.bidChips(player)
        except LookupError:
            print(f"Sorry, {name} must bid at least 1 chip")
            self.bidChips(player)


    def winner(self, player):
        # will cash out the winner and display winning message
        print(f"Congratulations {player.getName()}, you win!")
        for players in self._players:
            players[0].increaseChips(players[1])  

    def startRound(self):
        # will start the round
        print("Let the game begin!")
        self.nextRound()

    def endGame(self):
        # will end the game
        pass
    def getGameType(self):
        # will return the game type
        return self.__gameType
    
    def numDice(self):
        # will return the number of dice
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
        
    def playerThrow(self):
        # will throw the dice
        print("How strong will you throw (0-5)?")
        strength = input(">")
        strength = self._checkStrength(strength)
        if strength == False:
            self.playerThrow()
        return strength

class OddOrEven(Game):
    def __init__(self, players):
        gameType = "Odd or Even"
        numDice = 1
        minPlayers = 1
        maxPlayers = 1
        super().__init__(players, gameType, minPlayers, maxPlayers, numDice)
    
    def _playerGuess(self, player):
        # will get the players guess
        print(f"Hey {player.getName()}, Odd (o) or Even (e)?")
        guess = input(">")
        if guess != "o" and guess != "e":
            print("Invalid input")
            self._playerGuess(player)
        return guess

    def loser(self, player):
        # will display the losing message
        print(f"Sorry {player.getName()}, you lose!")

    def nextRound(self):
        # will start the next round
        currentRound = Round.Round(self._numDice)
        for player in self._players.keys():
            guess = self._playerGuess(player)
            strength = self.playerThrow()
            currentRound.rollDice()
            dieValue = currentRound.showDice(strength)[0]
            print(currentRound.showFaces())
            match guess:
                case "e":
                    if dieValue % 2 == 0:
                        self.winner(player)
                    else:
                        self.loser(player)
                case "o":
                    if dieValue % 2 == 1:
                        self.winner(player)
                    else:
                        self.loser(player)
            self.endGame()

class Bunco(Game):
    def __init__(self, players):
        gameType = "Bunco"
        numDice = 3
        minPlayers = 2
        maxPlayers = 4
        self.__roundNumber = 1
        self.__playerScores = {}
        super().__init__(players, gameType, minPlayers, maxPlayers, numDice)
    def startRound(self):
        print("Let the game begin!")
        for i in range(6):
            self.nextRound()
            self.__roundNumber += 1

    def nextRound(self):
        # will start the next round
        print(f"<Round {self.__roundNumber}>")
        currentRound = Round.Round(self._numDice)
        roundWinner = {"":0}
        # loop through players 
        for player in self._players:
            playerRoundScore = 0
            print(f"It's {player[0].getName()}'s turn")
            while playerRoundScore < 21:
                strength = self.playerThrow()
                currentRound.rollDice()
                dieValues = currentRound.showDice(strength)
                print(currentRound.showFaces())
                # check for bunco
                turnScore = 0
                if dieValues[0] == dieValues[1] == dieValues[2]:
                    if dieValues[0] == self.__roundNumber:
                        print("Bunco!")
                        turnScore += 21
                    else:
                        print("Mini Bunco!")
                        turnScore += 5
                if dieValues[0] == self.__roundNumber:
                    turnScore += 1
                if dieValues[1] == self.__roundNumber:
                    turnScore += 1
                if dieValues[2] == self.__roundNumber:
                    turnScore += 1
                playerRoundScore += turnScore
                print(f"You earned {turnScore} points, {playerRoundScore} points in total.")
                if turnScore == 0:
                    break
            self.__playerScores[player] = playerRoundScore
            if playerRoundScore > roundWinner[list(roundWinner.keys())[0]]:
                roundWinner = {player:playerRoundScore}
            elif playerRoundScore == roundWinner[list(roundWinner.keys())[0]]:
                roundWinner = {max(self.__playerScores, key=lambda key: self.__playerScores[key])}

class Maxi(Game):
    def __init__(self, players):
        gameType = "Maxi"
        numDice = 2
        minPlayers = 3
        maxPlayers = 5
        super().__init__(players, gameType, minPlayers, maxPlayers, numDice)


# testOddOrEven = OddOrEven([Player.Player("Bill"), Player.Player("Bob")])
# testOddOrEven.setPlayer("Bill")

testBunco = Bunco([Player.Player("Bill"), Player.Player("Bob"), Player.Player("Bobby")])
testBunco.selectPlayers()