"""CLI utilities for interacting with the Expense Tracker application."""

from collections import defaultdict
from datetime import datetime


def show_menu():
    """Display the main menu options for the user terminal interface."""
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    print("4. View Summary")
    print("5. Export Expenses")
    print("6. Edit Expense")
    print("7. Delete Expense")

    return input("Select an option: \n")


def get_expense_input():
    """Prompt user for expense input with validation and return the result."""
    while True:
        amount = input("Amount: \n")
        try:
            amount = float(amount)
            if amount <= 0 or amount > 1_000_000_000:
                raise ValueError
            break
        except ValueError:
            print("❌ Please enter a valid amount between 0 and 1,000,000,000.")

    while True:
        category = input("Category: \n").strip()
        if not category:
            print("❗ Category cannot be empty.")
        elif not category.isalpha():
            print("❌ Category should only contain letters.")
        else:
            break

    notes = input("Notes (optional): \n").strip()

    return amount, category, notes


def display_expenses(expenses):
    """Print each expense in a readable format."""
    if not expenses:
        print("No expenses recorded.")
        return

    for exp in expenses:
        print(
            f"[{exp['id'][:8]}] {exp['date']} - {exp['category']} - "
            f"${exp['amount']} - {exp['notes']}"
        )


def show_summary(expenses):
    """Display a summary of expenses."""
    if not expenses:
        print("No expenses to summarize.")
        return

    monthly_total = defaultdict(float)
    category_total = defaultdict(float)

    for exp in expenses:
        try:
            date = datetime.strptime(exp["date"], "%Y-%m-%d")
            month_key = date.strftime("%Y-%m")
            monthly_total[month_key] += float(exp["amount"])
            category_total[exp["category"]] += float(exp["amount"])
        except Exception as e:
            print(f"Skipping an invalid expense entry: {e}")

    print("\n📆 Monthly Total:")
    for month, total in monthly_total.items():
        print(f"  {month}: ${total:.2f}")

    print("\n📂 Category Total:")
    for cat, total in category_total.items():
        print(f"  {cat}: ${total:.2f}")


def ask_export_format():
    """Prompt user to choose a format for exporting expenses."""
    print("\n📤 Export Formats:")
    print("1. CSV")
    print("2. JSON")
    return input("Choose a format (1 or 2): \n")
