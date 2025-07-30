# Personal Finance Management App (CLI)

## Project Description
This is a simple command-line interface (CLI) application built with Python that helps users track their personal finances. It allows for the input of income and expenses, provides a summary of all transactions, and calculates the current net balance. All financial data is persistently stored in a JSON file, ensuring that no information is lost when the application is closed.

This project demonstrates fundamental Python programming concepts, including data structures (lists and dictionaries), functions, control flow (loops and conditionals), user input/output, basic error handling, and file operations with JSON for data persistence.

## Features
* **Add Income:** Record income with an amount, category, and description.
* **Add Expense:** Record expenses with an amount, category, and description.
* **View Transactions:** Display a comprehensive list of all recorded income and expenses.
* **View Balance:** Get an instant overview of total income, total expenses, and the current net balance.
* **Data Persistence:** All transactions are automatically saved to `transactions.json` and loaded on startup, preserving your financial history.

## Technologies Used
* **Python 3.x**
* **JSON** (for data storage)

## How to Run the Application

### Prerequisites
* Ensure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps:
1.  **Clone the Repository (or download the files):**
    If you are using Git:
    ```bash
    git clone https://github.com/Degefa-Gomora/ 
    cd PersonalFinanceApp
    ```
    (If you don't have Git, simply download the `main.py` and `README.md` files into a folder.)

2.  **Run the application:**
    Open your terminal or command prompt, navigate to the `PersonalFinanceApp` directory (where `main.py` is located), and run:
    ```bash
    python main.py
    ```

## How to Use
Upon running the application, you will be presented with a menu of options:
* **1. Add Income:** Follow the prompts to enter the amount, category (e.g., Salary, Gift), and a description for your income.
* **2. Add Expense:** Follow the prompts to enter the amount, category (e.g., Food, Transport, Rent), and a description for your expense.
* **3. View Transactions:** Displays a numbered list of all your recorded incomes and expenses.
* **4. View Balance:** Shows your total income, total expenses, and your current net financial balance.
* **5. Exit:** Closes the application. All data is automatically saved.

## Future Enhancements (Potential Next Steps)
* Add functionality to edit or delete existing transactions.
* Implement filtering of transactions by date or category.
* Develop reporting features (e.g., monthly summaries, spending by category).
* Introduce budgeting tools to set limits on expenses.
* Migrate to a simple database (like SQLite) for more robust data management.
* Develop a graphical user interface (GUI) using libraries like Tkinter or PyQt.

## Author
Degefa Gomora
LinkedIn: https://www.linkedin.com/in/degefa-gomora-4ba34530b/
Portifolio:https://portifolio.degefagomora.com/
