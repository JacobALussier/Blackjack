import unittest
from entity import Entity
class entityTestCAse(unittest.TestCase):
    _entity: Entity
        #Sets the players Bank to have 500 dollars, is going to see when the player
        #bets will the bank decrease
    def test_setUp(self) -> None:
        self._entity = Entity(bank=500)

    def test_bankDecrease(self):
        #Establishes a bank entity of 500 and asks the player for a bet
        #Once they bet, checks the players bank to see if value was subtracted
        Entity1 = Entity(bank=500)
        self._entity.bet(100)
        self.assertEqual(self._entity.bank, 400)

    def test_bankDecrease(self):
        #establishes a bet of 200 and then wqill check to see
        #in their bank went down to 300
        _entity(bank=500)
        self._entity.bet(200)
        self.assertEqual(self._entity.bank, 300)

if __name__ == '__main__':
    unittest.main()