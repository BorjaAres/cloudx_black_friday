import unittest
from unittest.mock import patch
from cloudx import Cart

class TestCartMethods(unittest.TestCase):
    def setUp(self):
        # This method runs before each test method
        self.cart = Cart()
        self.mock_products = {
            'Product A': [10, 5],
            'Product B': [20, 3],
        }

    def tearDown(self):
        # This method runs after each test method
        self.cart = None

    def test_add_product_sufficient_stock(self):
        with patch('cart.cloud_x_products', self.mock_products):
            self.cart.add_product('Product A', 2)
            self.assertEqual(self.cart.cart_dict, {'Product A': 2})
            self.assertEqual(self.mock_products['Product A'][1], 3)

    def test_add_product_insufficient_stock(self):
        with patch('cart.cloud_x_products', self.mock_products):
            self.cart.add_product('Product B', 5)
            self.assertEqual(self.cart.cart_dict, {'Product B': 3})
            self.assertEqual(self.mock_products['Product B'][1], 0)

    def test_remove_product(self):
        self.cart.cart_dict = {'Product A': 3}
        with patch('cart.cloud_x_products', self.mock_products):
            self.cart.remove_product('Product A', 2)
            self.assertEqual(self.cart.cart_dict, {'Product A': 1})
            self.assertEqual(self.mock_products['Product A'][1], 7)

    def test_checkout_discount(self):
        self.cart.cart_dict = {'Product A': 2, 'Product B': 1}
        with patch('cart.cloud_x_products', self.mock_products):
            total = self.cart.checkout()
            self.assertEqual(total, 48)  # (10*2) + (20 - 50%)

    def test_checkout_no_discount(self):
        self.cart.cart_dict = {'Product A': 1, 'Product B': 1}
        with patch('cart.cloud_x_products', self.mock_products):
            total = self.cart.checkout()
            self.assertEqual(total, 30)  # (10*1) + (20*1)

if __name__ == '__main__':
    unittest.main()
