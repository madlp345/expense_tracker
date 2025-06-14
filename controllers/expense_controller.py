"""Handles loading, saving, and creating expense data in JSON format."""

import json
from datetime import datetime
from pathlib import Path
import uuid

DATA_FILE = Path("data/expenses.json")


def load_expenses():
    """Load expenses from the JSON file."""
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []


def save_expense(expense):
    """Save expenses to the JSON file."""
    expenses = load_expenses()
    expenses.append(expense)
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def create_expense(amount, category, notes):
    """Create a new expense entry."""
    return {
        "id": str(uuid.uuid4()),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "amount": float(amount),
        "category": category,
        "notes": notes
    }
