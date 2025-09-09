# Command-Line To-Do List Manager

A simple command-line to-do list manager written in Python. This tool allows you to add, remove, and list tasks, with all tasks stored in a plain text file.

## Features

- **Add tasks** to your to-do list.
- **Remove tasks** by their number.
- **List all current tasks**.
- Tasks are saved persistently in a `todo.txt` file.

## Usage

```sh
python todo.py list
python todo.py add <task>
python todo.py remove <task_number>
```

### Examples

- List all tasks:
  ```sh
  python todo.py list
  ```
- Add a new task:
  ```sh
  python todo.py add Buy groceries
  ```
- Remove the second task:
  ```sh
  python todo.py remove 2
  ```

## Requirements

- Python 3.x

## Notes

- All tasks are saved in `todo.txt` in the current directory.
- Removing a task requires its task number, as shown in the list.

## License

MIT License
