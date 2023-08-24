from tabulate import tabulate
from cart import Cart
from cloudx import *

# Client class definition
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

