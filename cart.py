from cloudx import *

# Cart class definition
class Cart:
    discount = 50

    def __init__(self):
        self.cart_dict = {}

    # Method to add a product to the cart
    def add_product(self, product, quantity):

        if cloud_x_products[product][1] >= quantity:
            self.cart_dict[product] = self.cart_dict.setdefault(product, 0) + quantity
            cloud_x_products[product][1] -= quantity
            print(self.cart_dict)
        else:
            self.cart_dict[product] = self.cart_dict.setdefault(product, 0) + cloud_x_products[product][1]
            print(f'\nApologies, we dont have enough {italic_bold_open}{product}{italic_bold_close}, '
                  f'{italic_bold_open}{cloud_x_products[product][1]}{italic_bold_close} added to your cart\n')
            cloud_x_products[product][1] = 0
            print(self.cart_dict)

    # Method to remove a product from the cart
    def remove_product(self, product, quantity):
        if product in self.cart_dict and self.cart_dict[product] >= quantity:
            self.cart_dict[product] -= quantity
            cloud_x_products[product][1] += quantity
        else:
            print(f'There are not enough {italic_bold_open}{product}{italic_bold_close} in your Cart'
                  f'{self.cart_dict[product][0]} {italic_bold_open}{product}{italic_bold_close} removed')
            cloud_x_products[product][1] += self.cart_dict[product]
            self.cart_dict[product] = 0

    # Method to calculate and display the total after checkout
    def checkout(self):
        total = 0
        for product, number in self.cart_dict.items():
            total += self.cart_dict[product] * cloud_x_products[product][0]
            print("Total before discounts:", total)

        if total >= 200 and sum(self.cart_dict.values()) >= 5:
            total -= self.discount
            print("Total after discounts:", total)

            return total