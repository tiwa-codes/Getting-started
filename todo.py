import json
import os

todo_file = "todo.json"

def display_tasks():
    if os.path.exists(todo_file):
        with open(todo_file) as f:
            tasks = json.load(f)
            if tasks:
                print("To-Do List:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
            else:
                print("No tasks found.")
    else:
        print("No to-do list found.")

def add_task(task):
    if os.path.exists(todo_file):
        with open(todo_file) as f:
            tasks = json.load(f)
    else:
        tasks = []
    
    tasks.append(task)

    with open(todo_file, "w") as f:
        json.dump(tasks, f)

def delete_task(task_index):
    if os.path.exists(todo_file):
        with open(todo_file) as f:
            tasks = json.load(f)
            if task_index <= len(tasks):
                del tasks[task_index - 1]
                with open(todo_file, "w") as f:
                    json.dump(tasks, f)
                print("Task deleted successfully.")
            else:
                print("Invalid task index.")
    else:
        print("No to-do list found.")

def main():
    while True:
        print("To-Do List Application")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks()
        elif choice == "2":
            task = input("Enter the task: ")
            add_task(task)
            print("Task added successfully.")
        elif choice == "3":
            task_index = int(input("Enter the task index to delete: "))
            delete_task(task_index)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()