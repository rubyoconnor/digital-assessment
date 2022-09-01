def get_string(m):
    string_loop = True
    while string_loop == True:
        my_string =input(m)

        if len(my_string) == 0:
            print("you have not entered anything. Please redo")
            continue

        return my_string

def get_integer(m, a=0, b=5):
    integer_loop = True
    while integer_loop == True:
        try:
            my_integer = int(input(m))
        except ValueError:
            print("You have not entered a number. Please enter a number")
            continue
        if my_integer < a or my_integer >b:
            print("You have not entered a valid number.")
            continue
        return my_integer

def add_to_order(L ,order_list):
    """
    :param L: list (list of all the pastas)
    :param order_list: list (2D is of customer orders)
    :return: None
    """
    print("_" * 50)
    for i in range(0, len(L)):
        output = "{} : {} ${}".format(i, L[i][0], L[i][1])
        print(output)
        print("_" * 50)

    which_pasta = get_integer("Which number pasta would you like to order?",0,len(L)-1)

    quantity = get_integer("How many would you like to order?\nPlease note you are not allowed to order more than 5 of the same pasta.\nEnter Amount: ")

    print("_"*70)
    output = "{} {} have been added to your order".format(quantity, L[which_pasta][0])
    print(output)
    print("_"*70)


    order_list.append([quantity, L[which_pasta][0],  L[which_pasta][1]])

def delete_from_order(order_list):

    if len(order_list) == 0:
        print("_ "*30)
        print("You have no items in the order")
        print("_ "*30)
        return None

    print("_" * 50)
    for i in range(0, len(order_list)):
        output = "{} : {} x {}".format(i, order_list[i][0], order_list[i][1])
        print(output)
        print("_"*50)

    which_index = get_integer("Which number pasta would you like to remove from?",0, len(order_list)-1)
    quantity = get_integer("How many would you like to remove?")
    order_list[which_index][0] -= quantity

    if order_list[which_index][0] <= 0:
        output = "You have removed {} x {} from your order".format(quantity, order_list[which_index][1])
        print(output)
        order_list.pop(which_index)


    if len(order_list) == 0:
        print("_" *50)
        print("You now have no items in the order")
        print("_" *50)
        return None

    print("_" * 50)
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
    return None

def delivery_pick_up(customer_details, delivery_details, pickup_details):

    # check if list is not empty
    # option to leave
    # if continue clear current list


    if len(customer_details) > 0:
        print("You have already entered the customer information")
        print("This is the customer information that was previously added")

        if len(delivery_details) > 0:
            print("_" * 50)
            print("This is the previously entered customer details for delivery")
            print("_" * 50)

            output = "Name: {} \nPhone Number: {} \nAddress: {}".format(delivery_details[0][0], delivery_details[0][1],
                                                                        delivery_details[0][2])
            print(output)
            print("_" * 50)

        elif len(pickup_details) > 0:
            print("_" * 50)
            print("This is the previously added customer details for pick up")
            print("_" * 50)

            output = "Name: {} \nPhone Number: {}".format(pickup_details[0][0], pickup_details[0][1])
            print(output)
            print("_" * 50)

        validate_list_full = False
        while validate_list_full == False:

            list_full = get_string("Press 'C' to clear customer information\nPress 'Y' if this information is correct and you would like to exit")
            list_full = list_full.lower()

            if list_full in ["c","y"]:
                validate_list_full = True

            else:
                print("You have not entered a valid input. Please enter either 'y' or 'c'")

            if list_full == "c":
                del customer_details[:]
                del pickup_details[:]
                del delivery_details[:]
                print("The information has been cleared")
                print("Please enter new information")

            elif list_full == "y":
                print("The customer information is staying the same ")
                return None

    confirm_details = False
    while confirm_details == False:
        deliv_pickup_loop = False
        while deliv_pickup_loop == False:
            user_choice = get_string("Would you like to pick up (p) your order or get it delivered (d)? ->")
            user_choice = user_choice.lower()

            if user_choice in ["p", "d"]:
                deliv_pickup_loop = True

            else:
                print("You have not entered a valid input. Please enter either 'p' or 'd'")

            if user_choice == "p":
                name_loop = False
                while name_loop == False:
                    name = get_string("Please enter a name for your order->")
                    if len(name) >= 2:
                        name_loop = True

                    elif len(name) < 2:
                        print("not valid. too short")

                number_loop = False
                while number_loop == False:
                    number = get_string("Please enter your phone number ->")
                    if len(number) <= 5 or len(number) >= 12:
                        print("you have not entered a valid number")

                    elif len(number) >= 6:
                        number_loop = True

                customer_details.append([name, number])
                pickup_details.append([name, number])

                print("_"*50)
                print("This is your Contact information for pickup")
                print("_" * 50)
                output = "Name: {} \nPhone Number: {}".format(pickup_details[0][0], pickup_details[0][1])
                print(output)
                print("_" * 50)

                info_loop = False
                while info_loop == False:
                    info_confirm = get_string("CONFIRM DETAILS ('y' or 'n'")
                    info_confirm = info_confirm.lower()

                    if info_confirm in ["y", "n"]:
                        info_loop = True

                    else:
                        print("you have not entered a valid input")

                    if info_confirm == "y":
                        confirm_details = True


                    elif info_confirm == "n":
                        del customer_details[:]
                        del pickup_details[:]
                        print("okay please enter details again")

            elif user_choice == "d":
                name_loop = False
                while name_loop == False:
                    name = get_string("Please enter a name for your order->")
                    if len(name) >= 2:
                        name_loop = True

                    elif len(name) < 2:
                        print("not valid. too short")

                number_loop = False
                while number_loop == False:
                    number = get_string("Please enter your phone number ->")

                    if len(number) <= 5 or len(number) >= 12:
                        print("you have not entered a valid number")

                    elif len(number) >= 6:
                        number_loop = True

                address_loop = False
                while address_loop == False:
                    address = get_string("Pleas enter the address for delivery (Number, Street, Suburb) ->")
                    if len(address) >= 4:
                        address_loop = True
                    elif len(address) <=3:
                        print("you have not entered a valid address. Please enter a valid address.")

                customer_details.append([name, number, address])
                delivery_details.append([name ,number ,address])

                print("_" * 50)
                print("This is your Contact information for pickup")
                print("_" * 50)
                output = "Name : {} \nPhone number : {} \nAddress : {}".format(delivery_details[0][0], delivery_details[0][1], delivery_details[0][2])
                print(output)
                print("_" * 50)

                info_loop = False
                while info_loop == False:
                    info_confirm = get_string("CONFIRM DETAILS ('y' or 'n'")
                    info_confirm = info_confirm.lower()

                    if info_confirm in ["y","n"]:
                        info_loop = True

                    else:
                        print("you have not entered a valid input")

                    if info_confirm == "y":
                        confirm_details = True


                    elif info_confirm == "n":
                        del customer_details[:]
                        del delivery_details[:]
                        print("okay please enter details again")

