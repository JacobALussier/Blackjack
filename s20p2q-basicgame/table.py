'''class Table

'''
class Table:
    def __init__(self, players = [], playerBets:int = [], dealer = None, deck = None):
        self.players = players
        self.playerBets = playerBets
        self.dealer = dealer
        self.deck = deck
    
    def clear(self):
        self.dealer.blackjack = False
        self.dealer.bust = False
        self.dealer.standing = False
        for i in range(self.dealer.hand.get_size()):
            self.deck.add_card(self.dealer.hand.draw_card())        
        for player in self.players:
            player.blackjack = False
            player.bust = False
            player.standing = False
            for i in range(player.hand.get_size()):
                self.deck.add_card(player.hand.draw_card())
    
    def shuffle(self, num):
        self.deck.shuffle(num)

    def draw_card(self):
        return self.deck.draw_card()