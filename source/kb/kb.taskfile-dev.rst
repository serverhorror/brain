.. _kb.taskfile-dev:

taskfile.dev
============

- `taskfile.dev <https://taskfile.dev/>`_

Might be a nice alternative to :program:`make`

Installation
------------

.. code-block:: shell
  :linenos:

  go install github.com/go-task/task/v3/cmd/task@latest

Initial Task
------------

.. code-block:: yaml
  :linenos:

  version: "3"

  tasks:
    hello:
     cmds:
      - echo 'Hello World from Task!'
     silent: true
