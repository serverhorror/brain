---
created: 2026-05-07
tags:
  - kb
---

# taskfile.dev

- [taskfile.dev](https://taskfile.dev/)

Might be a nice alternative to `make`.

## Installation

```bash
go install github.com/go-task/task/v3/cmd/task@latest
```

## Initial Task

```yaml
version: "3"

tasks:
  hello:
   cmds:
    - echo 'Hello World from Task!'
   silent: true
```
