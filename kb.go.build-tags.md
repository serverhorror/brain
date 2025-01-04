---
title: Customizing Go Binaries with Build Tags
tags:
  - go
---

Source:

- [Customizing Go Binaries with Build Tags (digitalocean.com)](https://www.digitalocean.com/community/tutorials/customizing-go-binaries-with-build-tags)

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

- see: [goexperiment package - internal/goexperiment - Go Packages](https://pkg.go.dev/internal/goexperiment#pkg-overview)
  - see: [go/src/interna/goexperiment/flags.go#L111](https://github.com/golang/go/blob/master/src/internal/goexperiment/flags.go#L111)

```go
//go:build goexperiment.rangefunc

package example
```

```bash
GOEXPERIMENT=rangefunc go build
```
