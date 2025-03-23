.. _kb.go.build-tags:

Go - Customizing Go Binaries with Build Tags
--------------------------------------------

Source:

- `Customizing Go Binaries with Build Tags (digitalocean.com) <https://www.digitalocean.com/community/tutorials/customizing-go-binaries-with-build-tags>`_

In your source code put this as the **first** line:

.. code-block:: go
  :linenos:

  // +build tag_name

or (to include):

.. code-block:: go
  :linenos:

  //go:build tag_name

alternatively (to exclude):

.. code-block:: go
  :linenos:

  // +build !tag_name

Then build with:

.. code-block:: bash
  :linenos:

  go build -tags tag_name

## Go experiments

.. note::

  The experiments are available via build tags, so you can build with:

as of Go 1.22 the `rangefunc` experiment is available

- see: `goexperiment package - internal/goexperiment - Go Packages <https://pkg.go.dev/internal/goexperiment#pkg-overview>`_
  - see: `go/src/internal/goexperiment/flags.go#L111 <https://github.com/golang/go/blob/master/src/internal/goexperiment/flags.go#L111>`_
