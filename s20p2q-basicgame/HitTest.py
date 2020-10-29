import unittest

from Hit import Hit

""" Class of test cases for each condition of hit and also testing the addCard method."""
class HitTestCase(unittest.TestCase):
    # Test for a bust
    def testBust(self):
        HitObject = Hit()
        HitObject.nextCard = 9
        # Make total 25 signaling a bust
        playerHand, playerTotal = HitObject.addCard(HitObject.nextCard,[10,6])
        HitObject.setHitCondition(playerHand,playerTotal)
        self.assertTrue(HitObject.bust) 

     # Test for a split  
    def testSplit(self):
        HitObject = Hit()
        HitObject.nextCard = 10
        # Give the player the same first two cards signaling a split
        playerHand, playerTotal = HitObject.addCard(HitObject.nextCard,[10])
        HitObject.setHitCondition(playerHand,playerTotal)
        self.assertTrue(HitObject.split) 
    # Test for blackjack with Ace coming out first
    def testBlackJackAce(self):
        HitObject = Hit()
        HitObject.nextCard = 10
        # Give the player a 10 value when they started with an ace
        playerHand, playerTotal = HitObject.addCard(HitObject.nextCard,[11])
        HitObject.setHitCondition(playerHand,playerTotal)
        self.assertTrue(HitObject.blackjack)
    # Test for blackjack with face card coming first
    def testBlackJackFace(self):
        HitObject = Hit()
        HitObject.nextCard = 11
        # Give the player an ace when they started with a 10 value
        playerHand, playerTotal = HitObject.addCard(HitObject.nextCard,[10])
        HitObject.setHitCondition(playerHand,playerTotal)
        self.assertTrue(HitObject.blackjack)
    # test for a 21 that isn't "blackjack"
    def testTwentyOne(self):
        HitObject = Hit()
        HitObject.nextCard = 6
        # Give the player a 6 to put their total to 21
        playerHand, playerTotal = HitObject.addCard(HitObject.nextCard,[9,6])
        HitObject.setHitCondition(playerHand,playerTotal)
        self.assertTrue(HitObject.twentyone)
    # Test adding a card to the hand when they only have one
    def testNextCardOne(self):
        HitObject = Hit()
        HitObject.nextCard = 2
        # Add a 2 to their hand
        playerHand, playerTotal = HitObject.addCard(HitObject.nextCard,[10])
        self.assertEqual(12,playerTotal)
        self.assertEqual([10,2],playerHand)
    # Test adding a card to the hand when they have two cards
    def testNextCardTwo(self):
        HitObject = Hit()
        HitObject.nextCard = 9
        # Add a 9 to the hand
        playerHand, playerTotal = HitObject.addCard(HitObject.nextCard,[10,6])
        HitObject.setHitCondition(playerHand,playerTotal)
        self.assertEqual(25,playerTotal)
        self.assertEqual([10,6,9],playerHand)

if __name__ == '__main__':
 unittest.main()

