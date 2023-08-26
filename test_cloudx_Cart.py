import unittest
from client import Cart
from unittest.mock import patch


class TestCheckout(unittest.TestCase):

    def setUp(self):
        self.cart = Cart()

    def test_apply_discount_below_threshold(self):
        self.cart.total = 150  # Below the discount threshold
        self.cart.number_of_items = 3  # Below the item threshold

        expected_total = 150
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_above_threshold(self):
        self.cart.total = 250  # Above the discount threshold
        self.cart.number_of_items = 6  # Above the item threshold

        expected_total = self.cart.total - self.cart.discount
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_on_threshold(self):
        self.cart.total = 200  # Above the discount threshold
        self.cart.number_of_items = 5  # Above the item threshold

        expected_total = self.cart.total - self.cart.discount
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_only_quantity_below_threshold(self):
        self.cart.total = 250  # Above the discount threshold
        self.cart.number_of_items = 3  # Below the item threshold

        expected_total = 250
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_only_total_below_threshold(self):
        self.cart.total = 150  # Below the discount threshold
        self.cart.number_of_items = 6  # Above the item threshold

        expected_total = 150
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_huge_integer_with_discount(self):
        self.cart.total = 86532130  # Below the discount threshold
        self.cart.number_of_items = 687  # Above the item threshold

        expected_total = 86532080
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_huge_float_with_discount(self):
        self.cart.total = 86532130.65432543454  # Below the discount threshold
        self.cart.number_of_items = 687  # Above the item threshold

        expected_total = 86532080.65432544
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_huge_integer_without_discount(self):
        self.cart.total = 86532130  # Below the discount threshold
        self.cart.number_of_items = 4  # Above the item threshold

        expected_total = 86532130
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_huge_float_without_discount(self):
        self.cart.total = 86532130.65432543454  # Below the discount threshold
        self.cart.number_of_items = 3  # Above the item threshold

        expected_total = 86532130.65432543454
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_tiny_integer(self):
        self.cart.total = 1  # Below the discount threshold
        self.cart.number_of_items = 1  # Above the item threshold

        expected_total = 1
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_tiny_float(self):
        self.cart.total = 0.1  # Below the discount threshold
        self.cart.number_of_items = 1  # Above the item threshold

        expected_total = 0.1
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_not_discounted_print(self):
        # Capture the standard output using the 'patch' context manager
        with patch('builtins.print') as mock_print:
            # Test when total and number_of_items are not enough
            self.cart.total = 150
            self.cart.number_of_items = 4
            self.cart.apply_discount()

            # Check if the 'else' branch was printed
            mock_print.assert_called_with('\nBuy 5 or more products for $200 or more to get a $50 Discount!')

    def test_apply_discount_discounted_print(self):
        # Capture the standard output using the 'patch' context manager
        with patch('builtins.print') as mock_print:
            # Test when total and number_of_items are enough
            self.cart.total = 250
            self.cart.number_of_items = 7
            self.cart.apply_discount()

            # Check if the 'if' branch was printed
            mock_print.assert_called_with(f'\nTotal after discount: $200')

    def test_check_invalid_input_invalid_data_type_string_total(self):
        self.cart.total = '250'  # Invalid input: string
        self.cart.number_of_items = 7
        result = self.cart.check_valid_input()

        self.assertFalse(result)

    def test_check_invalid_input_invalid_data_type_string_quantity(self):
        self.cart.total = 250
        self.cart.number_of_items = '7'  # Invalid input: string
        result = self.cart.check_valid_input()

        self.assertFalse(result)

    def test_check_invalid_input_invalid_data_type_float_quantity(self):
        self.cart.total = 250
        self.cart.number_of_items = 7.5  # Invalid input: float
        result = self.cart.check_valid_input()

        self.assertFalse(result)

    def test_check_invalid_input_zero_quantity(self):
        self.cart.total = 25
        self.cart.number_of_items = 0  # Invalid input: zero items
        result = self.cart.check_valid_input()

        self.assertFalse(result)

    def test_check_invalid_input_zero_price(self):
        self.cart.total = 0  # Invalid input: zero price
        self.cart.number_of_items = 7
        result = self.cart.check_valid_input()

        self.assertFalse(result)

    def test_check_invalid_input_negative_quantity(self):
        self.cart.total = 250
        self.cart.number_of_items = -8  # Invalid input: negative
        result = self.cart.check_valid_input()

        self.assertFalse(result)

    def test_check_invalid_input_negative_price(self):
        self.cart.total = -20  # Invalid input: negative
        self.cart.number_of_items = 10
        result = self.cart.check_valid_input()

        self.assertFalse(result)

    def test_check_valid_input_valid_data_int(self):
        self.cart.total = 250
        self.cart.number_of_items = 7
        result = self.cart.check_valid_input()

        self.assertTrue(result)

    def test_check_valid_input_valid_data_float(self):
        self.cart.total = 2.5
        self.cart.number_of_items = 7
        result = self.cart.check_valid_input()

        self.assertTrue(result)

    if __name__ == '__main__':
        unittest.main()
