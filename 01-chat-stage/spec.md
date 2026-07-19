# TaskFlow — CLI Task Tracker Spec (Stage 1 output: Chat AI)

## Purpose
A simple command-line task tracker, stored as a local JSON file. This spec is the
handoff artifact from the chat stage to the IDE stage of the workflow.

## Commands
- `add "<title>"` — create a new task, status defaults to "pending"
- `list` — print all tasks with id, status, title
- `done <id>` — mark a task as "done"
- `delete <id>` — remove a task
- Data persists in `tasks.json` in the working directory

## Data model (see schema.json)
Each task:
- `id`: integer, auto-incremented
- `title`: string, required
- `status`: string, one of "pending" | "done"
- `created_at`: ISO 8601 timestamp string

## Non-functional requirements
- Pure Python 3, standard library only (no external deps)
- Single file: `task_tracker.py`
- Must handle a missing/empty `tasks.json` gracefully (start with empty list)
- Exit with a clear error message (not a stack trace) on invalid input, e.g.
  `delete 999` when no task 999 exists

## Sample data (for testing)
```json
[
  {"id": 1, "title": "Write lab report", "status": "pending", "created_at": "2026-07-19T09:00:00"},
  {"id": 2, "title": "Buy groceries", "status": "done", "created_at": "2026-07-18T14:30:00"}
]
```

## Acceptance criteria
- [ ] `python task_tracker.py add "Test task"` creates a task and prints its id
- [ ] `python task_tracker.py list` shows all tasks, done ones visually marked
- [ ] `python task_tracker.py done 1` flips status to done
- [ ] `python task_tracker.py delete 1` removes the task
- [ ] Re-running `list` after restart still shows prior tasks (persistence works)