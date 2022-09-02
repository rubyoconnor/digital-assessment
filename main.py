"""program that could be used as a system for phone ordering pasta """
def get_string(m):
    """
    Ask user for a character
    If nothing is entered
    Question will repeat
    """
    string_loop = True
    while string_loop == True:
        my_string = input(m)

        if len(my_string) == 0:
            # error message
            print("you have not entered anything. Please try again")
            continue

        return my_string


def get_integer(m, a=0, b=5):
    """
    Asks user for a integer
    :param a: 0, user cannot enter integer smaller than 0
    :param b: 5, user cannot enter integer bigger than 5
    If integer not between 0 - 5 is entered. Question will repeat.
    """
    integer_loop = True
    while integer_loop == True:
        try:
            my_integer = int(input(m))
        except ValueError:
            # error message if integer is not entered
            print("You have not entered a number. Please enter a number")
            continue
        if my_integer < a or my_integer > b:
            # error message if number is not in range
            print("You have not entered a valid number.")
            continue
        return my_integer


def add_to_order(L, order_list):
    """
    Asks user to choose a pasta to add
    Then how many they want to add
    Adds the pasta to the order_list
    :param L: list (list of all the pastas)
    :param order_list: list (2D is of customer orders)
    :return: None
    """
    print("_" * 50)
    # printing pasta_list with indexes
    for i in range(0, len(L)):
        output = "{} : {} ${}".format(i, L[i][0], L[i][1])
        print(output)
        print("_" * 50)

    # asking user which pasta they want to add
    which_pasta = get_integer("Which number pasta would you like to order?", 0, len(L)-1)
    # asking user how many pastas they want to add
    quantity = get_integer("How many would you like to order?\nPlease note you are not allowed to order more than 5 of the same pasta.\nEnter Amount: ")

    print("_"*70)
    # showing user what has been added to order
    output = "{} {} have been added to your order".format(quantity, L[which_pasta][0])
    print(output)
    print("_"*70)

    # adding the chosen pasta and quantity to the order_list in the main function
    order_list.append([quantity, L[which_pasta][0],  L[which_pasta][1]])


def delete_from_order(order_list):
    """
    Check if order_list empty
    Print out the current order_list
    Ask which pasta to delete
    Ask how many to delete
    Prints updated order list
    :param order_list: list (2D is of customer orders)
    :return:
    """

    # check if order_list is empty
    if len(order_list) == 0:
        print("_ "*30)
        # message letting user know there is no pasta to remove
        print("You have no items in the order")
        print("_ "*30)
        return None

    print("_" * 50)
    # printing out the order_list with indexes
    for i in range(0, len(order_list)):
        output = "{} : {} x {}".format(i, order_list[i][0], order_list[i][1])
        print(output)
        print("_"*50)

    # asking the user which pasta to remove
    which_index = get_integer("Which number pasta would you like to remove from?", 0, len(order_list)-1)
    # asking the user how many to remove
    quantity = get_integer("How many would you like to remove?")
    # removing the quantity of pasta from the order_list
    order_list[which_index][0] -= quantity

    # message informing user what they have removed
    output = "You have removed {} x {} from your order".format(quantity, order_list[which_index][1])
    print(output)

    # if user remove more than or equal to the amount of pasta remove pasta completely from order_list
    if order_list[which_index][0] <= 0:
        order_list.pop(which_index)

    # if nothing in order_list
    if len(order_list) == 0:
        print("_" * 50)
        # message telling user no items are in the order_list
        print("You now have no items in the order")
        print("_" * 50)
        # returning user to main menu
        return None

    print("_" * 50)
    # printing out the users order including totals
    print("This is your updated order - ")
    total = 0
    for x in order_list:
        subtotal = x[0] * x[2]
        total += subtotal
        output = "{} x {:<30} at ${:.2f}".format(x[0], x[1], subtotal)
        print(output)
    output = "Total = ${:.2f}".format(total)
    print(output)
    print("_" * 50)
    # returning user to main menu
    return None


