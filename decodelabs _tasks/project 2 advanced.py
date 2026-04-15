import json
import os

FILE_NAME = "expenses.json"

# Load data from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file)

# Add expense
def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        if amount < 0:
            print("⚠️ Expense cannot be negative!")
            return
        expenses.append(amount)
        save_expenses(expenses)
        print("✅ Expense added successfully!")
    except ValueError:
        print("❌ Invalid input!")

# View all expenses
def view_expenses(expenses):
    if not expenses:
        print("📭 No expenses found!")
        return
    
    print("\n📊 All Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp}")

# Show summary
def show_summary(expenses):
    if not expenses:
        print("📭 No expenses to calculate!")
        return
    
    total = sum(expenses)
    avg = total / len(expenses)

    print("\n📈 Summary:")
    print(f"💰 Total Spent: {total}")
    print(f"📊 Average Expense: {avg:.2f}")

# Clear all data
def clear_expenses():
    confirm = input("Are you sure? (yes/no): ")
    if confirm.lower() == "yes":
        save_expenses([])
        print("🗑️ All expenses cleared!")
    else:
        print("❌ Operation cancelled!")

# Main Program
def main():
    expenses = load_expenses()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Clear All Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            clear_expenses()
            expenses = []
        elif choice == "5":
            print("👋 Exiting... Data saved!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
