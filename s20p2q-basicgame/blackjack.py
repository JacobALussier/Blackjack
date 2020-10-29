import random as rn
import card
import dealer
import deck as d
import entity
import hand
import player as p
import table
import GUI

from os import system, name

'''Blackjack - CSC305 Project
-Cory Cothrum

-Denzell Rodriguez
-Matthew McNamee
-Alex Fisk 

Game
-Rounds
--Dealer
---Hand
--Player
---Hand
---Bets
--Deck
---Cards
----Suit, Value, Facing
--Win, Lose
'''
'''Graphical User Interface Menu File
Implemented by Jacob Lussier
March 2,2020'''

from tkinter import *
from PIL import Image
from PIL import ImageTk


def gameSetup(decks:int = 8):
    print("Setting up a table for you...")
    houseDealer = dealer.Dealer()
    playTable = table.Table()
    houseDealer.table = playTable
    playTable.dealer = houseDealer
    playDeck = houseDealer.make_deck(decks)
    playDeck.shuffle(7)
    playTable.deck = playDeck
    inname = input("Please enter player name: ")
    badinput = True
    while badinput:
        inbank = input("Please enter the starting bank value: ")
        try:
            inbank = int(inbank)
            if inbank > 0:
                badinput = False
        except:
            print("Invalid value")
    playTable.players.append(p.Player(bank = inbank, name = inname))
    return playTable


def playhit(player, playTable):
    playTable.dealer.deal(player)
    player.getHand()
    player.getTotal()

def playstand(player, playTable):
    player.standing = True
    print(f"{player.name} is standing this round")

def playdouble(player, playTable):
    doubleSuccess = player.betting(bet = player.bet, double = True)
    if doubleSuccess:
        playTable.dealer.deal(player, num = 1)
        player.getHand()
        player.getTotal()
        player.standing = True
    else:
        print("You dont have enough money in the bank for that.")


'''gameRound()
Handles each round of play. 
'''
def gameRound(playTable, roundnum):
    print(f"Round {roundnum}")
    #get initial bet
    print("Initial bets.")
    for player in playTable.players:
        print(f"{player.name} has {player.bank} in the bank.")
        player.betting()
    print("Dealing...")
    for player in playTable.players:
        playTable.dealer.deal(player, num = 2)
        player.getHand()
        player.getTotal()
    playTable.dealer.deal(playTable.dealer, num = 2)
    playTable.dealer.getHand(num = 1)
    playTable.dealer.getTotal(num = 1)
    #check for blackjack already, and see if player wants to doubledown
    if playTable.dealer.blackjack:
        print("The dealer already has 21! The house wins!")
        for player in playTable.players:
            playTable.dealer.bank += player.bet
            player.bet = 0
        return
    double = input("Would you like to double down? (y/n)")
    if double.lower()[0] == "y":
        playdouble(player, playTable)
    #get player input
    allbusted = False
    dealerstanding = False
    while not allbusted:
        allbusted = True
        allStanding = True
        #player turns
        for player in playTable.players:
            if player.blackjack:
                print(f"{player.name} has Blackjack! They win the round!")
                player.bank += 2*player.bet
                player.bet = 0
                return
            if player.bust == False and player.standing == False:
                allbusted = False
                allStanding = False
                print(f"{player.name}'s turn:")
                badinput = True
                while badinput:
                    playerchoice = input("What would you like to do? (h)it, (s)tand: ")
                    if playerchoice == "h":
                        badinput = False
                        playhit(player, playTable)
                        if player.bust:
                            print(f"{player.name} has busted out!")
                            playTable.dealer.bank += player.bet
                            player.bet = 0
                        if player.blackjack:
                            print(f"{player.name} has Blackjack! They win the round!")
                            player.bank += 2*player.bet
                            player.bet = 0
                            return
                    elif playerchoice == "s":
                        badinput = False
                        playstand(player, playTable)
                    else:
                        print("Invalid input")
            else:
                print(f"{player.name} is busted out!")
        for player in playTable.players:
            allbusted = True
            if player.bust == False:
                allbusted = False
        if allbusted:
            break
        #dealers turn
        dealerVal = playTable.dealer.getTotal(verbose = False)
        if dealerVal[1] <= 21:
            dealerVal = dealerVal[1]
        else:
            dealerVal = dealerVal[0]        
        if playTable.dealer.blackjack:
            playTable.dealer.getHand()
            playTable.dealer.getTotal()
            print("The house wins!")
            for player in playTable.players:
                playTable.dealer.bank += player.bet
                player.bet = 0
            return
        elif playTable.dealer.bust:
            print("The house has busted!")
            for player in playTable.players:
                player.bank += 2*player.bet
                player.bet = 0            
            return
        elif playTable.dealer.standing:
            print("The Dealer is standing")            
        else:
            if dealerVal < 17:
                print("The dealer takes a card")
                playTable.dealer.deal(playTable.dealer)
                playTable.dealer.getHand(num = 1)
                playTable.dealer.getTotal(num = 1)
            elif dealerVal >= 17:
                print("The Dealer is standing")
                playTable.dealer.standing = True
        #Check if everyone is just standing
        if playTable.dealer.standing and allStanding:
            #get totals and the highest wins
            winner = playTable.dealer
            hightotal = dealerVal
            for player in playTable.players:
                if not player.bust:
                    playerVal = player.getTotal(verbose = False)
                    if playerVal[1] <= 21:
                        playerVal = playerVal[1]
                    else:
                        playerVal = playerVal[0]
                    if playerVal > hightotal:
                        hightotal = playerVal
                        winner = player
            print(f"The winner is {winner.name}!")
            winner.getHand()
            winner.getTotal()
            winner.bank += 2*winner.bet
            winner.bet = 0
            return
    print("All players have busted out. The house wins!")
    for player in playTable.players:
        playTable.dealer.bank += player.bet
        player.bet = 0
    return

