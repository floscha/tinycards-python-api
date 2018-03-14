import unittest

from tinycards import Tinycards


class ClientTests(unittest.TestCase):

    def setUp(self):
        self.client = Tinycards()

    def test_get_trends_returns_10_decks(self):
        trends = self.client.get_trends()

        self.assertEqual(10, len(trends))


if __name__ == '__main__':
    unittest.main()
