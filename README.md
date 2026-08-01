# 🐳 Docker Complete Learning Guide

> A practical guide to Docker from beginner to advanced with hands-on assignments.

---

# Table of Contents

1. What is Docker?
2. Why Docker?
3. Virtual Machines vs Containers
4. Docker Architecture
5. Installing Docker
6. Docker Images
7. Docker Containers
8. Docker Registry
9. Docker Hub
10. Docker CLI
11. Dockerfile
12. Docker Build Process
13. Docker Layers
14. Multi-stage Builds
15. Docker Volumes
16. Bind Mounts
17. Docker Networks
18. Environment Variables
19. Docker Compose
20. Docker Logs
21. Docker Inspect
22. Docker Exec
23. Docker Statistics
24. Docker Best Practices
25. Docker Security
26. Docker in CI/CD
27. Docker Interview Questions
28. Assignments

---

# 1. What is Docker?

Docker is a platform that packages an application together with everything it needs to run:

- Application code
- Runtime
- Libraries
- Dependencies
- Configuration

Everything is packaged into an **Image**.

Running that image creates a **Container**.

Think of it as:

```
Image ---> Container
```

Image = Blueprint

Container = Running application

---

# 2. Why Docker?

Without Docker

```
Developer PC
Works ✔

Production
Doesn't Work ❌

Testing
Different Version ❌
```

Problems

- Different Operating Systems
- Different Libraries
- Different Runtime Versions
- Missing Dependencies

Docker solves

> "It works on my machine."

Now it works everywhere.

---

# 3. Virtual Machines vs Containers

## Virtual Machine

```
Application
Guest OS
Hypervisor
Host OS
Hardware
```

Every VM contains a complete operating system.

Pros

- Strong isolation

Cons

- Heavy
- Slow startup
- Large size

---

## Docker Container

```
Application
Libraries
Docker Engine
Host OS
Hardware
```

Containers share the host kernel.

Pros

- Lightweight
- Fast
- Small
- Easy deployment

---

# 4. Docker Architecture

```
             Docker Client

            docker build
            docker run
            docker pull

                  |

                  v

            Docker Daemon

      -------------------------

      Images
      Containers
      Networks
      Volumes

                  |

             Docker Registry
```

Main Components

Docker Client

- CLI

Docker Daemon

- Creates images
- Runs containers

Registry

Stores images.

Example:

Docker Hub

---

# 5. Installing Docker

Ubuntu

```bash
sudo apt update

sudo apt install docker.io

sudo systemctl start docker

sudo systemctl enable docker

docker --version
```

Test

```bash
docker run hello-world
```

---

# 6. Images

Image = Read-only template

Contains

- Ubuntu
- Python
- Node
- ASP.NET Runtime
- Java
- Libraries

List images

```bash
docker images
```

Pull image

```bash
docker pull nginx
```

Remove image

```bash
docker rmi nginx
```

---

# 7. Containers

Run image

```bash
docker run nginx
```

List running

```bash
docker ps
```

List all

```bash
docker ps -a
```

Stop

```bash
docker stop container_id
```

Delete

```bash
docker rm container_id
```

---

# 8. Docker Hub

Official cloud registry.

```
docker pull nginx

docker push username/app
```

---

# 9. Common Docker Commands

Show version

```bash
docker version
```

System info

```bash
docker info
```

Download image

```bash
docker pull ubuntu
```

Run container

```bash
docker run ubuntu
```

Interactive

```bash
docker run -it ubuntu bash
```

Background

```bash
docker run -d nginx
```

Expose port

```bash
docker run -p 8080:80 nginx
```

Assign name

```bash
docker run --name web nginx
```

---

# 10. Dockerfile

A Dockerfile is instructions for building an image.

Example

```Dockerfile
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","app.py"]
```

---

# Dockerfile Instructions

## FROM

Base image.

```Dockerfile
FROM ubuntu
```

---

## WORKDIR

Current directory.

```Dockerfile
WORKDIR /app
```

---

## COPY

Copies files.

```Dockerfile
COPY . .
```

---

## ADD

Like COPY but supports URLs and archives.

---

## RUN

Runs during build.

```Dockerfile
RUN apt update
```

---

## CMD

Runs when container starts.

```Dockerfile
CMD ["python","app.py"]
```

---

## ENTRYPOINT

Defines executable.

```Dockerfile
ENTRYPOINT ["dotnet","WeatherApi.dll"]
```

---

## ENV

Environment variable.

```Dockerfile
ENV ASPNETCORE_ENVIRONMENT=Production
```

---

## EXPOSE

Documents listening port.

```Dockerfile
EXPOSE 8080
```

---

# 11. Docker Build

```bash
docker build -t weather-api .
```

Meaning

```
-t

Tag

.

Current directory
```

---

# 12. Docker Layers

Each instruction creates a layer.

```
FROM

↓

COPY

↓

RUN

↓

CMD
```

Docker caches layers.

If only source code changes

Docker rebuilds only necessary layers.

---

# 13. Multi-stage Builds

Instead of

```
SDK
+
Build files
+
Source
+
Runtime

↓

Huge image
```

Use

```
Build Stage

↓

Publish

↓

Runtime Stage
```

Example

```Dockerfile
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build

WORKDIR /src

COPY . .

RUN dotnet publish -c Release -o /publish

FROM mcr.microsoft.com/dotnet/aspnet:9.0

WORKDIR /app

COPY --from=build /publish .

ENTRYPOINT ["dotnet","WeatherApi.dll"]
```

