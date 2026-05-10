---
created: 2026-05-07
tags:  \[kb\]
---

# Go - Customizing Go Binaries with Build Tags

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

> [!WARNING]
> New versions of go have native support for this!

<!-- markdownlint-disable-next-line MD028 -->
> [!NOTE]
> The experiments are available via build tags, so you can build with:

as of Go 1.22 the `rangefunc` experiment is available

- see: [goexperiment package - internal/goexperiment - Go
  Packages](https://pkg.go.dev/internal/goexperiment#pkg-overview)
  - see:
    [go/src/internal/goexperiment/flags.go#L111](https://github.com/golang/go/blob/master/src/internal/goexperiment/flags.go#L111)

## Sources

- [Customizing Go Binaries with Build Tags
  (digitalocean.com)](https://www.digitalocean.com/community/tutorials/customizing-go-binaries-with-build-tags)
