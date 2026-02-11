# Expense Tracker Project Overview

This project is a Personal Expense Tracker that allows users to manage and track their expenses efficiently.

## Features
- **Read Expenses from CSV**: The application reads expense data from a CSV file, ensuring that users can easily import their existing records.
- **Calculate Total Spend**: It calculates the total amount spent based on the imported data, providing users with a clear overview of their financial activities.
- **Display Recorded Expenses**: The application prints a formatted list of recorded expenses, including item name, amount, category, and description.

## Usage
1. Ensure you have a CSV file with the following headers: `item_name`, `amount`, `category`, and `description`.
2. Run the script to read the expenses and display them in a formatted manner.

## Requirements
- Required libraries: `argparse`, `csv`, `os`