def delivery_pick_up(customer_details, delivery_details, pickup_details):
    """
    Check if customer_details list is already full
    Lets user either clear details or return to main menu
    Asks for delivery or pick up
    Depending on delivery or pick up asks for name, number, address
    Prints out the information you entered
    Asks for confirmation
    :param customer_details: list with the customers details (for either delivery or pickup)
    :param delivery_details: list with the customers details for delivery
    :param pickup_details: list with the customers details for pick up
    :return: None

    """
    # check if list is not empty
    if len(customer_details) > 0:
        print("You have already entered the customer information")
        print("This is the customer information that was previously added")

        # print delivery details if not empty
        if len(delivery_details) > 0:
            print("_" * 50)
            print("This is the previously entered customer details for delivery")
            print("_" * 50)
            output = "Name: {} \nPhone Number: {} \nAddress: {}".format(delivery_details[0][0], delivery_details[0][1], delivery_details[0][2])
            print(output)
            print("_" * 50)

        # print pick up details if not empty
        elif len(pickup_details) > 0:
            print("_" * 50)
            print("This is the previously added customer details for pick up")
            print("_" * 50)
            output = "Name: {} \nPhone Number: {}".format(pickup_details[0][0], pickup_details[0][1])
            print(output)
            print("_" * 50)

        # loop for validating list_full input
        validate_list_full = False
        while validate_list_full == False:

            # asking user to either clear their previous information or return to main menu
            list_full = get_string("Press 'C' to clear customer information\nPress 'Y' if this information is correct and you would like to exit")
            # user can enter either upper case or lower case letters
            list_full = list_full.lower()

            # loop will stop if user enters either c or y
            if list_full in ["c", "y"]:
                # stops loop
                validate_list_full = True

            # loop will continue
            else:
                # error message if c or y is not entered
                print("You have not entered a valid input. Please enter either 'y' or 'c'")

            if list_full == "c":
                # all lists containing customer details will clear
                del customer_details[:]
                del pickup_details[:]
                del delivery_details[:]
                # message informing the user that their info has been cleared
                print("The information has been cleared")
                print("Please enter new information")

            elif list_full == "y":
                # message informing user their information is staying the same
                print("The customer information is staying the same ")
                # returning user to main menu
                return None

    # loop for info_confirm (whether user wants to confirm their details)
    confirm_details = False
    while confirm_details == False:
        # loop to validate pickup or delivery input
        deliv_pickup_loop = False
        while deliv_pickup_loop == False:
            # asking user if they want pick up or delivery
            user_choice = get_string("Would you like to pick up (p) your order or get it delivered (d)? ->")
            # user can enter either upper case or lower case letters
            user_choice = user_choice.lower()

            # if user inputs either p or d loop will stop
            if user_choice in ["p", "d"]:
                # stops loop
                deliv_pickup_loop = True

            # p or d is not entered
            # loop continues
            else:
                # error message
                print("You have not entered a valid input. Please enter either 'p' or 'd'")

            if user_choice == "p":
                # loop validating name input
                name_loop = False
                while name_loop == False:
                    # asking for users name
                    name = get_string("Please enter a name for your order->")
                    # name must be equal to or more than 2 characters
                    if len(name) >= 2:
                        # loop stops
                        name_loop = True

                    # if name is less than 2 characters
                    # loop continues
                    elif len(name) < 2:
                        # error messages informing user to enter at least 2 letters
                        print("You must enter at least 2 letters for your name")

                # loop validating users phone number length
                number_loop = False
                while number_loop == False:
                    # validate phone number
                    digit_loop = False
                    while digit_loop == False:
                        # asking for the users phone number
                        number = get_string("Please enter your phone number ->")
                        # phone number must be digits
                        if number.isdigit():
                            # digit_loop stops
                            digit_loop = True

                        else:
                            # error message
                            print("The phone number can only be numbers")

                    # must be more than 5 but less than 12 characters
                    if len(number) <= 5 or len(number) >= 12:
                        # loop continues
                        # error message informing user to enter a valid number
                        print("You have not entered a valid phone number.\n"
                              "Your number should be within 5-12 numbers")

                    elif len(number) >= 6:
                        # loop stops
                        number_loop = True

                # adding this name and number into both customer details and pick up details
                customer_details.append([name, number])
                pickup_details.append([name, number])

                # printing the information the user has entered for pick up
                print("_"*50)
                print("This is your Contact information for pickup")
                print("_" * 50)
                output = "Name: {} \nPhone Number: {}".format(pickup_details[0][0], pickup_details[0][1])
                print(output)
                print("_" * 50)

                # validating info_confirm
                info_loop = False
                while info_loop == False:
                    # asking user to confirm their details
                    info_confirm = get_string("CONFIRM DETAILS ('y' or 'n')")
                    # user may enter either upper case or lower case letters
                    info_confirm = info_confirm.lower()

                    # if user enters y or n
                    # loop stops
                    if info_confirm in ["y", "n"]:
                        info_loop = True

                    # user enters anything that is not y or n
                    # loop continues
                    else:
                        print("You have not entered a valid input. Please enter either 'y' or 'n'.")

                    # user enters y
                    # confirm_details loop stops
                    if info_confirm == "y":
                        confirm_details = True

                    # user enters n
                    elif info_confirm == "n":
                        # both customer_details and pickup details list clear
                        del customer_details[:]
                        del pickup_details[:]
                        # message telling user to re enter their details
                        print("Please enter details again.")

            # if user choose delivery
            elif user_choice == "d":
                # validating name input
                name_loop = False
                while name_loop == False:
                    # asking user for name
                    name = get_string("Please enter a name for your order->")
                    # if name is equal to or more than 2, loop stops
                    if len(name) >= 2:
                        # stops loop
                        name_loop = True

                    # name is less than 2
                    # loop continue
                    elif len(name) < 2:
                        print("You must enter at least 2 letters for your name")

                # validate number length loop
                number_loop = False
                while number_loop == False:
                    # validate number loop
                    digit_loop = False
                    while digit_loop == False:

                        number = get_string("Please enter your phone number ->")
                        # phone number must be only digits
                        if number.isdigit():
                            # digit_loop stops
                            digit_loop = True

                        else:
                            # error message
                            print("The phone number can only be numbers")

                    # number must be more than 5 and less than 12
                    if len(number) <= 5 or len(number) >= 12:
                        # number_loop continues
                        print("You have not entered a valid phone number.\n"
                              "Your number should be within 5-12 numbers")

                    elif len(number) >= 6:
                        # number_loop stops
                        number_loop = True

                # validating users address
                address_loop = False
                while address_loop == False:
                    # asking for users address
                    address = get_string("Please enter the address for delivery (Number, Street, Suburb) ->")
                    # if address more than 4 characters
                    if len(address) >= 5:
                        # address_loop stops
                        address_loop = True

                    # if address equal too or less than 3 characters
                    # address_loop continues
                    elif len(address) <= 4:
                        print("You have not entered a valid address. Please enter a valid address.")

                # adding the users details for delivery into these lists
                customer_details.append([name, number, address])
                delivery_details.append([name, number, address])

                # printing the customers details for delivery
                print("_" * 50)
                print("This is your Contact information for delivery")
                print("_" * 50)
                output = "Name : {} \nPhone number : {} \nAddress : {}".format(delivery_details[0][0], delivery_details[0][1], delivery_details[0][2])
                print(output)
                print("_" * 50)

                # validating info_confirm loop
                info_loop = False
                while info_loop == False:
                    # asking user to confirm their details for delivery
                    info_confirm = get_string("CONFIRM DETAILS ('y' or 'n')")
                    # user may enter either upper case or lower case letters
                    info_confirm = info_confirm.lower()

                    # if user inputs y or n
                    # info_loop will stop
                    if info_confirm in ["y", "n"]:
                        # stops loop
                        info_loop = True

                    # if anything other than y or n is entered
                    # info_loop continues
                    else:
                        # message informing user to input y or n
                        print("You have not entered a valid input. Please enter either 'y' or 'n'.")

                    # user input y
                    if info_confirm == "y":
                        # confirm_details loop stops
                        confirm_details = True

                    # user input n
                    elif info_confirm == "n":
                        # both customer and delivery lists are cleared
                        del customer_details[:]
                        del delivery_details[:]
                        # message telling user to enter their details again
                        print("Please enter details again.")


