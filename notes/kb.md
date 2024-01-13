---
id: 1ci4swjqclg8o3om6niefpj
title: 'Knowledge Base [KB]'
desc: ''
updated: 1705160202192
created: 1665486252544
tags:
  - kb
---

## Random notes that are not yet sorted

### instruqt

* https://instruqt.com/

Looks like it could be a good way to learn new things.
The platform provides more server side functionality than e.g. [[kb.hackerrrank]] or [[kb.codewars]].

### SadServers

* https://sadservers.com/
* https://github.com/fduran/sadservers

## Customizing Go Binaries with Build Flags

#go

In your source code put this as the **first** line:

```go
// +build tag_name
```

Then build with:

```bash
go build -tags tag_name
```
