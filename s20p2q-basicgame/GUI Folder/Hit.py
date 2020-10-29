''' Jacob Lussier
    CSC 305 Project - Blackjack---- Hit Class with unit testing
    Due Saturday April 3rd '''


''' This is a hit class that will check all the possible conditions that might occur 
when a player chooses to hit.
For example, we have bust(over 21), split(first two cards dealt are the same), 
blackjack(21 is met with face card and ace), twentyone(21 is met with any combination besides blackjack)
These conditions are important because they will trigger other things in the game (a win, a loss, option to split,
etc.) '''

class Hit:

    def __init__(self):
        self.bust = False
        self.split = False
        self.blackjack = False
        self.twentyone = False
        self.nextCard = 0
    
    #Method to add card to the players hand, returns their new hand and their new total
    def addCard(self,nextCard:int,currentHand:list):
        # Put the card in the players hand
        currentHand.append(nextCard)
        # Add the card's value to their total
        playerTotal = sum(currentHand)

        # return their hand and their total
        return currentHand, playerTotal
    
    #Method to check for all the possible conditions after a hit happens    
    def setHitCondition(self,currentHand,playerTotal):
        # Check for bust
        if playerTotal > 21:
            self.bust = True
        # Check for a regular twentyone
        elif playerTotal == 21 and len(currentHand) > 2:
            self.twentyone = True
        # Check for blackjack
        elif len(currentHand) == 2 and playerTotal == 21:
            self.blackjack = True
        # Check for split
        elif len(currentHand) == 2 and currentHand[0] == currentHand[1]:
            self.split = True
        return



   

    

        

            



        

