import hand as h
'''class Entity
Handles basic entities (names and things)
'''
class Entity:
    def __init__(self, name = "", bank = 0):
        self.hand = h.Hand()
        self.bet = 0
        self.name = name
        self.bank = bank
        self.bust = False
        self.blackjack = False
        self.standing = False

    def betting(self, bet = None, double = False):
        if self.bank > 0:
            badBet = True
            while badBet:
                if bet == None:
                    badinput = True
                    while badinput:
                        try:
                            bet = int(input("Please enter bet amount: "))
                            badinput = False
                        except:
                            print("Invalid amount.")
                if bet > 0:
                    if bet > self.bank:
                        print(f"Not enough money in the bank for that bet! You only have ${self.bank}")
                        if double:
                            return False
                    else:
                        badBet = False
                else:
                    print("Must at least $1.")
                if badBet:
                    bet = None
            self.bet = bet + self.bet
            self.bank -= self.bet
            return True
        else:
            print("You cannot bet with $0 in the bank!")

    def dealt(self, card):
        self.hand.add_card(card)
        self.getTotal(verbose = False)
    
    def getHand(self, num = None):
        if num == None:
            num = self.hand.get_size()
        print(f"{self.name}'s hand has:")
        if num:
            self.hand.display(num)
        else:
            print("Nothing!")
            
    def getTotal(self, verbose = True, num = None):
        if num == None:
            num = self.hand.get_size()
        if self.hand.get_size():
            total = self.hand.get_total(num)
            if verbose:
                if total[0] == total[1]:
                    totalstr = f"{total[0]}"
                else:
                    totalstr = f"Aces low: {total[0]}, Aces high: {total[1]}"
                print(f"{self.name}'s hand totals {totalstr}\n")
        else:
            if verbose:
                print(f"{self.name}'s hand is empty")
        if total[1] == 21 or total[0] == 21:
            self.blackjack = True
        elif total[0] > 21:
            self.bust = True
        return (total[0], total[1])