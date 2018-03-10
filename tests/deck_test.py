import unittest
from io import StringIO

from tinycards.model import Deck


class DeckTest(unittest.TestCase):

    def test_cards_from_csv(self):
        test_deck = Deck('Test Deck')
        csv_data = StringIO('front,back\nfront word,back word')

        test_deck.add_cards_from_csv(csv_data)

        first_card = test_deck.cards[0]
        self.assertEqual('front word', first_card.front.concepts[0].fact.text)
        self.assertEqual('back word', first_card.back.concepts[0].fact.text)


if __name__ == '__main__':
    unittest.main()
