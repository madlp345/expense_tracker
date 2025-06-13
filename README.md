![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# 💸 Expense Tracker CLI

Welcome to the **Expense Tracker CLI App**, a terminal-based Python application designed to help users manage personal expenses via an interactive interface. The application supports adding, viewing, editing, deleting, summarizing, and exporting expense data.

[Live App on Heroku](https://your-heroku-app-link-here) <!-- Replace this with the actual link once deployed -->

---

## 📚 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technologies](#-technologies)
- [Deployment](#-deployment)
- [How to Use](#-how-to-use)
- [File Structure](#-file-structure)
- [Testing](#-testing)
- [Bugs](#-bugs)
- [Future Features](#-future-features)
- [Credits](#-credits)
- [License](#-license)

---

## 📝 Overview

This project was developed as part of Code Institute’s Portfolio Project 3 for the Diploma in Full Stack Software Development. The CLI app allows users to log and track their expenses, providing a streamlined way to manage budgeting from the terminal.

---

## ✅ Features

- Add an expense (amount, category, notes)
- View all expenses
- Edit existing expenses
- Delete specific expenses
- View summarized monthly and category-based totals
- Export data to CSV or JSON formats
- Data persists between sessions using a JSON file

---

## 💻 Technologies

- **Python 3.10+**
- **JSON** (for data persistence)
- **datetime** & **collections** (standard libraries)
- **Heroku** (for deployment)
- **Code Institute Heroku Template** (to enable terminal-based interaction)

---

## 🚀 Deployment

This application is deployed via Heroku using Code Institute’s terminal-based deployment template.

To deploy:

1. Fork this repo and clone it to your IDE
2. Push to a new public GitHub repo
3. Create a new Heroku app
4. Connect Heroku to the GitHub repo
5. Ensure the following files are present:
    - `requirements.txt`
    - `runtime.txt`
    - `Procfile`
6. Use the CI terminal Heroku template so `input()` works correctly
7. Deploy the branch and open the app via **Heroku > Open App**

> ❗ Note: This project is **terminal-based** and will not run as a web page.

---

## ▶️ How to Use

Once deployed:

1. The app will launch and display a menu:
2. View Expense
3. Exit
4. View Summary
5. Export Expenses
6. Edit Expense
7. Delete Expense
Select an option:


2. Navigate using number inputs.

3. Example usage:
- Add an expense with amount, category, and optional notes.
- View all recorded expenses.
- Export all expenses to CSV or JSON.

---

## 📁 File Structure

```bash
expense-tracker/
│
├── controllers/
│   └── expense_controller.py
│   └── exporter.py
│
├── views/
│   └── cli.py
│
├── run.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── README.md
├── expenses.json
