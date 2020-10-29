import random as rn
''' class Deck
Handles cards, shuffling, returning cards, and 'buring' or placing on bottom of deck

'''
class Deck:
    def __init__(self, suits:int = [0, 1, 2, 3], suitStr:str = ["Hearts", "Diamonds", "Clubs", "Spades"], values:int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], valuesStr:str = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]):
        self.headCard = None
        self.tailCard = None
        self.size = 0
        self.suits = suits
        self.suitStr = suitStr
        self.values = values
        self.valuesStr = valuesStr
        
    #if empty deck, sets as top card. Else, adds to bottom of the card.
    def add_card(self, card):
        if self.size == 0:
            self.headCard = card
        else:
            card.next_card = self.tailCard
            self.tailCard.prev_card = card
        self.tailCard = card
        self.size += 1
            
    def insert_card(self, card, top, bottom):
        if top == self.tailCard:
            self.add_card(card)
        else:
            if top != None:
                top.prev_card = card
            if bottom != None:
                bottom.next_card = card
            card.next_card = top
            card.prev_card = bottom
            self.size += 1
            
    #returns a card object stripped of links, and sets the top of the deck to next card
    def draw_card(self):
        if self.size > 1:
            out = self.headCard
            self.headCard = self.headCard.prev_card
            self.headCard.next_card = None
            out.prev_card = None
            self.size -= 1
            return out
        elif self.size == 1:
            self.size = 0
            return self.headCard
        else:
            return None
    
    #shuffles deck by noting last card, then 'inserting' cards randomly until the last card is found- meaning we have loosly shuffled. 2-3 is fine, Casinos follow to 7-15
    def shuffle(self, times):
        for i in range(times):
            last = self.tailCard
            while self.headCard != last:
                cur = self.draw_card()
                place = self.headCard
                for steps in range(rn.randint(1, self.size-1)):
                    place = place.prev_card
                self.insert_card(cur, place, place.prev_card)
    
    def display(self, num:int):
        cur = self.headCard
        if self.size < num:
            num = self.size
            print(f"Too many cards selected ({num}), only {self.size} available")
        for i in range(num):
            cur.display()
            cur = cur.prev_card
            
    def total(self, num = 0):
        totala = 0
        totalb = 0
        cur = self.headCard
        if num == 0:
            num = self.size
        for i in range(num):
            if cur.value > 10:
                totala += 10
                totalb += 10
            elif cur.value == 1:
                totala += 1
                totalb += 11
            else:
                totala += cur.value
                totalb += cur.value
            cur = cur.prev_card
        return (totala, totalb)
