from collections import defaultdict
from datetime import datetime


def show_menu():
    """Display the main menu options fot the user terminal interface."""
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    print("4. View Summary")
    print("5. Export Expenses")
    print("6. Edit Expense")
    print("7. Delete Expense")

    return input("Select an option: ")

def get_expense_input():
    while True:
        amount = input("Amount: ")
        try:
            amount = float(amount)
            if amount <= 0 or amount > 1_000_000_000:
                raise ValueError
            break
        except ValueError:
            print("❌ Please enter a valid amount between 0 and 1,000,000,000.")

    while True:
        category = input("Category: ").strip()
        if not category:
            print("❗ Category cannot be empty.")
        elif not category.isalpha():
            print("❌ Category should only contain letters.")
        else:
            break

    notes = input("Notes (optional): ").strip()

    return amount, category, notes


def display_expenses(expenses):
    """Takes a list of expenses and prints each one in a readable format."""
    if not expenses:
        print("No expenses recorded.")
        return
    for exp in expenses:
        print(f"[{exp['id'][:8]}] {exp['date']} - {exp['category']} - ${exp['amount']} - {exp['notes']}")
        
def show_summary(expenses):
    """Display a summary of expenses"""
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
    print("\n📤 Export Formats:")
    print("1. CSV")
    print("2. JSON")
    return input("Choose a format (1 or 2): ")

        