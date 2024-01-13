---
id: rw3b58bt8xjl63a8cbcaujz
title: Build Tags
desc: ''
updated: 1705160441396
created: 1705160430666
tags:
  - go
---

# Customizing Go Binaries with Build Tags

Source:

  * [Customizing Go Binaries with Build Tags (digitalocean.com)](https://www.digitalocean.com/community/tutorials/customizing-go-binaries-with-build-tags)

In your source code put this as the **first** line:

```go
// +build tag_name
```
or (to include):

```go
//go:build tools
```


alternatively (to exclude):

```go
// +build !tag_name
```

Then build with:

```bash
go build -tags tag_name
```
