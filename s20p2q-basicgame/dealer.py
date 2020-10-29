import entity
import hand as h
import deck as d
import card as c
'''class Dealer
Handles deck creation, dealing,
'''
class Dealer(entity.Entity):
    def __init__(self, name = "The Dealer"):
        self.hand = h.Hand()
        self.bet = 0
        self.bank = 1000000
        self.table = None
        self.name = name
        self.bust = False
        self.blackjack = False
        self.standing = False
        self.image = None
        self.label = None
        
    def make_deck(self, size:int):
        newDeck = d.Deck()
        for i in range(size):
            for s in range(len(newDeck.suits)):
                for v in range(len(newDeck.values)):
                    newDeck.add_card(c.Card(suit = newDeck.suits[s], suitStr = newDeck.suitStr[s], value = newDeck.values[v], valueStr = newDeck.valuesStr[v]))
        return newDeck
        
    def deal(self, player, num:int = 1):
        for i in range(num):
            player.dealt(self.table.draw_card())
