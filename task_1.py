def display_menu():
    print("\n" + "=" * 30)
    print("     TO-DO LIST     ")
    print("=" * 30)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Exit")
    print("=" * 30)


def view_tasks(task_list):
    print("\n--- Current Tasks ---")
    if not task_list:
        print("Your to-do list is empty! Add a task to get started.")
    else:
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")


def add_task(task_list):
    print("\n--- Add a New Task ---")
    new_task = input("Enter the task description: ").strip()
    
    # Validation to prevent adding empty strings
    if new_task:
        task_list.append(new_task)
        print(f"Success: '{new_task}' has been added to your list.")
    else:
        print("Error: Task description cannot be blank.")


def main():
    todo_list = []
    
    while True:
        display_menu()
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            view_tasks(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            print("\nThank you for using the To-Do List application. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()