import os
import unittest
from tinycards.networking.image_utils import (get_image, mime_type_from_bytes,
                                              mime_type_from_path)


DEFAULT_COVER_URL = ('https://s3.amazonaws.com/tinycards/image/'
                     + '16cb6cbcb086ae0f622d1cfb7553a096')


class ImageUtilsTest(unittest.TestCase):

    def test_mime_type_from_bytes(self):
        with open(path_to('test_logo_blue.jpg'), 'rb') as img:
            self.assertEqual('image/jpeg', mime_type_from_bytes(img.read()))
        with open(path_to('test_logo_red.png'), 'rb') as img:
            self.assertEqual('image/png', mime_type_from_bytes(img.read()))
        with open(path_to('image_utils_test.py'), 'rb') as not_an_img:
            with self.assertRaisesRegex(ValueError, 'Unsupported image type'):
                mime_type_from_bytes(not_an_img.read())

    def test_mime_type_from_path(self):
        self.assertEqual('image/jpeg',
                         mime_type_from_path(path_to('test_logo_blue.jpg')))
        self.assertEqual('image/png',
                         mime_type_from_path(path_to('test_logo_red.png')))
        with self.assertRaisesRegex(ValueError, 'Unsupported image type'):
            mime_type_from_path(path_to('image_utils_test.py'))

    def test_get_image(self):
        img, mime_type = get_image(DEFAULT_COVER_URL)
        self.assertEqual(9659, len(img.read()))
        self.assertEqual('image/png', mime_type)


def path_to(filename):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.abspath(os.path.join(current_dir, filename))


if __name__ == '__main__':
    unittest.main()
