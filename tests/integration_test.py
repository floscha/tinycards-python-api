import os
import unittest

from tinycards import Tinycards
from tinycards.model import Deck


class TestIntegration(unittest.TestCase):
    def _clean_up(self):
        """Before tests are run, make sure we start from a clean slate."""
        all_decks = self.tinycards.get_decks()
        for d in all_decks:
            self.tinycards.delete_deck(d.id)

    def setUp(self):
        """Load data needed for most test cases."""
        identifier = os.environ.get('TINYCARDS_IDENTIFIER')
        password = os.environ.get('TINYCARDS_PASSWORD')
        if not identifier or not password:
            raise ValueError("Both identifier and password must be set in ENV")

        self.tinycards = Tinycards(identifier, password)

        # Delete all existing decks to start from a clean slate.
        self._clean_up()

    def _test_create_empty_deck(self):
        """Create a new empty deck."""
        new_deck = Deck('Test Deck', self.tinycards.user_id)
        created_deck = self.tinycards.create_deck(new_deck)
        self.assertEqual(Deck, type(created_deck))

        num_decks = len(self.tinycards.get_decks())
        self.assertEqual(1, num_decks)

    def _test_update_deck_without_change(self):
        """Commit an update without making any changes."""
        first_deck = self.tinycards.get_decks()[0]

        updated_deck = self.tinycards.update_deck(first_deck)

        self.assertEqual(Deck, type(updated_deck))

    def _test_update_deck_title(self):
        """Update the title of our deck."""
        test_deck = self.tinycards.find_deck_by_title('Test Deck')
        test_deck.title = 'Updated Test Deck'

        updated_deck = self.tinycards.update_deck(test_deck)

        self.assertEqual(Deck, type(updated_deck))
        self.assertEqual('Updated Test Deck', updated_deck.title)

    def _test_add_cards(self):
        """Add to cards to our deck."""
        first_deck = self.tinycards.get_decks()[0]
        first_deck.add_card(('front test 1', 'back test 1'))
        first_deck.add_card(('front test 2', 'back test 2'))

        updated_deck = self.tinycards.update_deck(first_deck)

        self.assertEqual(Deck, type(updated_deck))
        self.assertEqual(2, len(updated_deck.cards))

    def _test_delete_deck(self):
        """Delete the deck.

        Requires that a deck with title 'Updated Test Deck' was created
        earlier.
        """
        first_deck = self.tinycards.find_deck_by_title('Updated Test Deck')

        self.tinycards.delete_deck(first_deck.id)

        num_decks = len(self.tinycards.get_decks())
        self.assertEqual(0, num_decks)

    def test_integration(self):
        """Test the whole API.

        Needs to run serially to avoid side effects when operating on the same
        backend.
        """
        self._test_create_empty_deck()

        self._test_update_deck_without_change()

        self._test_update_deck_title()

        self._test_add_cards()

        self._test_delete_deck()

    def tearDown(self):
        """Clean up after all tests have finished running."""
        # Delete all decks created during the test routines.
        self._clean_up()


if __name__ == '__main__':
    unittest.main()
