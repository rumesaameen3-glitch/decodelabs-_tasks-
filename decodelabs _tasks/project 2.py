# Expense Tracker - Project 2 (Advanced Version)

expenses = []
total = 0

print("📊 Welcome to Expense Tracker")
print("Enter your expenses one by one.")
print("Type 'done' to finish.\n")

while True:
    user_input = input("Enter expense: ")

    if user_input.lower() == 'done':
        break

    try:
        expense = float(user_input)

        if expense < 0:
            print("⚠️ Expense cannot be negative!")
            continue

        expenses.append(expense)
        total += expense

        print(f"✅ Added: {expense}")
        print(f"💰 Current Total: {total}\n")

    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")

# Final Output
print("\n📌 Expense Summary")
print("----------------------")

for i, exp in enumerate(expenses, start=1):
    print(f"{i}. {exp}")

print("----------------------")
print(f"💵 Total Spent: {total}")
print("✅ Thank you for using Expense Tracker!")
