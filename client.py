from tabulate import tabulate
from products import cloud_x_products, italic_bold_open, italic_bold_close


class Client:
    username = ''  # Store the current username
    signed_in = False  # To track if a user is signed in or not

    def __init__(self, user):
        self.user = user
        self.cart = Cart()

    # Method to welcome users
    @classmethod
    def welcome_user(cls):
        print(f'Welcome to {italic_bold_open}CloudX!{italic_bold_close}\n'
              'Your online shop for all your sporting needs\n'
              f'{italic_bold_open}BLACK FRIDAY DEALS!{italic_bold_close}\n')

        # Asking for user action
        print(f'Please introduce your {italic_bold_open}Username{italic_bold_close} to log in,\n'
              f'type {italic_bold_open}Sign Up{italic_bold_close} if you are a new user,\n'
              f'or type {italic_bold_open}Browse{italic_bold_close} if you want to see our products:\n')

        cls.username = input(f'Type your {italic_bold_open}Username{italic_bold_close}, '
                             f'{italic_bold_open}Sign Up{italic_bold_close} or '
                             f'{italic_bold_open}Browse{italic_bold_close}: \n')

        return cls.username

    # Method to sign up a new user
    @classmethod
    def sign_up(cls):
        cls.username = input(f'Please enter a {italic_bold_open}Username{italic_bold_close}: ')
        cls.check_username_availability(cls.username.lower())
        cls.signed_in = True

        cls.add_user_to_dict()

    # Adding the new user to the dict
    @classmethod
    def add_user_to_dict(cls):
        new_user = Client(cls.username)
        users_dict[cls.username] = new_user

    # Method to check if a username is available during sign up
    @classmethod
    def check_username_availability(cls, user):
        while True:
            if user.lower() in users_dict:
                print(f'Sorry, {italic_bold_open}Username{italic_bold_close}: {user.title()} already exists')
                user = input(f'Please introduce a new {italic_bold_open}Username{italic_bold_close}: ')
            else:
                print(f'\nWelcome to {italic_bold_open}CloudX{italic_bold_close}, {user.title()}!\n')

                cls.username = user

                return cls.username

    # Method to check if a username exists during log in
    @classmethod
    def check_username_existence(cls, user):
        while True:
            if user in users_dict:
                print(f'\nWelcome back, {cls.username.title()}!\n')
                cls.signed_in = True

                return cls.signed_in

            else:
                user = input(f"\nThe {italic_bold_open}Username{italic_bold_close} doesn't exist."
                             f"\nPlease introduce a valid "
                             f"{italic_bold_open}Username{italic_bold_close} or "
                             f"{italic_bold_open}Sign Up{italic_bold_close}: ")
                cls.username = user
                if user.lower() == 'sign up':
                    cls.sign_up()
                    return cls.username

    # Method to browse available products and display them in a table
    @classmethod
    def browse(cls):
        column1 = list(cloud_x_products.items())[:len(cloud_x_products) // 2]
        column2 = list(cloud_x_products.items())[len(cloud_x_products) // 2:]

        table_data = []
        for (product1, details1), (product2, details2) in zip(column1, column2):
            row = [product1, details1[0], details1[1], ' ', product2, details2[0], details2[1]]
            table_data.append(row)

        headers = [f'{italic_bold_open}Product{italic_bold_close}',
                   f'{italic_bold_open}Price{italic_bold_close}',
                   f'{italic_bold_open}Stock{italic_bold_close}',
                   ' '] * 2

        print(tabulate(table_data, headers=headers, tablefmt='github'))

        if not cls.signed_in:
            print('\nWe have excellent discounts for Black Friday!')
            cls.username = input(
                f'Introduce your {italic_bold_open}Username{italic_bold_close}'
                f' or {italic_bold_open}Sign up{italic_bold_close} to discover them: \n')


# Cart class definition
class Cart:
    discount = 50

    def __init__(self):
        self.cart_dict = {}
        self.total = 0
        self.number_of_items = 0

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

    # Check if the input of the cart is valid
    def check_valid_input(self):
        if isinstance(self.total, (int, float)) and isinstance(self.number_of_items, int):
            if self.total > 0 and self.number_of_items > 0:
                return True
            else:
                print('Price and quantity should be above zero.')
        else:
            print('Invalid data types for total or number of items.')
        return False

    # Methods to calculate and display the total after checkout
    def checkout(self):
        self.calculate_number_of_items()

        for product, quantity in self.cart_dict.items():
            self.total += self.cart_dict[product] * cloud_x_products[product][0]
            if self.check_valid_input():
                print(f'\nTotal before discount: ${self.total}')
                self.apply_discount()

    def calculate_number_of_items(self):
        self.number_of_items = sum(self.cart_dict.values())
        return self.number_of_items

    # Method to apply the discount if conditions are met and input is valid
    def apply_discount(self):
        if self.total >= 200 and self.number_of_items >= 5:
            self.total -= self.discount
            print(f'\nTotal after discount: ${self.total}')
        else:
            print('\nBuy 5 or more products for $200 or more to get a $50 Discount!')

        return self.total


# Creating user instances
user_asra = Client('Asra')
user_joshua = Client('Joshua')
user_sartaz = Client('Sartaz')
user_borja = Client('Borja')


# Dictionary to store user instances
users_dict = {
    'asra': user_asra,
    'joshua': user_joshua,
    'sartaz': user_sartaz,
    'borja': user_borja,
}
