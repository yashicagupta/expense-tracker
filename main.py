from expenses import add_expense


def main():
    # gets expense details from user
    name = input("enter expense name: ")
    category = input("enter category: ")
    amount = float(input("enter amount: "))
    date = input("enter date: ")

    expense = add_expense(name, category, amount, date)

    print("expense added:", expense)


main()