import json

# Load existing tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(task, category, priority):
    tasks.append({"task": task, "category": category, "priority": priority, "completed": False})
    save_tasks(tasks)
    print(f"Added task: '{task}' under '{category}' with priority '{priority}'.")

# View all tasks
def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['task']} | Category: {task['category']} | Priority: {task['priority']} | Status: {status}")

# Mark a task as complete
def complete_task(index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[index - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number!")

# Edit a task
def edit_task(index, new_task):
    if 0 < index <= len(tasks):
        tasks[index - 1]["task"] = new_task
        save_tasks(tasks)
        print(f"Task updated to: '{new_task}'")
    else:
        print("Invalid task number!")

# Delete a task
def delete_task(index):
    if 0 < index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted task: '{removed_task['task']}'")
    else:
        print("Invalid task number!")

# Load tasks at startup
tasks = load_tasks()

# Main loop
while True:
    print("\nOptions: 1. Add | 2. View | 3. Complete | 4. Edit | 5. Delete | 6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        category = input("Enter category (Work/Personal/Others): ")
        priority = input("Set priority (High/Medium/Low): ")
        add_task(task, category, priority)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        index = int(input("Enter task number to complete: "))
        complete_task(index)
    elif choice == "4":
        view_tasks()
        index = int(input("Enter task number to edit: "))
        new_task = input("Enter new task description: ")
        edit_task(index, new_task)
    elif choice == "5":
        view_tasks()
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == "6":
        print("Exiting To-Do List...")
        break
    else:
        print("Invalid choice! Please enter a valid option.")
