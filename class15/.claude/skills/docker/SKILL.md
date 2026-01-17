---
name: Docker Operations
description: Use this skill when performing any Docker-related tasks including building images, running containers, managing containers, viewing logs, and working with Docker Compose
version: 1.0.0
---

# Docker Operations Skill

This skill provides comprehensive guidance for all Docker operations in this project.

## When to Use This Skill

Use this skill when the user requests any Docker-related operation:
- Building Docker images
- Running containers
- Managing container lifecycle (start, stop, restart, remove)
- Viewing container logs
- Working with Docker Compose
- Inspecting containers and images
- Docker cleanup operations

## Core Operations

### Building Images

```bash
# Build from Dockerfile in current directory
docker build -t <image-name>:<tag> .

# Build with specific Dockerfile
docker build -f Dockerfile.prod -t <image-name>:<tag> .

# Build with build arguments
docker build --build-arg NODE_ENV=production -t <image-name>:<tag> .
```

### Running Containers

```bash
# Run in detached mode
docker run -d --name <container-name> <image-name>

# Run with port mapping
docker run -d -p <host-port>:<container-port> <image-name>

# Run with volume mount
docker run -d -v <host-path>:<container-path> <image-name>

# Run with environment variables
docker run -d -e VAR_NAME=value <image-name>

# Run interactively
docker run -it --rm <image-name> /bin/sh
```

### Container Management

```bash
docker ps                    # List running containers
docker ps -a                 # List all containers
docker stop <container>      # Stop a container
docker start <container>     # Start a stopped container
docker restart <container>   # Restart a container
docker rm <container>        # Remove a container
docker rm -f <container>     # Force remove running container
```

### Logs and Inspection

```bash
docker logs <container>           # View logs
docker logs -f <container>        # Follow logs
docker logs --tail 100 <container> # Last 100 lines
docker inspect <container>        # Full container details
docker stats                      # Resource usage
```

### Image Management

```bash
docker images                # List images
docker pull <image>          # Pull from registry
docker push <image>          # Push to registry
docker rmi <image>           # Remove image
docker tag <src> <dest>      # Tag an image
```

## Docker Compose Operations

```bash
docker-compose up              # Start services
docker-compose up -d           # Start in detached mode
docker-compose up --build      # Rebuild and start
docker-compose down            # Stop and remove
docker-compose down -v         # Also remove volumes
docker-compose logs            # View all logs
docker-compose logs <service>  # View service logs
docker-compose ps              # List services
docker-compose exec <svc> sh   # Execute in service
```

## Cleanup Operations

```bash
docker system prune           # Remove unused data
docker system prune -a        # Remove all unused images
docker volume prune           # Remove unused volumes
docker network prune          # Remove unused networks
docker container prune        # Remove stopped containers
```

## Additional Resources

### Reference Files
- **`references/docker-commands.md`** - Complete Docker CLI reference
- **`references/docker-compose.md`** - Docker Compose configuration guide

### Examples
- **`examples/Dockerfile.example`** - Sample Dockerfile for Node.js apps
- **`examples/docker-compose.example.yml`** - Sample Docker Compose file

### Scripts
- **`scripts/docker-check.sh`** - Verify Docker installation and status

## Best Practices

1. **Always use specific tags** - Avoid using `latest` in production
2. **Use multi-stage builds** - Reduce image size
3. **Don't run as root** - Use USER directive in Dockerfile
4. **Use .dockerignore** - Exclude unnecessary files
5. **Health checks** - Add HEALTHCHECK to Dockerfiles
6. **Resource limits** - Set memory and CPU limits in production
