tasks = []

while True:
    print("\n*** Main Menu ***")
    print("1. Add a New Task")
    print("2. View All Tasks")
    print("3. Remove a Task")
    print("4. Mark a Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nTask List:")
            for i, t in enumerate(tasks, start=1):
                status = "Completed" if t["completed"] else "Pending"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")

            num = int(input("Enter task number to remove: "))

            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task '{removed['task']}' removed successfully!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, t in enumerate(tasks, start=1):
                status = "Completed" if t["completed"] else "Pending"
                print(f"{i}. {t['task']} - {status}")

            num = int(input("Enter task number to mark as completed: "))

            if 1 <= num <= len(tasks):
                tasks[num - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
