# # main.py
"""
Personal Finance Management App

This command-line application allows users to track their income and expenses,
view all transactions, and calculate their current balance.
All data is saved to a JSON file for persistence between sessions.
"""

import json # Import the json module for data persistence

# Global list to store all transactions. Each transaction is a dictionary.
transactions = []
# Name of the file where transactions will be saved/loaded.
TRANSACTIONS_FILE = 'transactions.json'

def save_transactions():
    """
    Saves the current transactions list to a JSON file.

    Handles potential IOError during file writing.
    """
    try:
        with open(TRANSACTIONS_FILE, 'w') as file:
            # json.dump writes the Python list to the file in JSON format.
            # indent=4 makes the JSON file human-readable with nice formatting.
            json.dump(transactions, file, indent=4)
        # print("Transactions saved successfully!") # Optional: uncomment for confirmation during development
    except IOError as e:
        print(f"Error saving transactions: {e}")

def load_transactions():
    """
    Loads transactions from a JSON file into the global transactions list.

    Handles FileNotFoundError (first run), JSONDecodeError (corrupted file),
    and other potential exceptions during file reading.
    """
    global transactions # Declare 'transactions' as global to modify the top-level list
    try:
        with open(TRANSACTIONS_FILE, 'r') as file:
            # Clear existing in-memory transactions before loading new ones
            transactions.clear()
            # json.load reads the JSON data from the file and converts it back to a Python list.
            loaded_data = json.load(file)
            # Add all loaded items to the global transactions list
            transactions.extend(loaded_data)
        # print("Transactions loaded successfully!") # Optional: uncomment for confirmation during development
    except FileNotFoundError:
        # This is expected on the first run when the file doesn't exist yet
        print("No existing transactions file found. Starting fresh.")
    except json.JSONDecodeError:
        # Handles cases where the JSON file might be malformed or corrupted
        print("Error reading transactions file. It might be corrupted. Starting fresh.")
    except Exception as e:
        # Catch any other unexpected errors during loading
        print(f"An unexpected error occurred while loading: {e}")


def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n--- Personal Finance Manager ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. View Balance")
    print("5. Exit")
    print("--------------------------------")

def add_income():
    """
    Prompts the user for income details (amount, category, description)
    and adds it as a dictionary to the global transactions list.
    Includes error handling for invalid amount input.
    """
    try:
        amount = float(input("Enter income amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return

        category = input("Enter income category (e.g., Salary, Gift): ")
        description = input("Enter a brief description: ")

        transaction = {
            'type': 'income',
            'amount': amount,
            'category': category,
            'description': description
        }
        transactions.append(transaction)
        print("Income added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number (e.g., 100 or 50.50).")
    except Exception as e:
        print(f"An unexpected error occurred while adding income: {e}")

def add_expense():
    """
    Prompts the user for expense details (amount, category, description)
    and adds it as a dictionary to the global transactions list.
    Includes error handling for invalid amount input.
    """
    try:
        amount = float(input("Enter expense amount: "))
        if amount <= 0:
            print("Amount must be positive.")
            return

        category = input("Enter expense category (e.g., Food, Transport, Rent): ")
        description = input("Enter a brief description: ")

        transaction = {
            'type': 'expense',
            'amount': amount,
            'category': category,
            'description': description
        }
        transactions.append(transaction)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a number (e.g., 100 or 50.50).")
    except Exception as e:
        print(f"An unexpected error occurred while adding expense: {e}")

def view_transactions():
    """
    Displays all recorded transactions from the global transactions list.
    If no transactions exist, a message is printed.
    """
    if not transactions:
        print("No transactions recorded yet.")
        return

    print("\n--- All Transactions ---")
    # enumerate provides both the index (i) and the item (transaction)
    for i, transaction in enumerate(transactions):
        transaction_type = transaction['type'].capitalize() # Capitalize "income" to "Income" etc.
        amount = transaction['amount']
        category = transaction['category']
        description = transaction['description']

        # f-string formatting: .2f ensures two decimal places for currency
        print(f"{i+1}. Type: {transaction_type}, Amount: ${amount:.2f}, Category: {category}, Description: {description}")
    print("------------------------")

def view_balance():
    """
    Calculates the total income, total expense, and net balance
    from the global transactions list and displays them.
    """
    total_income = 0
    total_expense = 0

    if not transactions:
        print("No transactions recorded yet. Balance is $0.00")
        return # Exit function if no transactions

    for transaction in transactions:
        if transaction['type'] == 'income':
            total_income += transaction['amount']
        elif transaction['type'] == 'expense':
            total_expense += transaction['amount']

    current_balance = total_income - total_expense

    print("\n--- Current Balance ---")
    print(f"Total Income:  ${total_income:.2f}")
    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Net Balance:   ${current_balance:.2f}")
    print("-----------------------")


def main():
    """
    Main function to run the Personal Finance Manager application.
    It loads data on startup and saves data after each modification and before exiting.
    """
    load_transactions() # Load transactions when the application starts

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_income()
            save_transactions() # Save after adding new income
        elif choice == '2':
            add_expense()
            save_transactions() # Save after adding new expense
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            view_balance()
        elif choice == '5':
            save_transactions() # Save final state before exiting
            print("Exiting Personal Finance Manager. Goodbye!")
            break # Exit the while loop
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()