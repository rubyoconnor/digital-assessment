
def get_string(m):
    my_string =input(m)
    return my_string

def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def add_to_order(L ,order_list):
    print("_" * 50)
    for i in range(0, len(L)):
        output = "{} : {} ${}".format(i, L[i][0], L[i][1])
        print(output)
    print("_" * 50)

    which_pasta = get_integer("Which number pasta would you like to order?")
    quantity = get_integer("How many would you like to order?")

    output = "You have added {} {} to your order".format(quantity, L[which_pasta][0])
    print(output)

    order_list.append([quantity, L[which_pasta][0],  L[which_pasta][1]])

def delete_from_order(order_list):
    print("_" * 50)
    for i in range(0, len(order_list)):
        output = "{} : {} x {}".format(i, order_list[i][0], order_list[i][1])
        print(output)
        print("_" * 50)

    which_index = get_integer("Which number pasta would you like to remove from?")
    quantity = get_integer("How many would you like to remove?")
    order_list[which_index][0] -= quantity

    if order_list[which_index][0] <= 0:
        output = "You have removed {} x {} from your order".format(quantity, order_list[which_index][1])
        print(output)
        order_list.pop(which_index)


    if len(order_list) == 0:
        print("_ " *50)
        print("You have no items in the order")
        print("_ " *50)

        return None

    print("_" * 50)
    print("This is your updated order")
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

        list_full = get_string("Press 'C' to clear customer information\nPress 'Y' if this information is correct and you would like to exit")

        if list_full == "c":
            del customer_details[:]
            del pickup_details[:]
            del delivery_details[:]
            print("The information has been cleared")
            print("Please enter new information")

        elif list_full == "y":
            print("The customer information is staying the same ")
            return None

    user_choice = get_string("Would you like to pick up (p) your order or get it delivered (d)? ->")

    if user_choice == "p":
        name = get_string("Please enter a name for your order->")
        number = get_string("Please enter your phone number ->")

        customer_details.append([name, number])
        pickup_details.append([name, number])

        print("This is your contact information for your order")
        print("_" * 50)


        output = "Name: {} \nPhone Number: {}".format(pickup_details[0][0], pickup_details[0][1])
        print(output)
        print("_" * 50)




    elif user_choice == "d":
        name = get_string("Please enter a name for your order ->")
        number = get_string("Please enter a phone number for your order -> ")
        address = get_string("Pleas enter the address for delivery (Number, Street, Suburb) ->")
        customer_details.append([name, number, address])
        delivery_details.append([name ,number ,address])

        print("This is your information for your order")
        print("_" * 50)

        output = "Name : {} \nPhone number : {} \nAddress : {}".format(delivery_details[0][0], delivery_details[0][1], delivery_details[0][2])
        print(output)
        print("_" * 50)

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

    user_details = get_string("COMFIRM ORDER (Y/N)? ")
    if user_details == "y":
        print("THANK YOU FOR ORDERING")
        print("YOUR ORDER HAS BEEN CONFIRMED")

        order_again = get_string("Would you like to order again (Y/N)?")
        if order_again == "y":
            print("New order starting...")
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
    print("_" * 50)
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
    print("_" * 50)
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
        ["p", "Print Pasta"],
        ["a", "Add Pasta"],
        ["r", "Review Order"],
        ["d", "Delete from Order"],
        ["g", "Delivery or Pickup"],
        ["c", "Confirm Order"],
        ["q", "Quit"]]

    order_list = []
    order_list = [[4, "Ravioli di Ricotta", 20], [3, "Spaghetti Pomodoro", 16]]

    customer_details = []

    delivery_details = []

    pickup_details = []

    run_program = True
    while run_program:
        for x in menu_list:
            output = "{} {}".format(x[0], x[1])
            print(output)
        user_input = input("Press enter an option ->")
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
                run_program =False
        elif user_input == "q":
            run_program = False
            print("You have quit")

main()