def newGame():
    playTable = gameSetup()
    continueGame = "y"
    roundnum = 1
    while continueGame == "y":
        gameRound(playTable, roundnum)
        playTable.clear()
        for player in playTable.players:
            if player.bank <= 0:
                playTable.players.remove(player)
        if len(playTable.players) == 0:
            print("All players are bankrupt! The house wins!")
            continueGame = "n"
        else:
            continueGame = input("Would you like to play another round? (y/n): ").lower()
            roundnum += 1
            input("Press <ENTER> to continue")
            consoleclear()

def rules():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    valuesStr = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
    print("The game of Blackjack is a card game between the\nDealer and a number of players. The goal of the game is simple;\nget as close to 21 as you can through being dealt cards.\nThe value of the cards are:")
    for i in range(len(values)):
        if values[i] == 1:
            print("The Ace, worth either 1 or 11 points.")
        else:
            print(f"The {valuesStr[i]}, worth {values[i]} points.")
    print("The player must bet at the begining of a round before they are dealt cards. After this,\nthey can choose to double their bet and receive only one additional card.\nOtherwise, the player may choose to hit or stand. The dealer asks around the table\nuntil all players are standing, and then cards are revealed and\nthe winner is choosen to be closest to 21.\nThe house wins in a draw.\n")
    print("Would you like to know more? Press Q to exit.\n1. Hitting\n2. Standing\n3. 21\n4. Busting\n5. Aces\n(Q)uit\n")
    incmd = "x"
    while incmd.lower() != "q":
        incmd = input("Please enter choice: ")
        if incmd == "1":
            print("The player may ask the dealer for a hit and recieve an additional card.\nThey may continue until they either reach 21 or exceed it,\nbusting out.")
        elif incmd == "2":
            print("The player may choose to stand, and stop receiving new cards in hand.\nThe dealer will stand on 17")
        elif incmd == "3":
            print("The goal of the game is to reach as close to if not 21,\nand there are several ways of getting there through card combinations.\nIn the event of a tie, the house always wins.")
        elif incmd == "4":
            print("If the player recieves a total greater then 21, they are busted out\nand lose their bet and hand. If all players bust out, the house wins.")
        elif incmd == "5":
            print("The aces is worth either 1 or 11, whichever gets you closest to 21.")
        elif incmd != "q":
            print("Invalid input")


def consoleclear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def MainMenu(graphical = False):
    if graphical:
        gfxmenu = GUI.setupMenu()
        gfxmenu.mainloop()
    else:
        incmd = None
        while incmd != "3":
            print("Welcome to BlackJack!\n\nWe have a table ready and waiting for you. What would you like to do?")
            print("\n1. New Game\n2. Rules\n3. Exit\n")
            incmd = input("Please enter choice: ")
            if incmd == "2":
                rules()
            elif incmd == "1":
                newGame()
            elif incmd != "3":
                print("Invalid input")
        print("Thanks for playing!")

def main():
    #MainMenu(graphical=True)
    MainMenu()
    
    
    
main()