def confirm_order(order_list, delivery_details, pickup_details, customer_details):

    """
    Check if customer_details is full
    Check if order_list is full
    If not user is sent back to main menu
    Customer details and order is printed
    User is asked to confirm order
    User can order again or quit
    :param order_list: list (2D is of customer orders)
    :param delivery_details:  list with the customer details for delivery
    :param pickup_details: list with the customer details for pick up
    :param customer_details: list with the customers details (for either delivery or pickup)
    :return: None
    """

    # checking customer_details is empty
    if len(customer_details) == 0:
        print("_" * 50)
        # error message informing user that customer details have not been entered
        print("You have not entered your customer details.\nYou cannot confirm order without filling out your customer details first")
        print("_" * 50)
        # returning user to main menu
        return None

    # checking if order_list is empty
    if len(order_list) == 0:
        print("_"*50)
        # error message informing user that they have no pasta in their order
        print("You have no pastas in your order.\nOrder a pasta before you confirm your order")
        print("_" * 50)
        # returning user to main menu
        return None

    # checking if delivery_details is not empty
    if len(delivery_details) > 0:
        print("_"*50)
        # printing the delivery details
        print("THIS IS THE CUSTOMER DETAILS FOR DELIVERY")
        print("_" * 50)
        output = "Name: {} \nPhone Number: {} \nAddress: {}".format(delivery_details[0][0], delivery_details[0][1], delivery_details[0][2])
        print(output)
        print("_" * 50)

    # checking if pick up details is not empty
    elif len(pickup_details) > 0:
        print("_" * 50)
        # printing the pick up details
        print("THIS IS THE CUSTOMER DETAILS FOR PICK UP")
        print("_" * 50)
        output = "Name: {} \nPhone Number: {}".format(pickup_details[0][0], pickup_details[0][1])
        print(output)
        print("_" * 50)

    print("_"*50)
    print("YOUR ORDER - ")
    print("_" * 50)
    total = 0

    # printing user order including totals
    for x in order_list:
        subtotal = x[0] * x[2]
        total += subtotal
        output = "{} x {:<30} at ${:.2f}".format(x[0], x[1], subtotal)
        print(output)

    # if delivery_details is not empty
    if len(delivery_details) > 0:
        print("Delivery Charge of $3")
        # adding add $3 delivery charge to total
        total += 3

    # printing total
    output = "Total = ${}".format(total)
    print(output)
    print("_" * 50)

    # loop validating user_details for confirm order
    confirm_loop = False
    while confirm_loop == False:
        # asking user if they want to confirm order
        user_details = get_string("CONFIRM ORDER (Y/N)? ")
        # user can enter either upper case of lower case letters
        user_details = user_details.lower()

        # if user enters y or n
        # confirm_loop stops
        if user_details in ["y", "n"]:
            # stops loop
            confirm_loop = True

        # if anything other than y or n is entered
        # confirm loop continues
        else:
            # error message informing user to enter either y or n
            print("You have not entered an valid input. Please enter either 'y' or 'n'")

        if user_details == "y":
            print("_ "*30)
            # message informing user order is confirmed
            print("Your order has been confirmed")
            print("Thank you for ordering")

            # more info about delivery
            if len(delivery_details) > 0:
                print("THE ORDER WILL ARRIVE IN 20 MINUTES ")
                print("_ "*30)

            # more info about pick up
            elif len(pickup_details) > 0:
                print("We are located at 132 Cuba Street, Te Aro. Your order is ready for pick up in 20 minutes")

            # loop validating order_again
            again_loop = False
            while again_loop == False:
                # asking user if want to order again
                order_again = get_string("Would you like to order again (Y/N)?")
                # user may enter either lower case or upper case
                order_again = order_again.lower()

                # if user enter y or n
                # again_loop stops
                if order_again in ["y", "n"]:
                    # loop stops
                    again_loop = True

                # if anything other than y or n is entered
                else:
                    # error message informing user to enter either y or n
                    print("You have not entered a valid input. Please enter either 'y' or 'n'.")

                if order_again == "y":
                    # message informing user that the program will start again
                    print("The program will now start again")
                    # clearing all information the user has entered
                    del customer_details[:]
                    del delivery_details[:]
                    del pickup_details[:]
                    del order_list[:]
                    # returning user to the main menu
                    return None

                elif order_again == "n":
                    # message telling user that program is over
                    print("PROGRAM OVER")
                    # program will end
                    return False

        # user didn't confirm order
        elif user_details == "n":
            print("RETURNING THE MAIN MENU")
            # returning user to the main menu
            return None


