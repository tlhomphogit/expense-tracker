import argparse
import csv
import os

# class Items:
#     def __init__(self, items):
#         self.items = items

#     def __str__(self):
#         return f'{self.items}'

class Expenses:
    def __init__(self):
        self.expenses = []

    def read_from_file(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'Error! The file {filepath} was not found.')
        
        with open(filepath, mode='r') as file:
            expense_data = csv.DictReader(file)

            for row in expense_data:
                row['amount'] = float(row['amount'])
                self.expenses.append(row)
        # return Items(self.expenses)
    def calc_total_spend(self):
        # amounts = [s.get('amount') for s in self.expenses] or ...
        amounts = [s['amount'] for s in self.expenses]
        self.total =  round(sum(amounts), 2)
        return self.total

    def print_recorded_expenses(self):
        print('-' * 110)
        print(f'{" ":<39} {"PERSONAL EXPENSE TRACKER"}')
        print('-' * 110)
        print(f'{"Item Name":<28} {"Amount":<10} {"Category":<12} {"Description"}')
        print('-' * 110)
        for items in self.expenses:
            print(f'{items["item_name"]:<28} {items["amount"]:<10} {items["category"]:<12} {items["description"]}')
        print('-' * 110)
        print(f'{"TOTAL":<28} {self.calc_total_spend()}')
        print('-' * 110)


file = '/home/wethinkcode/Documents/WeThinkCode/expense-tracker/expenses.csv'
expenses = Expenses()
expenses.read_from_file(file)
# items = Items(expenses.read_from_file(file))
expenses.print_recorded_expenses()