Advantages

- Smaller image
- Faster deployment
- More secure

---

# 14. Volumes

Without volume

```
Container Deleted

↓

Data Lost
```

Volume

```
Container

↓

Volume

↓

Disk
```

Create

```bash
docker volume create mydata
```

Mount

```bash
docker run -v mydata:/data ubuntu
```

---

# 15. Bind Mount

```bash
docker run -v $(pwd):/app python
```

Useful for development.

---

# 16. Networks

Types

- bridge
- host
- none

Create

```bash
docker network create backend
```

Run

```bash
docker run --network backend nginx
```

---

# 17. Environment Variables

```bash
docker run -e DB_HOST=localhost app
```

Dockerfile

```Dockerfile
ENV DB_HOST=localhost
```

---

# 18. Docker Compose

Run multiple containers.

Example

```yaml
services:

  api:

    build: .

    ports:

      - "5000:8080"

  sql:

    image: mcr.microsoft.com/mssql/server

    environment:

      ACCEPT_EULA: "Y"

      SA_PASSWORD: "Password123!"
```

Run

```bash
docker compose up
```

Stop

```bash
docker compose down
```

---

# 19. Logs

```bash
docker logs container
```

Live

```bash
docker logs -f container
```

---

# 20. Exec

Run command inside container.

```bash
docker exec -it container bash
```

---

# 21. Inspect

```bash
docker inspect container
```

Shows

- IP
- Mounts
- Ports
- Network

---

# 22. Statistics

```bash
docker stats
```

Shows

- CPU
- Memory
- Network
- Disk

---

# 23. Cleaning

Unused images

```bash
docker image prune
```

Everything unused

```bash
docker system prune
```

---

# 24. Best Practices

✅ Use official images

✅ Use multi-stage builds

✅ Keep images small

✅ Use .dockerignore

✅ Pin image versions

Instead of

```Dockerfile
FROM node:latest
```

Use

```Dockerfile
FROM node:22
```

---

# 25. Docker Security

- Don't run as root
- Scan images
- Keep images updated
- Use trusted registries
- Don't store secrets in images

---

# 26. Docker in CI/CD

Pipeline

```
Git Push

↓

GitHub Actions

↓

Build Image

↓

Run Tests

↓

Push Image

↓

Deploy
```

---

# 27. Useful Commands Cheat Sheet

```bash
docker images

docker ps

docker ps -a

docker pull nginx

docker run nginx

docker run -it ubuntu bash

docker run -d nginx

docker stop id

docker rm id

docker rmi image

docker build -t app .

docker logs app

docker exec -it app bash

docker inspect app

docker stats

docker compose up

docker compose down
```

---

# Assignment 1

Install Docker.

Tasks

- Install Docker
- Run hello-world
- Pull nginx
- Run nginx
- Open browser

---

# Assignment 2

Ubuntu Container

- Run Ubuntu
- Open Bash
- Create file
- Install curl
- Exit

---

# Assignment 3

Python App

Create

```python
print("Hello Docker")
```

Write Dockerfile.

Build image.

Run it.

---

# Assignment 4

ASP.NET API

Containerize an ASP.NET Core API.

Requirements

- Multi-stage Dockerfile
- Expose port
- Environment variables

---

# Assignment 5

Node.js

Containerize Express application.

Requirements

- Dockerfile
- Build image
- Publish port

---

# Assignment 6

Docker Compose

Run

- ASP.NET API
- SQL Server

Connect them together.

---

# Assignment 7

Volumes

Create MySQL container.

Store database using volume.

Delete container.

Verify data still exists.

---

# Assignment 8

Networks

Create

- Backend network

Run

- API
- Database

Verify communication.

---

# Assignment 9

Optimization

Given a Dockerfile

Improve

- Image size
- Build speed
- Security

---

# Assignment 10

GitHub Actions

Create workflow

Pipeline

Build Docker Image

↓

Run Tests

↓

Push Docker Hub

↓

Deploy

---

# Mini Project

Containerize an entire application.

Example

```
React

↓

ASP.NET API

↓

SQL Server

↓

Redis
```

Requirements

- Dockerfiles
- Docker Compose
- Volumes
- Networks
- Environment Variables
- Multi-stage Build

---

# Docker Interview Questions

1. What is Docker?

2. Difference between Image and Container?

3. Difference between CMD and ENTRYPOINT?

4. Difference between COPY and ADD?

5. What is a Volume?

6. Why use Multi-stage Builds?

7. Difference between Docker Compose and Docker Swarm?

8. Explain Docker Layers.

9. What is .dockerignore?

10. Explain Docker Networking.

11. What happens during docker build?

12. What happens during docker run?

13. Explain Docker Registry.

14. Why shouldn't containers run as root?

15. Explain bind mounts vs volumes.

---

# Learning Roadmap

```
Docker Basics
        │
        ▼
Images
        │
        ▼
Containers
        │
        ▼
Dockerfile
        │
        ▼
Volumes
        │
        ▼
Networks
        │
        ▼
Compose
        │
        ▼
Multi-stage Builds
        │
        ▼
Security
        │
        ▼
CI/CD
        │
        ▼
Kubernetes
```

---

# Next Step

After mastering Docker, learn:

- Kubernetes
- Helm
- Docker Swarm
- Azure Container Apps
- Azure Kubernetes Service (AKS)
- GitHub Actions
- ArgoCD
- Prometheus
- Grafana
