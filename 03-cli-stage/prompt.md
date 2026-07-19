# Stage 3 prompt (CLI-based AI)

Input: `../02-ide-stage/task_tracker.py`
Output: `test_task_tracker.py`, fixed `task_tracker.py` (if needed), `README.md`

`cd` into the folder holding `task_tracker.py`, start a Claude Code
session, and paste:

```
Write pytest tests for task_tracker.py covering add/list/done/delete and
the missing-tasks.json case. Run them, fix any bugs you find, then write
a short README.md explaining usage.
```

## Why this prompt is designed this way

- It asks the CLI AI to do the one thing only it can: actually execute
  the code and react to real failures, instead of describing what should
  happen.
- "Fix any bugs you find" closes the loop — this stage doesn't just check
  stage 2's work, it repairs it, which is where the workflow actually
  saves someone time instead of just moving the work around.
- Works with Claude Code, Aider, Gemini CLI, or anything else with shell
  and file access — nothing in the prompt names a vendor.