import unittest
from unittest.mock import patch
from cloudx import Client


class TestClientMethods(unittest.TestCase):
    def setUp(self):
        # This method runs before each test method
        self.mock_users_dict = {'existinguser': None}
        self.original_users_dict = dict(Client.users_dict)
        Client.users_dict = self.mock_users_dict

    def tearDown(self):
        # This method runs after each test method
        Client.users_dict = self.original_users_dict

    @patch('builtins.input', side_effect=['testuser'])
    def test_welcome_user(self, mock_input):
        username = Client.welcome_user()
        self.assertEqual(username, 'testuser')

    @patch('builtins.input', side_effect=['newuser'])
    def test_sign_up(self, mock_input):
        username = Client.sign_up()
        self.assertEqual(username, 'newuser')

    def test_check_username_availability_existing(self):
        with patch.dict('client.users_dict', self.mock_users_dict):
            username = Client.check_username_availability('existinguser')
            self.assertIsNone(username)

    def test_check_username_availability_new(self):
        with patch.dict('client.users_dict', self.mock_users_dict):
            username = Client.check_username_availability('newuser')
            self.assertEqual(username, 'newuser')

    def test_check_username_existence_existing(self):
        with patch.dict('client.users_dict', self.mock_users_dict):
            signed_in = Client.check_username_existence('existinguser')
            self.assertTrue(signed_in)

    def test_check_username_existence_nonexistent(self):
        with patch.dict('client.users_dict', self.mock_users_dict):
            signed_in = Client.check_username_existence('nonexistentuser')
            self.assertFalse(signed_in)

    def test_browse(self):
        # Implement test cases for the browse method
        pass

    # Add more test methods for other Client methods

if __name__ == '__main__':
    unittest.main()
