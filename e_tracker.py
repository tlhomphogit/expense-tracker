import argparse
import csv

class Expense:
    def __init__(self):
        self.expense = []

    def read_from_file(self, filepath):
        vision = []
        with open(filepath, mode='r') as file:
            expense_data = csv.DictReader(file)

        for row in expense_data:
            self.expense.append(row)

    def __str__(self):
        return f'{self.expense}'

    
expense = Expense()
print(expense.read_from_file('/home/wethinkcode/Documents/WeThinkCode/expense-tracker/expenses.csv'))