def review_order(order_list, delivery_details):
    """
    Check if order list is empty
    Print the users order with totals delivery fee
    :param order_list: list (2D is of customer orders)
    :param delivery_details:  list with the customer details for delivery
    :return: None
    """
    print("*"*50)
    # total start at 0
    total = 0

    # checking if order_list is empty
    if len(order_list) == 0:
        # message informing user nothing is in the order
        print("You have no items in the order")
        # returning user to main menu
        return None

    # printing the order list with prices and totals
    for x in order_list:
        subtotal = x[0] * x[2]
        total += subtotal
        output = "{} x {:<30} at ${:.2f}".format(x[0], x[1], subtotal)
        print(output)

    # if delivery_details list is not empty
    # add on $3 to total
    if len(delivery_details) > 0:
        print("Delivery Charge of $3")
        # adding on $3
        total += 3

    # printing total
    output = "Total = ${}".format(total)
    print(output)
    print("*"*50)
    return None


def print_pasta(L):
    """
    Printing the pasta menu
    :param L: pasta list - list with the pastas and prices
    :return: None
    """
    # printing the pasta menu
    print("_" * 50)
    for x in L:
        output = "{} ${}".format(x[0], x[1])
        print(output)
    print("_" * 50)


def main():
    """
    :return: None
    """
    pasta_list = [
        ["Linguine Gamberi", 23],
        ["Fusilli Pesto", 19],
        ["Conchilglie alla Bolognese", 22],
        ["Rigatoni alla Caponata", 21],
        ["Fettuccine Carbonara", 20],
        ["Spaghetti Pomodoro", 16],
        ["Pappardelle Ricci D’Angello", 26],
        ["Raviolo di Salsiccia", 22],
        ["Ravioli di Ricotta", 20]
    ]

    menu_list = [
        ["P", "Print Pasta Menu"],
        ["A", "Add Pasta"],
        ["R", "Review Order"],
        ["D", "Delete from Order"],
        ["G", "Delivery or Pickup"],
        ["C", "Confirm Order"],
        ["Q", "Quit"]]

    order_list = []
    customer_details = []
    delivery_details = []
    pickup_details = []

    run_program = True
    while run_program:
        # printing the menu list
        for x in menu_list:
            output = "{} - {}".format(x[0], x[1])
            print(output)

        user_input = input("Press enter an option ->")
        # user can enter either upper case or lower case
        user_input = user_input.lower()
        if user_input == "p":
            # calling print pasta function
            print_pasta(pasta_list)
        elif user_input == "a":
            # calling add_to_order function
            add_to_order(pasta_list, order_list)
        elif user_input == "r":
            # calling review_order function
            review_order(order_list, delivery_details)
        elif user_input == "d":
            # calling delete_from_order function
            delete_from_order(order_list)
        elif user_input == "g":
            # calling delivery_pick_up function
            delivery_pick_up(customer_details, delivery_details, pickup_details)
        elif user_input == "c":
            # calling confirm_order function
            result = confirm_order(order_list, delivery_details, pickup_details, customer_details)
            if result is False:
                run_program = False
        elif user_input == "q":
            # quit the program
            run_program = False
            # message telling user they have quit
            print("You have quit")
        else:
            # error message
            print("You have not entered a valid option. Please try again.")

main()
