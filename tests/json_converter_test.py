from dataclasses import dataclass
import unittest

from tinycards.networking.json_converter import json_to_object, object_to_json


@dataclass
class TestClass:
    test_str: str
    test_int: int


class JsonUtilTest(unittest.TestCase):

    def test_json_to_object(self):
        test_json_data = {'testStr': 'test', 'testInt': 1}

        test_object = json_to_object(test_json_data, TestClass)

        self.assertIsInstance(test_object.test_str, str)
        self.assertEqual('test', test_object.test_str)
        self.assertIsInstance(test_object.test_int, int)
        self.assertEqual(1, test_object.test_int)

    def test_object_to_json(self):
        test_object = TestClass('test', 1)

        test_json_data = object_to_json(test_object)

        self.assertIn('testStr', test_json_data)
        self.assertEqual('test', test_json_data['testStr'])
        self.assertIn('testInt', test_json_data)
        self.assertEqual(1, test_json_data['testInt'])


if __name__ == '__main__':
    unittest.main()
