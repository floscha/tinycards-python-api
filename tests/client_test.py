import unittest

from tinycards import Tinycards


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = Tinycards()

        # Remove all favorites to start from a clean slate.
        favorites = self.client.get_favorites()
        for fav in favorites:
            self.client.remove_favorite(fav.id)

    def test_get_trends_returns_10_decks(self):
        trends = self.client.get_trends()

        self.assertEqual(10, len(trends))

    def test_subscribe(self):
        """Test subscribing to an example user.

        We chose a popular the official Duolingo user account which can be
        expected to not be deleted any time soon:
        https://tinycards.duolingo.com/users/Duolingo5900 (ID = 321702331)

        """
        user_id = 321702331
        expected_added_subscription = user_id

        added_subscription = self.client.subscribe(user_id)

        self.assertEqual(expected_added_subscription, added_subscription)

    def test_unsubscribe(self):
        """Test unsubscribing from an example user.

        For this case we chose Librarium Linguae as another example account
        to be able to run tests concurrently:
        https://tinycards.duolingo.com/users/BenPulliam (ID = 164877247)

        """
        user_id = 164877247
        expected_removed_subscription = self.client.subscribe(user_id)
        # TODO Catch error in case subscribing failed.

        removed_subscription = self.client.unsubscribe(user_id)

        self.assertEqual(expected_removed_subscription, removed_subscription)

    def test_favorite_functionality(self):
        """Test all functionality to manage favorites."""

        favorites = self.client.get_favorites()

        self.assertEqual(0, len(favorites))

        # Add the following deck:
        # https://tinycards.duolingo.com/decks/3JyetMiC/writing-arabic
        # (ID = 79c92553-369b-41af-b1ee-8f95110eb456)
        deck_id = '79c92553-369b-41af-b1ee-8f95110eb456'

        added_favorite = self.client.add_favorite(deck_id)

        favorites = self.client.get_favorites()
        self.assertEqual(1, len(favorites))
        self.assertEqual(deck_id, favorites[0].deck.id)

        # Remove the previously added deck from favorites.
        expected_removed_id = added_favorite.id

        removed_favorite_id = self.client.remove_favorite(added_favorite.id)

        self.assertEqual(expected_removed_id, removed_favorite_id)
        favorites = self.client.get_favorites()
        self.assertEqual(0, len(favorites))

    def test_search(self):
        """Test the `search()` method.

        Assumes that the very popular 'Duolingo French Course' will appear as
        the top result for the search query 'french'.

        """
        search_query = 'french'
        expected_first_result_id = '988b66f6-5fbb-4649-a641-0bebb8541496'

        search_results = self.client.search(search_query)
        first_result = search_results[0]
        actual_first_result_id = first_result.data.id

        self.assertEqual(expected_first_result_id, actual_first_result_id)


if __name__ == '__main__':
    unittest.main()
