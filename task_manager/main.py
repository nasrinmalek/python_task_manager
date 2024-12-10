import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def list_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['task']} [{status}]")

if __name__ == "__main__":
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = int(input("Enter choice (1/2/3): "))

        if choice == 1:
            task = input("Enter the task: ")
            add_task(task)
        elif choice == 2:
            list_tasks()
        elif choice == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
