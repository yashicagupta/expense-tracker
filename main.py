from expenses import add_expense, view_expenses


def main():
    # adds an expense
    name = input("enter expense name: ")
    category = input("enter category: ")
    amount = float(input("enter amount: "))
    date = input("enter date: ")

    add_expense(name, category, amount, date)

    print("\ncurrent expenses:")
    view_expenses()


main()