# Agent Rules

Rules any AI agent must follow when working on this project.

---

## 1. Commits

Never commit unless explicitly asked to.

When asked, follow the [Conventional Commits](https://www.conventionalcommits.org/) pattern:

```
<type>(<optional scope>): <description>
```

Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `build`.

**A commit message is one line — the subject. No body.** If the change can't be honestly described in a single line, the commit is doing too much: split the work into several commits, each one focused enough to fit on its own line.

```bash
# Good — two focused commits
feat(query): add retrieval step to /query endpoint
docs(readme): document the retrieval configuration

# Bad — one commit that needs a body to explain itself
feat: add retrieval and update docs and fix env loading
```

## 2. Keep the README in sync

Whenever a change affects **how the project is installed, configured, or run**, update [README.md](README.md) in the same task — not later. This includes:

- new or changed dependencies, or a different Python/`uv` requirement
- new environment variables (also add them to [.env.example](.env.example))
- changes to the run command or the entrypoint declared in [pyproject.toml](pyproject.toml)
- new, renamed, or removed endpoints

If a change doesn't touch any of the above, leave the README alone.

## 3. Plan and build with superpowers skills

Always invoke the relevant `superpowers` skill before writing code — process skills first, implementation skills second:

- `superpowers:brainstorming` — before any new feature or behaviour change
- `superpowers:writing-plans` — to turn requirements into a written plan
- `superpowers:test-driven-development` — before writing implementation code
- `superpowers:systematic-debugging` — before proposing a fix for any bug or test failure
- `superpowers:dispatching-parallel-agents` — when the plan has 2+ independent tasks, dispatch them as parallel subagents

Skills are not optional. If there's even a small chance one applies, invoke it and decide afterwards.

## 4. Review every finished task

Before reporting a task as done, dispatch a **reviewer subagent** to review the work against the original request.

Use `superpowers:requesting-code-review`, and handle the result with `superpowers:receiving-code-review` — verify each point technically instead of agreeing by default. Fix what's genuinely wrong, and state plainly what you chose not to change and why.

A task is only complete once the review has run and its findings have been addressed.
