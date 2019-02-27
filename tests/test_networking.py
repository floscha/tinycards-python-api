from collections import OrderedDict
import unittest
import textwrap

from tinycards.model.deck import Deck
from tinycards.networking.form_utils import to_multipart_form
from tinycards.networking.json_converter import deck_to_json


class TestNetworking(unittest.TestCase):
    def test_simple_multipart_form_parsing(self):
        test_data = OrderedDict([('name', 'test_name'),
                                 ('description', 'test_description')])
        test_form_boundary = '----WebKitFormBoundary3BvCIJDoE9COqAff'

        produced_form = to_multipart_form(test_data, test_form_boundary)

        expected_form = textwrap.dedent("""\
            ------WebKitFormBoundary3BvCIJDoE9COqAff
            Content-Disposition: form-data; name="name"

            test_name
            ------WebKitFormBoundary3BvCIJDoE9COqAff
            Content-Disposition: form-data; name="description"

            test_description
            ------WebKitFormBoundary3BvCIJDoE9COqAff--""")
        self.assertMultiLineEqual(expected_form, produced_form)


if __name__ == '__main__':
    unittest.main()
