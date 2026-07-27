from storage import load_expenses, save_expenses

expenses = load_expenses()


def add_expense(name, category, amount, date):
    # creates a new expense
    expense = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)

    # saves the expense
    save_expenses(expenses)

    return expense


def view_expenses():
    # shows all expenses
    if not expenses:
        print("no expenses found")
        return

    for expense in expenses:
        print(
            expense["name"],
            "|",
            expense["category"],
            "|",
            "$" + str(expense["amount"]),
            "|",
            expense["date"]
        )


def get_total():
    # calculates total spending
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total