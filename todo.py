import sys
import os

TODO_FILE = "todo.txt"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        tasks = [line.strip() for line in f if line.strip()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")

def remove_task(index):
    tasks = load_tasks()
    try:
        idx = int(index) - 1
        removed = tasks.pop(idx)
        save_tasks(tasks)
        print(f"Removed task: {removed}")
    except (IndexError, ValueError):
        print("Invalid task number.")

def print_usage():
    print("Usage:")
    print("  python todo.py list")
    print("  python todo.py add <task>")
    print("  python todo.py remove <task_number>")

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]
    if command == "list":
        list_tasks()
    elif command == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif command == "remove" and len(sys.argv) == 3:
        remove_task(sys.argv[2])
    else:
        print_usage()

if __name__ == "__main__":
    main()
