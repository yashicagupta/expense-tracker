import json


def save_expenses(expenses):
    # saves expenses to a file
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def load_expenses():
    # loads expenses from a file
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []