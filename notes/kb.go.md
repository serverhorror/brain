---
id: bc8gb1blxcy1kg2thjhh67q
title: Go
desc: ''
updated: 1705160955960
created: 1664020967164
tags:
  - kb
  - go
  - grpc
---


## General

* [Learn Go with tests (quii.gitbook.io)](https://quii.gitbook.io/learn-go-with-tests/go-fundamentals/structs-methods-and-interfaces)
* [☁️ Air - Live reload for Go apps](https://github.com/cosmtrek/air)
* [chi](https://go-chi.io/)

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

![[kb.go.build-tags]]

## Discovering available updates

Source:

  * [Discovering available updates (go.dev)](https://go.dev/doc/modules/managing-dependencies#discovering_updates)

> You can check to see if there are newer versions of dependencies you’re already using in your current module. Use the go list command to display a list of your module’s dependencies, along with the latest version available for that module. Once you’ve discovered available upgrades, you can try them out with your code to decide whether or not to upgrade to new versions.
> 
> For more about the go list command, see go list -m.
> 
> Here are a couple of examples.
> 
> List all of the modules that are dependencies of your current module, along with the latest version available for each:
> 
> ```shell-session
> $ go list -m -u all
> ```
>
> Display the latest version available for a specific module:
> 
> ```shell-session
> $ go list -m -u example.com/theirmodule
> ```
>

## gRPC

![[kb.grpc#required-tools]]

## buf

![[buf.build|kb.grpc#bufbuild]]

## Bitbucket

![[kb.git#using-bitbucket-serverdatacenter-git]]
