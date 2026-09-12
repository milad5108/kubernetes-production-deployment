# Architecture

## Overview

This project runs a FastAPI application on Kubernetes using Minikube.

The main request flow is:

```text
Client
  |
  v
NGINX Ingress
  |
  v
Kubernetes Service
  |
  v
Kubernetes Deployment
  |
  v
Application Pods