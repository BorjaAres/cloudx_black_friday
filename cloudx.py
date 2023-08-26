from client import Client, users_dict
from products import italic_bold_open, italic_bold_close, cloud_x_products


def main():
    # Welcome the user
    Client.welcome_user()

    # User authentication and interaction loop
    while not Client.signed_in:
        if Client.username.lower() == 'browse':
            Client.browse()
        elif Client.username.lower() == 'sign up':
            Client.sign_up()
        else:
            # Check if the entered username exists
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
            # Ask user how many of the chosen product to add
            number_of_items = input(
                f'How many {italic_bold_open}{action}{italic_bold_close} would you like to add to the Cart?: ')
            # Add the chosen product to the cart
            users_dict[Client.username].cart.add_product(action.title(), int(number_of_items))
        elif action.lower() == 'remove':
            # Ask user which product to remove and how many
            item = input(
                f'What {italic_bold_open}Product{italic_bold_close} would you like to remove?: ')
            number_of_items = input(
                f'How many {italic_bold_open}{item}{italic_bold_close} would you like to remove from the Cart?: ')
            # Remove the chosen product from the cart
            users_dict[Client.username].cart.remove_product(item, int(number_of_items))
        elif action.lower() == 'checkout':
            # Proceed to checkout and finalize the purchase
            users_dict[Client.username].cart.checkout()
            break


if __name__ == "__main__":
    main()
