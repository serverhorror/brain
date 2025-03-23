.. _kubernetes-kind-cluster:

Kubernetes - Create KiND Cluster
================================

1. Get started

   ```text
   kind create cluster
   ```

   output

   ```text
   Creating cluster "kind" ...
   ✓ Ensuring node image (kindest/node:v1.25.0) 🖼
   ✓ Preparing nodes 📦
   ✓ Writing configuration 📜
   ✓ Starting control-plane 🕹️
   ✓ Installing CNI 🔌
   ✓ Installing StorageClass 💾
   Set kubectl context to "kind-kind"
   You can now use your cluster with:

   kubectl cluster-info --context kind-kind

   Have a nice day! 👋
   ```

1. standard `kubectl` commands

   ````text

   ```text
   kubectl cluster-info --context kind-kind
   ````

   output

   ```text
   Kubernetes control plane is running at https://127.0.0.1:56236
   CoreDNS is running at https://127.0.0.1:56236/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

   To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
   ```

   And taking a look at the context

   ```text
   kubectl config current-context
   ```

   output

   ```text
   kind-kind
   ```
