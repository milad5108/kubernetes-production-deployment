# Kubernetes Production Deployment

A production-style Kubernetes deployment project built to demonstrate practical Kubernetes skills including application deployment, service networking, ingress routing, configuration management, health checks, rolling updates, rollback, and horizontal pod autoscaling.

This project is part of a DevOps portfolio focused on Junior DevOps Engineer, Remote, and International opportunities.

---

## Project Overview

This repository deploys a FastAPI application to Kubernetes using Minikube.

The project includes:

- Kubernetes Deployment
- ClusterIP Service
- NGINX Ingress
- ConfigMap
- Kubernetes Secret
- Readiness Probe
- Liveness Probe
- Rolling Update
- Rollback
- Horizontal Pod Autoscaler
- CPU and Memory Requests/Limits
- Metrics Server integration
- Load-based Scaling Validation

---

## Application

The application is a lightweight FastAPI service.

Current application version:

```text
v1.1

---

# Screenshots

## Kubernetes Resources

![Kubernetes Resources](screenshots/01-kubernetes-resources.png)

---

## Ingress Validation

![Ingress Validation](screenshots/02-ingress-validation.png)

---

## HPA Scale Up

![HPA Scale Up](screenshots/03-hpa-scale-up.png)

---

## HPA Scale Down

![HPA Scale Down](screenshots/04-hpa-scale-down.png)

---

## Metrics Server

![Metrics Server](screenshots/05-metrics-server.png)