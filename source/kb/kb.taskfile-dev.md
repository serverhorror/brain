---
title: taskfile.dev
tags:
  - kb
  - make
---

- <https://taskfile.dev/>

Might be a nice alternative to `make`

## Installation

```shell
go install github.com/go-task/task/v3/cmd/task@latest
```

### Initial Task

```yml
version: "3"

tasks:
  hello:
    cmds:
      - echo 'Hello World from Task!'
    silent: true
```
