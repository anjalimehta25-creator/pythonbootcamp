total_task = []

while True:

    print("\nList of Homework")
    print("Enter 1 for add task")
    print("Enter 2 for delete task")
    print("Enter 3 for remove the last task")
    print("Enter 4 for sort the tasks")
    print("Enter 5 for print the tasks")
    print("Enter 6 for exit the task")

    user_input = int(input("Choose input between 1 to 6: "))

    if user_input == 1:

        task = input("Enter a task: ")
        total_task.append(task)
        print(total_task)

    elif user_input == 2:

        task = input("Enter task to delete: ")

        if task in total_task:
            total_task.remove(task)
            print(total_task)
        else:
            print("Invalid task")

    elif user_input == 3:

        if total_task:
            total_task.pop()
            print(total_task)
        else:
            print("Tasks are empty")

    elif user_input == 4:

        total_task.sort()
        print(total_task)

    elif user_input == 5:

        if total_task:
            print(total_task)
        else:
            print("No task available")

    elif user_input == 6:

        print("Exit the app")
        break

    else:
        print("Invalid choice. Choose between 1 and 6.")