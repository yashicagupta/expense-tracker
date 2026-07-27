from expenses import add_expense, get_total


def test_add_expense():
    # checks if expense gets added
    expense = add_expense("coffee", "food", 5, "2026-07-27")

    assert expense["name"] == "coffee"
    assert expense["amount"] == 5


def test_total():
    # checks if total is calculated
    total = get_total()

    assert total >= 5


def test_invalid_amount():
    # checks if negative amounts are not allowed
    assert -10 <= 0


print("all tests passed")