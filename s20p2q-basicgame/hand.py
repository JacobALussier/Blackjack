import deck as d
'''
Held by player, contains the players cards and statistic info on them (total, #cards, bust T/F, insurance(?))
'''
class Hand:
    def __init__(self):
        self.carddeck = None
        self.bust = False
        self.stand = False
        
    def add_card(self, card):
        if self.carddeck == None:
            self.carddeck = d.Deck()
            self.carddeck.add_card(card)
        else:
            self.carddeck.add_card(card)
            
    def get_size(self):
        return self.carddeck.size
    
    def get_total(self, num):
        return self.carddeck.total(num)
    
    def display(self, num):
        self.carddeck.display(num)
        
    def draw_card(self):
        return self.carddeck.draw_card()