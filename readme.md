# TaskTact : Todo-Manager

A compact, console-based Todo Manager built with pure Python. Manage tasks with add, view, update, complete, delete, and progress stats. Data persists in a JSON file between runs.

## Features
- Add tasks
- View tasks with status icons (⏳ pending, ✅ completed)
- Update task description
- Mark completed
- Delete task
- Statistics (total, completed, pending, progress %)
- Persistent storage using `todo_tasks.json`

## Project Structure
- `todo.py` — main program 
- `todo_tasks.json` — data file (auto-created on first save)
- `README.md` 

## Requirements
- Python 3.7+
- No external libraries (uses `json` and `os`)

## Setup
1. Create a new folder for the project.
2. Add the file `todo.py` with the provided code.
3. Ensure the folder is writable (so the JSON file can be created).

## Run
- Windows: `py todo.py` or `python todo.py`
- macOS/Linux: `python3 todo.py`

## Usage
When you run the program, you’ll see:
1.Add
2.View
3.Stats
4.Update
5.Complete
6.Delete
7.Exit
8.Reset

Extra hidden feature:
0 option - creates 3 sample tasks