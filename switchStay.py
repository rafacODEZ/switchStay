import random


class switchStay:
    def __init__(self):
        self.stats = Statistics()
        self.UI = Userinterface()
        self.cards = Cards()

    def playRound(self):
        sim = 0  # counter for simming up the different strings entered
        strategy = self.UI.askSwitchorStay()  # ask user if they want to switch or stay

        self.cards.showCards("all")  # shows all cards

        while sim != len(strategy):
            self.cards.hideCards()  # hides all the cards

            # player is asked to pick a card
            playersChoice = self.UI.pickCardQuestion()

            self.cards.setplayersChoice(playersChoice)  # stores the players choice

            self.cards.revealLoserCard()  # reveals a loser card

            # assigns stay or switch to decision
            decision = self.cards.StayorSwitch(strategy[sim])

            # adds to counter to change to next simmed game
            sim += 1

            # passes decision to check if its a win
            win = self.cards.winnerCard(decision)

            # if player wins the round, it increases wins and games simmed by 1
            if win == 1:
                self.stats.setWins(win)
                self.stats.setgamesSimed(1)

            # if player loses the round it increases games simmed by 1
            elif win == 0:
                self.stats.setgamesSimed(1)

        wins = self.stats.getWins()  # gets all the wins throughout game
        games = self.stats.getgamesSimed()  # gets all the games played
        percentage = self.stats.precentageOfWins()  # gets the percentage of wins

        self.UI.endgameResults(wins, games, percentage)  # prints out end results

    def playGame(self):
        self.UI.printIntro()  # prints intro to game

        game = self.UI.startGameQuestion()  # Asks user if they want to start a game

        while True:
            if game == True:
                self.UI.gamesHowToPlay()  # prints how to play info
                self.playRound()
                break

            else:
                # if game ends before it starts, displays zero wins,games, and percentage
                self.UI.endgameResults(wins=0, games=0, percentage=0)
                print("Thanks for playing")
                break


class Cards:
    def __init__(self):
        self.cards = ["Loser", "Loser", "Winner"]
        self.playerChoice = ""
        self.loserCard = ""
        self.shuffledCards = dict()

    def showCards(self, show):
        random.shuffle(self.cards)

    def hideCards(self):
        positions = ["1", "2", "3"]
        random.shuffle(positions)

        count = 0
        for pos in positions:
            self.shuffledCards[pos] = self.cards[count]
            count += 1

        hide = []
        for posit in self.shuffledCards.keys():
            hide.append(posit)

    def revealLoserCard(self):
        # reveals a loser card then removes it from dict
        for key, value in self.shuffledCards.items():
            if key == self.playerChoice:
                continue  # does nothing if loop lands on players choie of card
            elif value == "Loser":  # reveals a loser card to player
                self.shuffledCards.pop(key)
                break

    def setplayersChoice(self, choice):
        self.playerChoice = choice  # sets the players choice

    def StayorSwitch(self, choice):
        if choice == "S":  # if the player stays then nothing happens
            self.playerChoice = self.playerChoice
            return self.playerChoice
        elif choice == "W":
            for card in self.shuffledCards:
                if card != self.playerChoice:
                    self.playerChoice = card
                    return self.playerChoice

    def winnerCard(self, choice):
        # decies if the player has won or lost
        # depending on their choice
        if self.shuffledCards[choice] == "Winner":
            return 1
        else:
            return 0


class Statistics:
    def __init__(self):
        self.wins = 0
        self.gamesSimed = 0

    def getWins(self):
        return self.wins

    def getgamesSimed(self):
        return self.gamesSimed

    def setWins(self, win):
        self.wins += win

    def setgamesSimed(self, games):
        self.gamesSimed += games

    def precentageOfWins(self):
        percentage = self.wins / self.gamesSimed
        return percentage


class Userinterface:
    def printIntro(self):
        print()
        print()
        startGameMSG = (
            " ***************************************************************"
            + "\n *                                                             *"
            + "\n *              - Welcome To Switch or Stay -                  *"
            + "\n *                                                             *"
            + "\n *    Three cards are shown to the player, only one is a       *"
            + "\n *     winning card. The dealer randomly places the cards      *"
            + "\n *    facing down so the player doesn't know which card is     *"
            + "\n *   the winning card, but the dealer does. The player picks   *"
            + "\n *    a card they think is a winning card. Then the dealer     *"
            + "\n *  turns over a card revealing a losing card. At this point   *"
            + "\n *   the players strategy comes into effect. If the player     *"
            + "\n *   decides correctly and ends up picking the winning card,   *"
            + "\n *      the player wins the round. At the end of the game      *"
            + "\n *          the results are printed out to the player.         *"
            + "\n *                                                             *"
            + "\n *                        Good luck!                           *"
            + "\n *              May the odds be in your favor.                 *"
            + "\n *                                                             *"
            + "\n ***************************************************************"
        )
        print()
        print(startGameMSG)
        print()

    def gamesHowToPlay(self):
        print()
        print()
        howToMSG = (
            " ***************************************************************"
            + "\n *                                                             *"
            + "\n *                   - How To Play -                           *"
            + "\n *                                                             *"
            + "\n *     After starting the game, You will be prompted to        *"
            + "\n *     enter a string with a strategy you think will get       *"
            + "\n *                 you the most wins.                          *"
            + "\n *                                                             *"
            + "\n *           'S' for Stay and 'W' for switch.                  *"
            + "\n *                                                             *"
            + "\n *               For Example: SWSSWWW                        *"
            + "\n *                                                             *"
            + "\n ***************************************************************"
        )
        print()
        print(howToMSG)
        print()

    def startGameQuestion(self):

        while True:
            print()
            user = input("Start Game (yes or no)?  ").lower()

            if user == "yes":
                return True

            elif user == "no":
                return False

            else:
                print("Invalid Input!")
                continue

    def pickCardQuestion(self):
        user = random.randint(1, 3)

        return str(user)

    def askSwitchorStay(self):
        strategy = []

        while True:
            user = input("Enter your strategy: ")
            try:
                for string in user:
                    if (string != "S") and (string != "W"):
                        raise Exception

                    elif string == "S" or string == "W":
                        strategy.append(string)
                else:
                    break
            except:
                print("Invalid Input!")
                print()
                strategy = []

        return strategy

    def endgameResults(self, wins, games, percentage):
        print()
        results = f"You have won {wins} games!\n"
        results += f"You played {games} games!\n"
        results += f"Your percentage of wins is {percentage:.1%}!"
        print(results)


if __name__ == "__main__":
    switchStay()

s = switchStay()
s.playGame()
