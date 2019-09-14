import unittest
from gofish import drawCard, getCard

# Go to project settings and add local python directory as Sources, so that you can import the local files here

# Naming convention - start tests with "test_"


class GoFishTest(unittest.TestCase):
    def setUp(self):
        self.deck = [(x, y) for x in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] for y in ["spades", "hearts", "diamonds", "clubs"]]

    def test_draw(self):
        hand = {}
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)

        self.assertEqual(len(self.deck), 52-5)

class GoFishTestLimitedDeck_HighLightBug(unittest.TestCase):
    def setUp(self):
        self.deck = \
            [
                ("2", "hearts"),
                ("3", "clubs"),
                ("4", "hearts"),
                ("5", "clubs")
            ]

    def test_handSizeIs4(self):
        hand = {}
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)

        # Manipulate deck to force player to draw a 2 of Clubs
        self.deck.append(("2", "clubs"))
        drawCard("Test", self.deck, hand)

        # Will fail with current bug
        self.assertEqual(len(hand), 4)

    def test_handContainsExpectedRanks(self):
        hand = {}
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)

        # Manipulate deck to force player to draw a 2 of Clubs
        self.deck.append(("2", "clubs"))
        drawCard("Test", self.deck, hand)

        print(sorted(hand))
        expectedHand = ['2', '3', '4', '5']
        self.assertEqual(sorted(hand), expectedHand)

    def test_handContainsExpectedSuits(self):
        hand = {}
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)

        # Manipulate deck to force player to draw a 2 of Clubs
        self.deck.append(("2", "clubs"))
        drawCard("Test", self.deck, hand)

        expectedValues = [['clubs'], ['clubs'], ['hearts'], ['hearts', 'clubs']]
        self.assertEqual(sorted(hand.values()), expectedValues)

    def test_4OfSameRank(self):
        hand = {}
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)
        drawCard("Test", self.deck, hand)

        # Manipulate deck to force player to draw all four 2s
        self.deck.append(("2", "clubs"))
        drawCard("Test", self.deck, hand)
        expectedValues = [['clubs'], ['clubs'], ['hearts'], ['hearts', 'clubs']]
        self.assertEqual(sorted(hand.values()), expectedValues)

        self.deck.append(("2", "diamonds"))
        drawCard("Test", self.deck, hand)
        expectedValues = [['clubs'], ['clubs'], ['hearts'], ['hearts', 'clubs', 'diamonds']]
        self.assertEqual(sorted(hand.values()), expectedValues)

        self.deck.append(("2", "spades"))
        drawCard("Test", self.deck, hand)
        expectedValues = [['clubs'], ['clubs'], ['hearts']]
        self.assertEqual(sorted(hand.values()), expectedValues)

        self.assertEqual(len(hand), 3)

        expectedHand = ['3', '4', '5']
        self.assertEqual(sorted(hand), expectedHand)

if __name__ == '__main__':
    unittest.main()