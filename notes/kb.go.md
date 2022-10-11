---
id: ck6zlerrtdccv0fxnko3qxn
title: Go
desc: ''
updated: 1665485881915
created: 1664020967164
tags:
  - kb
  - go
  - grpc
---


## General

### Installing Tool Dependencies

* Create a file `tools.go`

  ```go
  // This comment is here so that the "normal" build process ignores it.
  // To install these dependencies run:
  //
  // `go get -tags tools .`
  //
  // or simply
  //
  // `go mod tidy`

  //go:build tools


  // This allows us to have a "self contained" codebase,
  // there are not (a lot of) external tools required for this to work.

  //go:generate go install "google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest"
  //go:generate go install "google.golang.org/protobuf/cmd/protoc-gen-go@latest"

  package main

  import (
    _ "google.golang.org/grpc/cmd/protoc-gen-go-grpc"
    _ "google.golang.org/protobuf/cmd/protoc-gen-go"
  )
  ```

* Run the following command

  ```text
  go mod tidy
  go get -tags tools ./...
  go generate -tags tools
  ```

## gRPC

### Required Tools

* Download the `protoc` compiler from

  <https://github.com/protocolbuffers/protobuf/releases>

* extract to `$env:USERPROFILE/sdk`
* add `$env:USERPROFILE/sdk/<protoc-directory>/bin` to your path

#### buf

![[buf.build|kb.grpc#bufbuild]]
