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
        self.__gameType = gameType
        self.__minPlayers = minPlayers
        self.__maxPlayers = maxPlayers
        self._numDice = numDice
        self.allPlayers = players

    def selectPlayers(self):
        if self.__minPlayers == 1:
            print("What is the name of the player ?")
            name = input(">")
            self.__setPlayer(name)
        elif self.__minPlayers > 1:
            print(f"How many players ({self.__minPlayers}-{self.__maxPlayers})?")
            try:
                numPlayers = int(input(">"))
                if numPlayers > self.__maxPlayers or numPlayers < self.__minPlayers or numPlayers > len(self.allPlayers):
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
                if self.__setPlayer(name):
                    playerCount += 1
        self.startRound()
    def __setPlayer(self, name):
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


    def endGame(self, winner):
        # will cash out the winner and display winning message
        print(f"Congratulations {winner.getName()}, you win!")
        # get the sum of the pot
        pot = 0
        for player in self._players:
            pot += self._players[player]
        for player in self._players.keys():
            if player == winner:
                player.increaseChips(pot)
            else:
                player.decreaseChips(self._players[player])
        self.__winner = winner
    def getWinner(self):
        players = []
        for player in self._players:
            players.append(player)
        return [players, self.__winner]
    def startRound(self):
        # will start the round
        print("Let the game begin!")
        self.nextRound()

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
                        self.endGame(player)
                    else:
                        self.loser(player)
                case "o":
                    if dieValue % 2 == 1:
                        self.endGame(player)
                    else:
                        self.loser(player)

class Bunco(Game):
    def __init__(self, players):
        gameType = "Bunco"
        numDice = 3
        minPlayers = 2
        maxPlayers = 4
        super().__init__(players, gameType, minPlayers, maxPlayers, numDice)
        self.__roundNumber = 1
        self.__playerScores = {}

    def setPlayerScores(self):
        for player in self._players:
            self.__playerScores[player] = [[], 0, 0, 0]
    
    def startRound(self):
        self.setPlayerScores()
        print("Let the game begin!")
        for i in range(6):
            self.nextRound()
            self.__roundNumber += 1
        self.showGameSummary()

    def nextRound(self):
        # will start the next round
        print(f"<Round {self.__roundNumber}>")
        currentRound = Round.Round(self._numDice)
        roundWinner = {"":-1}
        # loop through players 
        for player in self._players:
            playerRoundScore = 0
            playerRoundBuncos = 0
            print(f"It's {player.getName()}'s turn")
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
                        playerRoundBuncos += 1
                        turnScore += 21
                    else:
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
            gameScore = self.__playerScores[player][1] + playerRoundScore
            buncos = self.__playerScores[player][2] + playerRoundBuncos

            self.__playerScores[player][0].append(playerRoundScore)
            self.__playerScores[player][1] = gameScore
            self.__playerScores[player][2] = buncos
            
            if playerRoundScore > roundWinner[list(roundWinner.keys())[0]]:
                roundWinner = {player:playerRoundScore}
            elif playerRoundScore == roundWinner[list(roundWinner.keys())[0]]:
                roundWinner = {max(self.__playerScores, key=lambda key: self.__playerScores[key][0][self.__roundNumber-1]): self.__playerScores[max(self.__playerScores, key=lambda key: self.__playerScores[key][0][self.__roundNumber-1])]}
        if roundWinner[list(roundWinner.keys())[0]] == 0:
            print("It was a tie this round")
        else:
            first_key, _ = next(iter(roundWinner.items()), (None, None))
            print(f"{first_key.getName()} is the winner in Round {self.__roundNumber}!")
            self.__playerScores[first_key][3] += 1

    def showGameSummary(self):
        # will show the game summary
        playerCount = len(self.__playerScores)
        playerNames = []
        roundScores = []
        totalScores = []
        buncos = []
        for player in self.__playerScores:
            playerNames.append(player.getName())
            roundScores.append(self.__playerScores[player][0])
            totalScores.append(self.__playerScores[player][1])
            buncos.append(self.__playerScores[player][2])
        print("====="+"=========="*(playerCount))
        nameOutput = "Round"
        for player in playerNames:
            nameOutput += " "*(10-len(player))+ f"{player}"
        print(nameOutput)
        print("====="+"=========="*(playerCount))
        for i in range(6):
            roundOutput = f"    {i+1}"
            for j in range(playerCount):
                roundOutput += " "*(10-len(str(roundScores[j][i]))) + f"{roundScores[j][i]}"
            print(roundOutput)
        print("====="+"=========="*(playerCount))
        totalOutput = "Total"
        for i in range(playerCount):
            totalOutput += " "*(10-len(str(totalScores[i]))) + f"{totalScores[i]}"
        print(totalOutput)
        print("====="+"=========="*(playerCount))
        buncoOutput = "Buncos"
        for i in range(playerCount):
            if i == 0:
                buncoOutput += " "*(9-len(str(buncos[i]))) + f"{buncos[i]}" 
            else:
                buncoOutput += " "*(10-len(str(buncos[i]))) + f"{buncos[i]}" 
        print(buncoOutput)
        print("====="+"=========="*(playerCount))
        winner = self._findWinner()
        if winner != False:
            print(f"{winner.getName()} won {self.__playerScores[winner][3]} rounds, scoring {self.__playerScores[winner][1]} points, with {self.__playerScores[winner][2]} Buncos.")
        self.endGame(winner)
        
    def _findWinner(self):
        # will find the winner
        #first check self.__playerScores to see if someone has won the most number of rounds
        #if not check self.__playerScores to see if someone has the highest score
        #if not check self.__playerScores to see if someone has the most buncos
        #if not print a tie between the players
        winner = None
        for player in self.__playerScores:
            if winner == None:
                winner = player
            elif self.__playerScores[player][3] > self.__playerScores[winner][3]:
                winner = player
            elif self.__playerScores[player][3] == self.__playerScores[winner][3]:
                if self.__playerScores[player][1] > self.__playerScores[winner][1]:
                    winner = player
                elif self.__playerScores[player][1] == self.__playerScores[winner][1]:
                    if self.__playerScores[player][2] > self.__playerScores[winner][2]:
                        winner = player
                    elif self.__playerScores[player][2] == self.__playerScores[winner][2]:
                        print("Tie between " + player.getName() + " and " + winner.getName())
                        return False
        return winner


