"""Main runner for the Expense Tracker CLI."""

import json
from controllers.expense_controller import (
    create_expense,
    save_expense,
    load_expenses,
    DATA_FILE
)
from views.cli import (
    show_menu,
    get_expense_input,
    display_expenses,
    show_summary,
    ask_export_format
)
from controllers.exporter import export_to_csv, export_to_json


def main():
    """Run the Expense Tracker CLI application."""
    print("👋 Welcome to the Expense Tracker CLI!")

    while True:
        choice = show_menu()

        if choice == "1":
            amount, category, notes = get_expense_input()
            expense = create_expense(amount, category, notes)
            save_expense(expense)
            print("✅ Expense saved successfully!")

        elif choice == "2":
            expenses = load_expenses()
            display_expenses(expenses)

        elif choice == "3":
            print("👋 Exiting the Expense Tracker. Goodbye!")
            break

        elif choice == "4":
            expenses = load_expenses()
            show_summary(expenses)

        elif choice == "5":
            expenses = load_expenses()
            if not expenses:
                print("❌ No expenses to export.")
            else:
                format_choice = ask_export_format()
                if format_choice == "1":
                    export_to_csv(expenses)
                elif format_choice == "2":
                    export_to_json(expenses)
                else:
                    print("❗ Invalid format option.")

        elif choice == "6":
            expenses = load_expenses()
            if not expenses:
                print("❌ No expenses to edit.")
                continue

            display_expenses(expenses)
            selected_id = input(
                "Enter the ID of the expense to edit: \n"
            ).strip()

            matched = next(
                (e for e in expenses if e["id"].startswith(selected_id)), None
            )
            if not matched:
                print("❗ Expense not found.")
                continue

            print("Enter new values (leave empty to keep current):")
            new_amount = input(
                f"Amount [{matched['amount']}]: \n"
            ) or matched["amount"]
            new_category = input(
                f"Category [{matched['category']}]: \n"
            ) or matched["category"]
            new_notes = input(
                f"Notes [{matched['notes']}]: \n"
            ) or matched["notes"]

            try:
                matched["amount"] = float(new_amount)
                matched["category"] = new_category
                matched["notes"] = new_notes

                with open(DATA_FILE, "w") as file:
                    json.dump(expenses, file, indent=4)

                print("✅ Expense updated successfully!")
            except ValueError:
                print("❌ Invalid input. Amount must be a number.")

        elif choice == "7":
            expenses = load_expenses()
            if not expenses:
                print("❌ No expenses to delete.")
                continue

            display_expenses(expenses)
            selected_id = input(
                "Enter the ID of the expense to delete: \n"
            ).strip()

            matched = next(
                (e for e in expenses if e["id"].startswith(selected_id)), None
            )
            if not matched:
                print("❗ Expense not found.")
                continue

            print("\nAre you sure you want to delete this expense?")
            print(
                f"[{matched['id'][:8]}] {matched['date']} - "
                f"{matched['category']} - ${matched['amount']} - "
                f"{matched['notes']}"
            )
            confirm = input("Type 'yes' to confirm: \n").strip().lower()

            if confirm == "yes":
                updated_expenses = [
                    e for e in expenses if e["id"] != matched["id"]
                ]
                with open(DATA_FILE, "w") as file:
                    json.dump(updated_expenses, file, indent=4)
                print("🗑️ Expense deleted successfully.")
            else:
                print("❎ Deletion cancelled.")


if __name__ == "__main__":
    main()
