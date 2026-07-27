from expenses import add_expense, view_expenses


def main():
    # gets expense details from user
    name = input("enter expense name: ")
    category = input("enter category: ")

    try:
        amount = float(input("enter amount: "))

        if amount <= 0:
            print("amount must be positive")
            return

    except ValueError:
        print("please enter a valid number")
        return

    date = input("enter date: ")

    if name == "" or category == "":
        print("name and category cannot be empty")
        return

    add_expense(name, category, amount, date)

    print("\ncurrent expenses:")
    view_expenses()


main()