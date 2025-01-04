# Kubernetes - Create a Simple Resource

1. Running things directly

   !!WARN: This is not the recommended way to run things in Kubernetes!!

   ```text
   kubectl run --image gcr.io/google-containers/busybox mypod
   ```

   output

   ```text
   pod/mypod created
   ```

2. Inspect the pod

   ```text
   kubectl get pod
   ```

   output

   ```text
   NAME    READY   STATUS             RESTARTS      AGE
   mypod   0/1     CrashLoopBackOff   1 (12s ago)   16s
   ```

3. Look at "all" the things

   ```text
   kubectl get all
   ```

   output

   ```text
   NAME        READY   STATUS             RESTARTS     AGE
   pod/mypod   0/1     CrashLoopBackOff   1 (3s ago)   7s

   NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
   service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   13m
   ```
