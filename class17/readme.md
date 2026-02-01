# Getting Started with Kubernetes/k8s

## Pods (Apartment inside the building)
- A Pod is the smallest unit in Kubernetes that wraps one or more containers.
- Kubernetes doesn't talk to containers directly, it manages Pods instead.

## Nodes (Building for the Pods)
- A Node is a physical or virtual machine where Pods actually run.
- There are two types: Master Node (decides where Pods go) and Worker Node (runs the Pods).

## Clusters (Society - Lots of Buildings)
- A Cluster is a group of Nodes working together as one system.
- It has one Master Node (manager) and multiple Worker Nodes (actual buildings where Pods live).


# Installation

**NOTE**: Docker Desktop should be enabled in the background <br />

## Kubectl
- **Command**: `winget install Kubernetes.kubectl`
- **verify Installation**: `kubectl version --client`

## MiniKube
- **Command**: `winget install Kubernetes.minikube`
- **verify installtion**: `minikube version`

## Create Kubernetes cluster inside a Docker
- This command creates and starts a local Kubernetes cluster inside a Docker container.

**Command:** `minikube start --driver=docker`

- NOTE: This process will take time

#### Run commands after the Installtion
- `minikube status`
- vminikube dashboard`

NOTE: Incase the Installation fails run these commands and try again
- `minikube delete`
- `docker rm -f minikube-preload-sidecar`
- `docker rm -f minikube`
- `docker system prune -f` (**This will remove everything in from your docker**)
-  `docker volume rm minikube` 
- `minikube start --driver=docker`

## Lets Create your First Pod
- `kubectl run my-first-pod --image=python --command -- sleep 3600`

| Part | Meaning |
|------|---------|
| `--command` | Custom command run karo |
| `--` | Yahan se container ka command shuru |
| `sleep 3600` | Container ko 1 hour tak alive rakho |
