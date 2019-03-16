import os
import unittest
import requests

from tinycards import Tinycards
from tinycards.model import Deck


DEFAULT_COVER_URL = 'https://s3.amazonaws.com/tinycards/image/16cb6cbcb086ae0f622d1cfb7553a096'


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
        self.assertTrue(isinstance(created_deck, Deck))
        self.assertEqual('', created_deck.shareable_link)
        self.assertEqual(DEFAULT_COVER_URL, created_deck.cover)

        num_decks = len(self.tinycards.get_decks())
        self.assertEqual(1, num_decks)

    def _test_update_deck_without_change(self):
        """Commit an update without making any changes."""
        first_deck = self.tinycards.get_decks()[0]

        updated_deck = self.tinycards.update_deck(first_deck)

        self.assertTrue(isinstance(updated_deck, Deck))

    def _test_update_deck_title(self):
        """Update the title of our deck."""
        test_deck = self.tinycards.find_deck_by_title('Test Deck')
        test_deck.title = 'Updated Test Deck'

        updated_deck = self.tinycards.update_deck(test_deck)

        self.assertTrue(isinstance(updated_deck, Deck))
        self.assertEqual('Updated Test Deck', updated_deck.title)

    def _test_add_cards(self):
        """Add to cards to our deck."""
        first_deck = self.tinycards.get_decks()[0]
        first_deck.add_card(('front test 1', 'back test 1'))
        first_deck.add_card(('front test 2', 'back test 2'))

        updated_deck = self.tinycards.update_deck(first_deck)

        self.assertTrue(isinstance(updated_deck, Deck))
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

    def _test_create_shareable_deck(self):
        """Create a new empty, shareable deck."""
        new_deck = Deck('Test shareable Deck', self.tinycards.user_id, private=True, shareable=True)
        created_deck = self.tinycards.create_deck(new_deck)
        self.assertTrue(isinstance(created_deck, Deck))
        self.assertNotEqual('', created_deck.shareable_link)
        resp = requests.get(created_deck.shareable_link)
        self.assertEqual(200, resp.status_code)
        self._delete_deck(created_deck.id)  # Clean up after ourselves.

    def _test_create_deck_with_cover(self):
        """Create a new empty deck, with a cover."""
        current_dir = os.path.dirname(os.path.realpath(__file__))
        blue_cover_filepath = os.path.abspath(os.path.join(current_dir, 'test_logo_blue.jpg'))
        deck = Deck('Test Deck with cover', self.tinycards.user_id, cover=blue_cover_filepath)
        deck = self.tinycards.create_deck(deck)
        self.assertTrue(isinstance(deck, Deck))
        self._assert_cover_was_updated(blue_cover_filepath, deck.cover)
        # Add a few tests cards (to pass server-side validation) & update the deck's cover:
        deck.add_card(('front test 1', 'back test 1'))
        deck.add_card(('front test 2', 'back test 2'))
        red_cover_filepath = os.path.abspath(os.path.join(current_dir, 'test_logo_red.jpg'))
        deck.cover = red_cover_filepath
        deck = self.tinycards.update_deck(deck)
        self.assertTrue(isinstance(deck, Deck))
        self._assert_cover_was_updated(red_cover_filepath, deck.cover)
        self._delete_deck(deck.id)  # Clean up after ourselves.

    def _assert_cover_was_updated(self, filepath, deck_cover):
        self.assertNotEqual(DEFAULT_COVER_URL, deck_cover)
        self.assertTrue(deck_cover.startswith('https://'))
        resp = requests.get(deck_cover)
        self.assertEqual(200, resp.status_code)
        with open(filepath, 'rb') as f:
            self.assertEqual(f.read(), resp.content)

    def _delete_deck(self, deck_id):
        self.tinycards.delete_deck(deck_id)
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

        self._test_create_shareable_deck()

        self._test_create_deck_with_cover()

    def tearDown(self):
        """Clean up after all tests have finished running."""
        # Delete all decks created during the test routines.
        self._clean_up()


if __name__ == '__main__':
    unittest.main()