class Maxi(Game):
    def __init__(self, players):
        gameType = "Maxi"
        numDice = 2
        minPlayers = 3
        maxPlayers = 5
        super().__init__(players, gameType, minPlayers, maxPlayers, numDice)
        self.__playersLeft = []
    
    def testSetPlayerLeft(self):
        self._players = {Player.Player("Bill"):50, Player.Player("Bob"):50, Player.Player("Bobby"):50}

    def startRound(self):
        # will start the round
        for player in self._players:
            self.__playersLeft.append(player)
        print("Let the game begin!")
        while len(self.__playersLeft) > 1:
            self.nextRound()
            if len(self.__playersLeft) == 1:
                self.endGame(self.__playersLeft[0])
                break
            playersLeft = ""
            for player in self.__playersLeft:
                playersLeft += ", " +player.getName()
            print(f"Players remaining: {playersLeft[2:]}")

    def nextRound(self):
        # will start the next round
        currentRound = Round.Round(self._numDice)
        playerScores = {}
        for player in self.__playersLeft:
            print(f"It's {player.getName()}'s turn")
            strength = self.playerThrow()
            currentRound.rollDice()
            dieValues = currentRound.showDice(strength)
            print(currentRound.showFaces())
            playerScores[player] = sum(dieValues)
        # find max score from player scores then remove all players from self.__playersLeft that don't have that score
        maxScore = max(playerScores, key=lambda key: playerScores[key])
        for player in self.__playersLeft:
            if playerScores[player] != playerScores[maxScore]:
                self.__playersLeft.remove(player)


# testOddOrEven = OddOrEven([Player.Player("Bill"), Player.Player("Bob")])
# testOddOrEven.setPlayer("Bill")

#testBunco = Bunco([Player.Player("Bill"), Player.Player("Bob"), Player.Player("Bobby")])
#testBunco.selectPlayers()
# testBunco.TestSetPlayerScores()
# testBunco.showGameSummary()

# players = {Player.Player("Bill"): 10, Player.Player("Bob"): 20, Player.Player("Bobby"): 30}
# # print(max(players, key=lambda key: players[key]).getName())
# roundWinner = {max(players, key=lambda key: players[key]): players[max(players, key=lambda key: players[key])]}
# first_key, _ = next(iter(roundWinner.items()), (None, None))
# print(first_key)


def testMaxi():
    maxiTest = Maxi([Player.Player("Bill"), Player.Player("Bob"), Player.Player("Bobby")])
    maxiTest.testSetPlayerLeft()
    maxiTest.startRound()

if __name__ == "__main__":
    testMaxi()