---
created: 2026-05-07
tags:
  - kb
  - k8s
  - kubernetes
  - BUG
---

# Kubernetes - Create a Simple Resource

- [ ] #BUG: CrashLoopBackOff? WTF?

1. Running things directly

    > [!WARNING]
    > This is not the recommended way to run things in Kubernetes!

    ```bash
    kubectl run --image gcr.io/google-containers/busybox mypod
    ```

    output:

    ```text
    pod/mypod created
    ```

2. Inspect the pod

    ```bash
    kubectl get pod
    ```

    output:

    ```text
    NAME    READY   STATUS             RESTARTS      AGE
    mypod   0/1     CrashLoopBackOff   1 (12s ago)   16s
    ```

3. Look at "all" the things:

   ```bash
    kubectl get all
    ```

    output:

    ```bash
    NAME        READY   STATUS             RESTARTS     AGE
    pod/mypod   0/1     CrashLoopBackOff   1 (3s ago)   7s

    NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   13m
    ```
