# Stage 1 prompt (chat-based AI)

Paste this into any chat-based AI tool (ChatGPT, Gemini Chat, Claude.ai,
etc.). It asks for a spec and a schema, not code — the output needs to
work as a build contract for stage 2, no matter which chat tool wrote it.

```
I need a spec for a small CLI task tracker called TaskFlow. Cover:

1. Commands the CLI supports (add/list/done/delete or similar), what each
   does, and how data persists between runs.
2. A data model for a single task: fields, types, and a JSON Schema for it.
3. Non-functional requirements: language/runtime, dependency constraints,
   error handling expectations.
4. Sample data I can use to test with.
5. A short checklist of acceptance criteria.

Output as Markdown with headings, plus the JSON Schema as a separate fenced
code block. Don't write any implementation code — just the spec.
```

## Why this prompt is designed this way

- It asks for content and structure, not implementation. The schema and
  acceptance criteria are the contract; the Python is left to whichever
  tool actually has somewhere to run it.
- The constraints ("standard library only", "single file") are spelled
  out up front so the next stage isn't handed a spec it can't finish in
  the time available.
- Nothing here assumes a specific chat product — any tool that can follow
  instructions and write Markdown works.