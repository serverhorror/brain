---
id: rw3b58bt8xjl63a8cbcaujz
title: Customizing Go Binaries with Build Tags
desc: ''
updated: 1716159280881
created: 1705160430666
tags:
  - go
---

Source:

  * [Customizing Go Binaries with Build Tags (digitalocean.com)](https://www.digitalocean.com/community/tutorials/customizing-go-binaries-with-build-tags)

In your source code put this as the **first** line:

```go
// +build tag_name
```
or (to include):

```go
//go:build tag_name
```


alternatively (to exclude):

```go
// +build !tag_name
```

Then build with:

```bash
go build -tags tag_name
```

## Go experiments

**NOTE** The experiments are available via build tags, so you can build with:

as of Go 1.22 the `rangefunc` experiment is available


```go
//go:build goexperiment.rangefunc

package example
```

```bash
GOEXPERIMENT=rangefunc go build
```
