tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(i + 1, "-", tasks[i])

    elif choice == "3":
        print("Program ended")
        break

    else:
        print("Invalid choice")

