---
created: 2026-05-07
tags:
  - kb
  - k8s
  - kubernetes
---

# Kubernetes - Create KiND Cluster

1. Get started

    ```bash
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

    ```bash
    kubectl cluster-info --context kind-kind
    ```

    output

    ```text
    Kubernetes control plane is running at https://127.0.0.1:56236
    CoreDNS is running at https://127.0.0.1:56236/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

    To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
    ```

    ```bash
    kubectl config current-context
    ```

    ```text
    kind-kind
    ```
