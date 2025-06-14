"""Module to export expense data to CSV and JSON files."""

import json
import csv
from pathlib import Path

EXPORT_FOLDER = Path("exports")
EXPORT_FOLDER.mkdir(exist_ok=True)


def export_to_csv(expenses, filename="expenses_export.csv"):
    """Export expenses to a CSV file."""
    filepath = EXPORT_FOLDER / filename
    with open(filepath, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "date", "amount", "category", "notes"]  # include 'id'
        )
        writer.writeheader()
        writer.writerows(expenses)
    print(f"✅ Exported to CSV: {filepath}")



def export_to_json(expenses, filename="expenses_export.json"):
    """Export expenses to a JSON file."""
    filepath = EXPORT_FOLDER / filename
    with open(filepath, mode='w') as file:
        json.dump(expenses, file, indent=4)
    print(
        f"✅ Expenses exported to JSON: {filepath.resolve()} "
        "successfully!"
    )
