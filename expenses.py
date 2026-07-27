expenses = []


def add_expense(name, category, amount, date):
    # creates a new expense
    expense = {
        "name": name,
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)

    return expense