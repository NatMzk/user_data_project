import unittest
from main import UserDataGenerator


class UserDataGeneratorTest(unittest.TestCase):
    def test_generate_data_is_returned_value_list_type(self):
        actual = UserDataGenerator().generate_data(number_of_users=1)
        self.assertIsInstance(actual, list)

    def test_generate_data_is_user_data_dict_type(self):
        actual = UserDataGenerator().generate_data(number_of_users=5)
        self.assertIsInstance(actual[0], dict)
        self.assertTrue(len(actual) == 5)  # > < =< ==


if __name__ == '__main__':
    unittest.main()