def confirm_order(order_list, delivery_details, pickup_details, customer_details):

    if len(customer_details) == 0:
        print("_" * 50)
        print("You have not entered your customer details. You cannot confirm order without filling out your customer details first")
        print("_" * 50)
        return None

    if len(order_list) == 0:
        print("_"*50)
        print("You have no pastas in your order. Order a pasta before you confirm your order")
        print("_" * 50)
        return None

    if len(delivery_details) > 0:
        print("_"*50)
        print("THIS IS THE CUSTOMER DETAILS FOR DELIVERY")
        print("_" * 50)

        output = "Name: {} \nPhone Number: {} \nAddress: {}".format(delivery_details[0][0], delivery_details[0][1], delivery_details[0][2])
        print(output)
        print("_" * 50)

    elif len(pickup_details) > 0:
        print("_" * 50)
        print("THIS IS THE CUSTOMER DETAILS FOR PICK UP")
        print("_" * 50)


        output = "Name: {} \nPhone Number: {}".format(pickup_details [0][0], pickup_details [0][1])
        print(output)
        print("_" * 50)


    print("_"*50)
    print("YOUR ORDER - ")
    print("_" * 50)
    total = 0

    for x in order_list:
        subtotal = x[0] * x[2]
        total += subtotal
        output = "{} x {:<30} at ${:.2f}".format(x[0], x[1], subtotal)
        print(output)

    if len(delivery_details) > 0:
        print("Delivery Charge of $3")
        total += 3

    output = "Total = ${}".format(total)
    print(output)
    print("_" * 50)

    confirm_loop = False
    while confirm_loop == False:
        user_details = get_string("COMFIRM ORDER (Y/N)? ")
        user_details = user_details.lower()

        if user_details in ["y","n"]:
            confirm_loop = True

        else:
            print("you have not entered an valid input.")

        if user_details == "y":
            print("_ "*30)
            print("Your order has been confirmed")
            print("Thank you for ordering")

            if len(delivery_details) > 0:
                print("YOUR ORDER WILL ARRIVE IN 20 MINUTES ")
                print("_ "*30)

            elif len(pickup_details) > 0:
                print("We are located at 132 Cuba Street, Te Aro. Your order is ready for pick up in 20 minutes")

            again_loop = False
            while again_loop == False:

                order_again = get_string("Would you like to order again (Y/N)?")
                order_again = order_again.lower()

                if order_again in ["y","n"]:
                    again_loop = True

                else:
                    print("you have not entered a valid input")

                if order_again == "y":
                    print("The program will now start again")
                    del customer_details[:]
                    del delivery_details[:]
                    del pickup_details[:]
                    del order_list[:]
                    return None

                elif order_again == "n":
                    print("Program over")
                    return False

        elif user_details == "n":
            print("RETURNING THE MAIN MENU")
            return None


def review_order(order_list, delivery_details):
    print("*"*50)

    total = 0

    if len(order_list) == 0:
        print("You have no items in the order")
        return None

    for x in order_list:
        subtotal = x[0] * x[2]
        total += subtotal
        output = "{} x {:<30} at ${:.2f}".format(x[0], x[1], subtotal)
        print(output)


    if len(delivery_details) > 0:
        print("Delivery Charge of $3")
        total += 3

    output = "Total = ${}".format(total)
    print(output)
    print("*"*50)
    return None

def print_pasta(L):
    print("_" * 50)
    for x in L:
        output = "{} ${}".format(x[0], x[1])
        print(output)
    print("_" * 50)

def main():
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
        for x in menu_list:
            output = "{} - {}".format(x[0], x[1])
            print(output)

        user_input = input("Press enter an option ->")
        user_input = user_input.lower()
        if user_input == "p":
            print_pasta(pasta_list)
        elif user_input == "a":
            add_to_order(pasta_list, order_list)
        elif user_input == "r":
            review_order(order_list, delivery_details)
        elif user_input == "d":
            delete_from_order(order_list)
        elif user_input == "g":
            delivery_pick_up(customer_details, delivery_details, pickup_details)
        elif user_input == "c":
            result = confirm_order(order_list, delivery_details, pickup_details, customer_details)
            if result is False:
                run_program = False
        elif user_input == "q":
            run_program = False
            print("You have quit")
        else:
            print("You have not entered a valid option. Please try again.")

main()


















