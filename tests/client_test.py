import unittest

from tinycards import Tinycards


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = Tinycards()

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


if __name__ == '__main__':
    unittest.main()
