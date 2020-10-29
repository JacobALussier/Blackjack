import entity
import hand as h
'''class Player
Handles own hand and betting
'''
class Player(entity.Entity):
    def __init__(self, bank:int = 0, name:str = ""):
        self.hand = h.Hand()
        self.bet = 0
        self.bank = bank
        self.name = name
        self.bust = False
        self.blackjack = False
        self.standing = False
        self.image = None
        self.label = None