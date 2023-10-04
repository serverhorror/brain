---
id: pmj92td2iut7phh7kper0cy
title: taskfile.dev
desc: ''
updated: 1696454972539
created: 1664021167735
tags:
  - kb
  - make
---


* <https://taskfile.dev/>

Might be a nice alternative to `make`

## Installation

```
go install github.com/go-task/task/v3/cmd/task@latest
```

### Initial Task

```yml
version: '3'

tasks:
  hello:
    cmds:
      - echo 'Hello World from Task!'
    silent: true
```
