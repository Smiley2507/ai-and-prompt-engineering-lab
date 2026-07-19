# TaskFlow

A tiny CLI task tracker. Pure Python 3 standard library, no dependencies.
Tasks are stored as a JSON array in `tasks.json` in the current directory.

## Usage

```
python3 task_tracker.py add "<title>"   # add a new task
python3 task_tracker.py list            # list all tasks
python3 task_tracker.py done <id>       # mark a task done
python3 task_tracker.py delete <id>     # delete a task
```

`tasks.json` is created automatically on the first `add`; if it's missing,
`list` just reports "no tasks yet".

## Tests

```
pytest test_task_tracker.py
```
