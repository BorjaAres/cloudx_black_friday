# Make a note about the use of ANSI
# Note about installing tabulator
from tabulate import tabulate


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

        return cls.username

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
                if user.lower() == 'sign up':
                    cls.sign_up()
                    return cls.username

    # Method to browse available products
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


# 'Product': ['Price', 'Stock'],
cloud_x_products = {
    'Basketball': [25.9, 9],
    'Tennis Racket': [50, 8],
    'Running Shoes': [80.9, 5],
    'Yoga Mat': [30, 5],
    'Gym Gloves': [15.9, 6],
    'Swimming Goggles': [25, 7],
    'Cycling Helmet': [60.9, 6],
    'Resistance Bands Set': [25, 5],
    'Dumbbells Set': [100.9, 5],
    'Fitness Tracker': [120, 6],
    'Water Bottle': [20, 5],
    'Sport Shorts': [30.9, 5]
}

italic_bold_open = '\033[1;3m'
italic_bold_close = '\033[0m'

# Creating user instances
new_user = Client.username
user_asra = Client('Asra')
user_joshua = Client('Joshua')
user_sartaz = Client('Sartaz')
user_borja = Client('Borja')
user_new = Client(Client.username)

# Dictionary to store user instances
users_dict = {
    'asra': user_asra,
    'joshua': user_joshua,
    'sartaz': user_sartaz,
    'borja': user_borja,
    new_user: user_new
}

# Welcome the user
Client.welcome_user()

# User authentication and interaction loop
while not Client.signed_in:
    if Client.username.lower() == 'browse':
        Client.browse()
    elif Client.username.lower() == 'sign up':
        Client.sign_up()
    else:
        Client.check_username_existence(Client.username.lower())
        break

# Main interaction loop
while Client.signed_in:
    Client.browse()
    print(f'\nType the {italic_bold_open}Product Name{italic_bold_close} to add it to the cart.\n'
          f'Type {italic_bold_open}Remove{italic_bold_close} to remove a product.\n'
          f'Type {italic_bold_open}Checkout{italic_bold_close} when you are ready to pay\n')

    action = input(f'Please introduce a {italic_bold_open}Product Name{italic_bold_close}, '
                   f'{italic_bold_open}Remove{italic_bold_close}, '
                   f'{italic_bold_open}Checkout{italic_bold_close}: ')

    if action.title() in cloud_x_products:
        number_of_items = input(
            f'How many {italic_bold_open}{action}{italic_bold_close} would you like to add to the Cart?: ')
        users_dict[Client.username].cart.add_product(action.title(), int(number_of_items))
    elif action.lower() == 'remove':
        item = input(
            f'What {italic_bold_open}Product{italic_bold_close} would you like to remove?: ')
        number_of_items = input(
            f'How many {italic_bold_open}{item}{italic_bold_close} would you like to remove from the Cart?: ')
        users_dict[Client.username].cart.remove_product(item, int(number_of_items))
    elif action.lower() == 'checkout':
        users_dict[Client.username].cart.checkout()
        break
