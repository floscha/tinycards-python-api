import unittest

from tinycards.model import User


class UserTest(unittest.TestCase):

    def test_user_constructor_sets_correct_properties(self):
        expected_creation_date = 0
        expected_email = 'abc@xyz.com'
        expected_fullname = 'abc'
        expected_id = 1234
        expected_learning_language = 'fr'
        expected_picture_url = 'http://example.org/img'
        expected_subscribed = True
        expected_subscriber_count = 0
        expected_subscription_count = 0
        expected_ui_language = 'en'
        expected_username = 'xyz'

        test_user = User(
            creation_date=expected_creation_date,
            email=expected_email,
            fullname=expected_fullname,
            user_id=expected_id,
            learning_language=expected_learning_language,
            picture_url=expected_picture_url,
            subscribed=expected_subscribed,
            subscriber_count=expected_subscriber_count,
            subscription_count=expected_subscription_count,
            ui_language=expected_ui_language,
            username=expected_username
        )

        self.assertEqual(expected_creation_date, test_user.creation_date)
        self.assertEqual(expected_email, test_user.email)
        self.assertEqual(expected_fullname, test_user.fullname)
        self.assertEqual(expected_id, test_user.id)
        self.assertEqual(expected_learning_language,
                         test_user.learning_language)
        self.assertEqual(expected_picture_url, test_user.picture_url)
        self.assertEqual(expected_subscribed, test_user.subscribed)
        self.assertEqual(expected_subscriber_count, test_user.subscriber_count)
        self.assertEqual(expected_subscription_count,
                         test_user.subscription_count)
        self.assertEqual(expected_ui_language, test_user.ui_language)
        self.assertEqual(expected_username, test_user.username)


if __name__ == '__main__':
    unittest.main()
