''' class Card
Handles suit, and value. Stores these as ints and a bool.
suits:
0 - heart
1 - diamond
2 - club
3 - spade
values:
2-10: non-face
11 - jack
12 - queen
13 - king
1 - ace
initializes on the ace of spades
'''
class Card:
    
    def __init__(self, suit:int, suitStr:str, value:int, valueStr:str):
        self.suit = suit
        self.suitStr = suitStr
        self.value = value
        self.valueStr = valueStr
        self.next_card = None
        self.prev_card = None
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value
    
    def display(self):
        print(f"{self.valueStr} of {self.suitStr}")