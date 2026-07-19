# Stage 3 notes (CLI-based AI)

Input: `../02-ide-stage/task_tracker.py`
Output: `test_task_tracker.py`, `README.md`, any bugfixes to `task_tracker.py`

## Bugs found and fixed

| Bug | Root cause | Fix |
|---|---|---|
| | | |

## Test coverage

- [ ] add
- [ ] list
- [ ] done
- [ ] delete
- [ ] missing/empty tasks.json
- [ ] invalid id (delete/done on a task that doesn't exist)

## Verification

Run from this stage's folder:

```bash
python3 -m pytest test_task_tracker.py -v
```

Paste the pass/fail summary here once it's run.