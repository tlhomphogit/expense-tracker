# Expense Tracker Project Overview

This project is a Personal Expense Tracker that allows users to manage and track their expenses efficiently.

## Features

### e_tracker.py
- **Read Expenses from CSV**: The `Expenses` class reads expense data from a CSV file, ensuring that users can easily import their existing records.
- **Calculate Total Spend**: Calculates the total amount spent based on the imported data, providing users with a clear overview of their financial activities.
- **Display Recorded Expenses**: Prints a formatted table of recorded expenses with the following columns:
  - Item Name
  - Amount
  - Category
  - Description
- **Get Items**: The `to_items()` method returns the list of expenses for use by other modules.

### items.py
- **Filter by Category**: The `Items` class allows users to filter expenses by a specific category.
- **Interactive Category Selection**: Displays all available expense categories and prompts the user to select one for filtering.
- **Filtered Display**: Shows filtered results in a formatted table displaying item name, amount, and category.

## Modules

### Expenses Class (e_tracker.py)
- `__init__()`: Initializes an empty list of expenses.
- `read_from_file(filepath)`: Reads expense data from a CSV file.
- `to_items()`: Returns the list of expenses.
- `calc_total_spend()`: Calculates and returns the total amount spent.
- `print_recorded_expenses()`: Displays all expenses in a formatted table with the total.

### Items Class (items.py)
- `__init__(items)`: Initializes with a list of expense items.
- `filter_by_category()`: Filters expenses by category and displays the results.

## Usage
1. Ensure you have a CSV file with the following headers: `item_name`, `amount`, `category`, and `description`.
2. **To view all expenses**: Run `e_tracker.py` to read and display all recorded expenses with the total amount spent.
3. **To filter expenses by category**: Run `items.py` to filter expenses by a selected category.

## Requirements
- Required libraries: `argparse`, `csv`, `os`