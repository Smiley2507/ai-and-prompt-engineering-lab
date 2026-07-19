#!/usr/bin/env python3
"""TaskFlow — a simple CLI task tracker.

Pure Python 3 standard library. Tasks are persisted as a JSON array in
``tasks.json`` in the current working directory.

Usage:
    python task_tracker.py add "<title>"
    python task_tracker.py list
    python task_tracker.py done <id>
    python task_tracker.py delete <id>
"""

import json
import sys
from datetime import datetime

DATA_FILE = "tasks.json"
VALID_STATUSES = ("pending", "done")


def load_tasks():
    """Return the list of tasks, tolerating a missing or empty data file."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as fh:
            content = fh.read().strip()
            if not content:
                return []
            data = json.loads(content)
    except FileNotFoundError:
        return []
    except (json.JSONDecodeError, OSError) as exc:
        fail("could not read {}: {}".format(DATA_FILE, exc))

    if not isinstance(data, list):
        fail("{} is corrupt: expected a JSON array".format(DATA_FILE))
    return data


def save_tasks(tasks):
    """Persist the task list to disk."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as fh:
            json.dump(tasks, fh, indent=2)
            fh.write("\n")
    except OSError as exc:
        fail("could not write {}: {}".format(DATA_FILE, exc))


def fail(message):
    """Print a clean error message (no stack trace) and exit non-zero."""
    print("error: {}".format(message), file=sys.stderr)
    sys.exit(1)


def next_id(tasks):
    """Auto-increment: one past the highest existing id, or 1 if empty."""
    return max((task.get("id", 0) for task in tasks), default=0) + 1


def parse_id(raw):
    """Parse a CLI-supplied id, failing gracefully on non-integers."""
    try:
        return int(raw)
    except (TypeError, ValueError):
        fail("'{}' is not a valid task id".format(raw))


def cmd_add(args):
    if len(args) != 1 or not args[0].strip():
        fail('add requires a non-empty title, e.g. add "Write lab report"')
    tasks = load_tasks()
    task = {
        "id": next_id(tasks),
        "title": args[0],
        "status": "pending",
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    tasks.append(task)
    save_tasks(tasks)
    print("added task {}".format(task["id"]))


def cmd_list(args):
    if args:
        fail("list takes no arguments")
    tasks = load_tasks()
    if not tasks:
        print("no tasks yet")
        return
    for task in tasks:
        mark = "x" if task.get("status") == "done" else " "
        print("[{}] {:>3}  {}".format(mark, task.get("id", "?"), task.get("title", "")))


def cmd_done(args):
    if len(args) != 1:
        fail("done requires a task id, e.g. done 1")
    task_id = parse_id(args[0])
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["status"] = "done"
            save_tasks(tasks)
            print("task {} marked done".format(task_id))
            return
    fail("no task with id {}".format(task_id))


def cmd_delete(args):
    if len(args) != 1:
        fail("delete requires a task id, e.g. delete 1")
    task_id = parse_id(args[0])
    tasks = load_tasks()
    remaining = [task for task in tasks if task.get("id") != task_id]
    if len(remaining) == len(tasks):
        fail("no task with id {}".format(task_id))
    save_tasks(remaining)
    print("task {} deleted".format(task_id))


COMMANDS = {
    "add": cmd_add,
    "list": cmd_list,
    "done": cmd_done,
    "delete": cmd_delete,
}


def main(argv):
    if not argv:
        fail("no command given; use one of: {}".format(", ".join(COMMANDS)))
    command, args = argv[0], argv[1:]
    handler = COMMANDS.get(command)
    if handler is None:
        fail("unknown command '{}'; use one of: {}".format(command, ", ".join(COMMANDS)))
    handler(args)


if __name__ == "__main__":
    main(sys.argv[1:])
