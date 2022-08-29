def print_pasta(L):
    print("_" * 50)
    for x in L:
        output = "{} {}".format(x[0], x[1])
        print(output)
    print("_"*50)

def main():
    pasta_list = [
        ["Linguine Gamberi", "$23"],
        ["Fusilli Pesto", "$19"],
        ["Conchilglie alla Bolognese", "$22"],
        ["Rigatoni alla Caponata", "$21"],
        ["Fettuccine Carbonara", "$20"],
        ["Spaghetti Pomodoro", "$16"],
        ["Pappardelle Ricci D’Angello", "$26"],
        ["Raviolo di Salsiccia", "$22"],
        ["Ravioli di Ricotta", "$20"]
        ]

    menu_list = [
        ["p", "Print Pasta"],
        ["q", "Quit"]]

    run_program = True
    while run_program:
        for x in menu_list:
            output = "{} {}".format(x[0], x[1])
            print(output)
        user_input = input("Press enter an option ->")
        if user_input == "p":
            print_pasta(pasta_list)
        elif user_input == "q":
            run_program = False
            print("You have quit")

main()