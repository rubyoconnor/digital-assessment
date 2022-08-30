def get_string(m):
    my_string = input(m)
    return my_string


def get_integer(m):
    my_integer = int(input(m))
    return my_integer

def add_to_order(L, order_list):
    print("_" * 50)
    for i in range(0, len(L)):
        output = "{} : {} ${}".format(i, L[i][0], L[i][1])
        print(output)
    print("_" * 50)

    which_pasta = get_integer("Which number pasta would you like to order?")
    quantity = get_integer("How many would you like to order?")

    output = "You have added {} {} to your order".format(quantity, L[which_pasta][0])
    print(output)

    order_list.append([quantity, L[which_pasta][0], L[which_pasta][1]])


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


def review_order(order_list):
    print("_" * 50)
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
        ["q", "Quit"]]

    order_list = []
    order_list = [[4, "Ravioli di Ricotta", 20], [3, "Spaghetti Pomodoro", 16]]

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
            review_order(order_list)
        elif user_input == "d":
            delete_from_order(order_list)
        elif user_input == "q":
            run_program = False
            print("You have quit")


main()









