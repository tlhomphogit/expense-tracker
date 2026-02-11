from e_tracker import Expenses

class Items:
    def __init__(self, items):
        self.items = items

    def filter_by_category(self):  
        ctgrs = [s['category'] for s in self.items]
        categories = list(set(ctgrs))

        print(f'Filter by categories:')
        print(', '.join(categories))
        filter_by = input('Filter by: ')

        filtered = [
            {'item_name': s['item_name'],'category': s['category'], 'amount': s['amount']} for s in self.items if s['category'] == filter_by
        ]

        for items in filtered:
            print(f'{items["item_name"]:<28} {items["amount"]:<10} {items["category"]:<12}')
    
file = 'expenses.csv'
expenses = Expenses()
expenses.read_from_file(file)
items = Items(expenses.to_items())
items.filter_by_category()
    