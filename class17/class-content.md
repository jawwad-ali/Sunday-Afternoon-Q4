# Kubernetes

## Why Kubernetes?

Kubernetes is a system that manages **scaling**, **healing**, and **load balancing** across containers.

### The Problem

When users use an application, load goes to the container. The container uses machine resources.

| Local Machine | Cloud Providers |
|---------------|-----------------|
| 8GB RAM → 16GB → 32GB | AWS, Azure, Google Cloud |

Scaling locally has limits. Cloud providers with Kubernetes solve this.

---

## What are Pods?

- Containers live inside **Pods** in Kubernetes (K8s)
- **99% of the time**, there is only **one container in a Pod**

---

## What is Kubectl?

- `kubectl` is a **command-line interface (CLI)** tool for Kubernetes
- Used to interact with and manage K8s clusters

---

## Kubernetes Architecture Overview

```
1. Python Image
   │
   └── 2. Container
       │
       └── 3. Pod
           ├── 3.1 kubelet (takes instructions from K8s)
           └── 3.2 containerd (Container engine)
```

### Components Explained

| Component | Description |
|-----------|-------------|
| **Image** | Blueprint for creating containers (e.g., Python image) |
| **Container** | Running instance of an image |
| **Pod** | Smallest deployable unit in K8s; wraps container(s) |
| **kubelet** | Agent that runs on each node; receives instructions from K8s control plane |
| **containerd** | Container runtime/engine that manages container lifecycle |
