import unittest

#This class gives a tip or help to the user on what they should do with their hand.
#It gives them a tip such as hit, stay, double, or split.
class Tip:
    def __init__(self, dealerhand, playerhand):
        #Dealerhand will give the value of the dealers face up card.
        self.dealerhand = dealerhand
        #Playerhand will give a list of the cards in the players hand.
        #This functionality will hand do call the class for playerhand and dealer hand.
        self.playerhand = playerhand
        #This two value will change when added into system, but now they give the
        #first and second card in players hand.
        self.playercard1 = playerhand[0]
        self.playercard2 = playerhand[1]

    #This function give the value of all the cards in the players hand added into a sum.
    def hand_value(self):
        value = 0
        #For each card in the players hand, add to value.
        for i in range(len(self.playerhand)):
            value += self.playerhand[i]
        return value;


    #This module is not complete as it only gives values for one dealer hand
    #but, it will not be hard to add other dealer hands, so the unittests just test functionality.
    #This function checks the dealers hand and then checks all possible combinations for the player
    #hand to give a tip.
    def tip_for_hands(self):
        tip = ""
        value = self.hand_value()

        #If the dealers face up card is 2, it will then go through and check all combinations for player hand.
        if(self.dealerhand == 2):
            if(self.playercard1 == 2 & self.playercard2==2):
                tip = "Split"
                return tip
            elif(self.playercard1 == 3 & self.playercard2 == 3):
                tip = "Split"
                return tip
            elif (self.playercard1 == 4 & self.playercard2 == 4):
                tip = "Hit"
                return tip
            elif (self.playercard1 == 5 & self.playercard2 == 5):
                tip = "Double"
                return tip
            elif (self.playercard1 == 6 & self.playercard2 == 6):
                tip = "Split"
                return tip
            elif (self.playercard1 == 7 & self.playercard2 == 7):
                tip = "Split"
                return tip
            elif (self.playercard1 == 8 & self.playercard2 == 8):
                tip = "Split"
                return tip
            elif (self.playercard1 == 9 & self.playercard2 == 9):
                tip = "Split"
                return tip
            elif (self.playercard1 == 10 & self.playercard2 == 10):
                tip = "Stay"
                return tip
            elif (self.playercard1 == 11 & self.playercard2 == 2):
                tip = "Hit"
                return tip
            elif (self.playercard1 == 11 & self.playercard2 == 3):
                tip = "Hit"
                return tip
            elif (self.playercard1 == 11 & self.playercard2 == 4):
                tip = "Hit"
                return tip
            elif (self.playercard1 == 11 & self.playercard2 == 5):
                tip = "Hit"
                return tip
            elif (self.playercard1 == 11 & self.playercard2 == 6):
                tip = "Hit"
                return tip
            elif (self.playercard1 == 11 & self.playercard2 == 7):
                tip = "Stay"
                return tip
            elif (self.playercard1 == 11 & self.playercard2 == 8):
                tip = "Stay"
                return tip
            elif (self.playercard1 == 11 & self.playercard2 == 9):
                tip = "Stay"
                return tip
            elif (value == 5):
                tip = "Hit"
                return tip
            elif (value == 6):
                tip = "Hit"
                return tip
            elif (value == 7):
                tip = "Hit"
                return tip
            elif (value == 8):
                tip = "Hit"
                return tip
            elif (value == 9):
                tip = "Hit"
                return tip
            elif (value == 10):
                tip = "Double"
                return tip
            elif (value == 11):
                tip = "Double"
                return tip
            elif (value == 12):
                tip = "Hit"
                return tip
            elif (value == 13):
                tip = "Stay"
                return tip
            elif (value == 14):
                tip = "Stay"
                return tip
            elif (value == 15):
                tip = "Stay"
                return tip
            elif (value == 16):
                tip = "Stay"
                return tip
            elif (value == 17):
                tip = "Stay"
                return tip
            elif (value == 18):
                tip = "Stay"
                return tip
            elif (value == 19):
                tip = "Stay"
                return tip
            elif (value == 20):
                tip = "Stay"
                return tip

#Unit tests
class Tests(unittest.TestCase):
    """ Use these to test your algorithms """

    #This test checks for double card like 2,2 or 5,5 in player hand.
    def test_doublecard(self):
        t = Tip(2, [2,2])
        #Test for dealer card 2 and player hand 2,2
        self.assertEqual(t.tip_for_hands(),"Split")

        t = Tip(2, [5,5])
        #Test for dealer card 2 and player hand 5,5
        self.assertEqual(t.tip_for_hands(), "Double")
        return

    #This class checks for value of the player hand
    def test_value(self):
        t = Tip(2, [8,2])
        #Test for dealer card 2 and player hand value = 10
        self.assertEqual(t.tip_for_hands(), "Double")

        t = Tip(2, [10,3])
        #Test for dealer card 2 and player hand value = 13
        self.assertEqual(t.tip_for_hands(), "Stay")

        t = Tip(2, [8,2,4])
        #Test for dealer card 2 and player hand with 3 cards = 14
        self.assertEqual(t.tip_for_hands(), "Stay")

        return


if __name__ == "__main__":
    unittest.main()
