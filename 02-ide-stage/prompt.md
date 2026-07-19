# Stage 2 prompt (IDE-based AI)

Input: `../01-chat-stage/spec.md`, `../01-chat-stage/schema.json`
Output: `task_tracker.py`, `tasks.json`

Open a folder containing the two input files in VS Code, open the Claude
extension panel, and paste:

```
Read spec.md and schema.json in this folder. Implement task_tracker.py
exactly per the spec: pure Python 3 stdlib, CRUD commands (add/list/done/
delete), JSON persistence in tasks.json, graceful error handling on
invalid input. Also create tasks.json pre-populated with the sample data
from the spec.
```

## Why this prompt is designed this way

- It hands the IDE AI the same files the chat AI produced, so there's no
  re-explaining the requirements and no drift between what was asked for
  and what gets built.
- Scoped to one output file, which keeps the result reviewable in the
  editor in a single pass instead of a sprawling multi-file scaffold.
- Works with any IDE assistant that can read and write files in an open
  folder — the Claude extension, Copilot Chat, Cursor, whatever's handy.