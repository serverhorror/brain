.. _kubernetes:

Kubernetes
==========

.. toctree::
   :glob:
   :titlesonly:
   :maxdepth: 1
   :caption: Contents:

   **

Kubernetes I\ *n* Docker (KI\ *n*\ D)
-------------------------------------

.. todo:: FIXME: enable mermaid

.. code-block:: text

  graph LR
    image([image]) --> |used by|container
    subgraph pod
      direction TB
      container
    end

.. todo:: FIXME: enable mermaid

.. code-block:: text

  graph LR

    subgraph deployment
      direction TB

      subgraph pod
        container
      end

    end

We can easily create a cluster using :ref:`kubernetes-kind-cluster`.


To create simple (trivial) resources you can use :command:`kubectl` directly.
For a complete example look at :ref:`kubernetes-create-simple-resource`.

*Alternative* — Install ``minikube``
------------------------------------

- Follow the instructions in `minikube start <https://minikube.sigs.k8s.io/docs/start/>`_
- Download ``minikube.exe``

  .. code-block:: powershell
     :linenos:

     New-Item -Path 'c:\' -Name 'minikube' -ItemType Directory -Force
     Invoke-WebRequest -OutFile 'c:\minikube\minikube.exe' -Uri 'https://github.com/kubernetes/minikube/releases/latest/download/minikube-windows-amd64.exe' -UseBasicParsing

- Add the executable to your path

  .. code-block:: powershell
     :linenos:

     $oldPath = [Environment]::GetEnvironmentVariable('Path', [EnvironmentVariableTarget]::User)
     if ($oldPath.Split(';') -inotcontains 'C:\minikube'){ `
       [Environment]::SetEnvironmentVariable('Path', $('C:\minikube;{0}' -f $oldPath), [EnvironmentVariableTarget]::User) `
     }

- Reload your path.
  The easiest way is to stop and start your terminal again.

  If you use VS Code do not use ``Developer: Reload Window``. You will need to close and open the full application.

  .. image:: ../../_assets/images/vscode-reload-window.png
     :alt: VS Code Reload Window Command

  The same applies to other tools like JetBrains products if you use them.

  .. code-block:: powershell
     :linenos:

     Get-Command minikube

  Output:

  .. code-block:: text
     :linenos:

     CommandType     Name                                               Version    Source
     -----------     ----                                               -------    ------
     Application     minikube.exe                                       0.0.0.0    C:\minikube\minikube.exe

Kubernetes CPU limits
---------------------

.. image:: ../../_assets/images/k8s-cpu-limits.excalidraw.svg
   :alt: Kubernetes CPU Limits

How to start a Pod
------------------

.. code-block:: bash
   :linenos:

   kubectl run nginx --image=nginx

How to delete a Pod
-------------------

.. code-block:: bash
   :linenos:

   kubectl delete pod nginx

How to get a Pod
----------------

.. code-block:: bash
   :linenos:

   kubectl get pod nginx

.. .. _kubernetes-kind-cluster:
..
.. .. _kubernetes-create-simple-resource:
