.. _kb.go:

Go
==

General
=======

- `Learn Go with tests (quii.gitbook.io) <https://quii.gitbook.io/learn-go-with-tests/go-fundamentals/structs-methods-and-interfaces>`_
- `Air - Live reload for Go apps <https://github.com/cosmtrek/air>`_
- `Chi - Lightweight, idiomatic Go HTTP router <https://go-chi.io/>`_

Installing Tool Dependencies
----------------------------

- Create a file `tools.go`

  .. code-block:: go
     :linenos:

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

- Run the following command

  .. code-block:: text
     :linenos:

     go mod tidy
     go get -tags tools ./...
     go generate -tags tools


* see also :ref:`kb.go.build-tags`

Getting a specific dependency version
-------------------------------------

Source

- `Getting a specific dependency version (go.dev) <https://go.dev/doc/modules/managing-dependencies#getting_version>`_

  You can get a specific version of a dependency module by specifying its version in the go get command. The command updates the require directive in your go.mod file (though you can also update that manually).

  You might want to do this if:

  You want to get a specific pre-release version of a module to try out.
  You've discovered that the version you're currently requiring isn't working for you, so you want to get a version you know you can rely on.
  You want to upgrade or downgrade a module you're already requiring.
  Here are examples for using the go get command:

  To get a specific numbered version, append the module path with an @ sign followed by the version you want:

  .. code-block:: shell-session
    :linenos:

    go get example.com/theirmodule@v1.3.4

  To get the latest version, append the module path with @latest:

  .. code-block:: shell-session
    :linenos:

    go get example.com/theirmodule@latest

  The following go.mod file require directive example (see the :file:`go.mod` reference for more) illustrates how to require a specific version number:

  .. todo:: FIXME find out if go.mod lexer is available

  .. code-block:: text
    :linenos:

    # gomod
    require example.com/theirmodule v1.3.4

Discovering available updates
-----------------------------

Source:

- `Discovering available updates (go.dev) <https://go.dev/doc/modules/managing-dependencies#discovering_updates>`_

  You can check to see if there are newer versions of dependencies you're already using in your current module.
  Use the :command:`go list` command to display a list of your module's dependencies,
  along with the latest version available for that module.
  Once you've discovered available upgrades,
  you can try them out with your code to decide whether or not to upgrade to new versions.
  For more about the :command:`go list` command, see :command:`go list -m`.

  Here are a couple of examples.

  List all of the modules that are dependencies of your current module, along with the latest version available for each:

  .. code-block:: shell-session
      :linenos:

      go list -m -u all

  Display the latest version available for a specific module:

  .. code-block:: shell-session
      :linenos:

      go list -m -u example.com/theirmodule

gRPC
----

* see also :ref:`kb.grpc.required-tools`
* see also :ref:`kb.grpc-buf.build`
* see also :ref:`kb.git.using-bitbucket`
