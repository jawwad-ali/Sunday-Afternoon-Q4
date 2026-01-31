# Getting Started with Kubernetes/k8s

## Pods (Apartment inside the building)
- 


## Nodes (Building for the Pods)
-

## Clusters (Society - Lots of Buildings)
-



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
- minikube status
- minikube dashboard
