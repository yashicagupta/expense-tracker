Expense Tracker

A simple Python expense tracker that allows users to add expenses, view saved expenses, and calculate total spending.

Features

- Add new expenses
- Store expenses using JSON
- View previous expenses
- Calculate total spending
- Validate user input
- Handle errors

Setup

1. Clone the repository
2. Run the program:

python3 main.py
Usage Example

Enter expense name: coffee
Enter category: food
Enter amount: 5
Enter date: 2026-07-27

Output:

coffee | food | $5.0 | 2026-07-27

total spending: $5.0

Files
- main.py - runs the program and handles user input
- expenses.py - manages expense functions
- storage.py - saves and loads expense data
- tests.py - tests project functions