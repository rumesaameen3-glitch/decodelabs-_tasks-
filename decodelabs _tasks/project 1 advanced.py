import json
import os
import time

FILENAME = "tasks.json"

# Load tasks from file
if os.path.exists(FILENAME):
    with open(FILENAME, "r") as file:
        tasks = json.load(file)
else:
    tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n Your Tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    # Update Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            print("\nSelect task to update:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

            try:
                num = int(input("Enter task number: "))
                if 1 <= num <= len(tasks):
                    new_task = input("Enter new task: ")
                    tasks[num - 1] = new_task
                    print("Task updated!")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nSelect task to delete:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

            try:
                num = int(input("Enter task number: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Task '{removed}' deleted!")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number")

    # Exit
    elif choice == "5":
        # Save tasks
        with open(FILENAME, "w") as file:
            json.dump(tasks, file, indent=4)

        print("\nTasks saved successfully!")
        time.sleep(2)  # pause so user can see message
        print("Program closed.")
        break

    else:
        print("Invalid choice, try again.")
