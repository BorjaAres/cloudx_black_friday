import unittest
from client import Cart
from products import cloud_x_products


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

    def test_apply_discount_total_below_threshold(self):
        self.cart.total = 250  # Above the discount threshold
        self.cart.number_of_items = 3  # Below the item threshold

        expected_total = 250
        self.assertEqual(self.cart.apply_discount(), expected_total)

    def test_apply_discount_items_below_threshold(self):
        self.cart.total = 150  # Below the discount threshold
        self.cart.number_of_items = 6  # Above the item threshold

        expected_total = 150
        self.assertEqual(self.cart.apply_discount(), expected_total)

    if __name__ == '__main__':
        unittest.main()
