.. _kubernetes-create-simple-resource:

Kubernetes - Create a Simple Resource
=====================================

1. Running things directly

   .. warning::

      This is not the recommended way to run things in Kubernetes!

   .. code-block:: shell-session

      $ kubectl run --image gcr.io/google-containers/busybox mypod

   output::

      pod/mypod created

2. Inspect the pod

   .. code-block:: shell-session

      kubectl get pod

   output::

      NAME    READY   STATUS             RESTARTS      AGE
      mypod   0/1     CrashLoopBackOff   1 (12s ago)   16s

3. Look at "all" the things::

      kubectl get all

   output::

      NAME        READY   STATUS             RESTARTS     AGE
      pod/mypod   0/1     CrashLoopBackOff   1 (3s ago)   7s

      NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
      service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   13m
