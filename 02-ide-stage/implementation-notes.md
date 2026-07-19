# Stage 2 notes (IDE-based AI)

Input: `../01-chat-stage/spec.md`, `../01-chat-stage/schema.json`
Output: `task_tracker.py`, `tasks.json`

The spec leaves a few things open on purpose — exact error wording, how
ids get assigned, how `list` formats output. Once you've run the IDE
stage, jot down what it decided and why, the same way you'd leave a note
in a code review.

## Judgment calls made

| Spec said | Implementation decision | Why |
|---|---|---|
| "auto-incremented id" | | |
| "graceful error on invalid input" | | |
| | | |

## Deviations from a literal reading

- (anything the IDE AI added or changed beyond the spec, and whether you
  kept it)

## Verification

- [ ] Code runs without syntax errors
- [ ] Ran each command once by hand and it behaved as expected