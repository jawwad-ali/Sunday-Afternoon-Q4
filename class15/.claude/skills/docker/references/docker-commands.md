# Docker CLI Command Reference

## Container Lifecycle Commands

| Command | Description | Common Flags |
|---------|-------------|--------------|
| `docker create` | Create a container | `--name`, `-e`, `-v`, `-p` |
| `docker run` | Create and start container | `-d`, `-it`, `--rm`, `--name` |
| `docker start` | Start stopped container | `-a` (attach), `-i` (interactive) |
| `docker stop` | Stop running container | `-t` (timeout seconds) |
| `docker restart` | Restart container | `-t` (timeout) |
| `docker kill` | Kill container immediately | `-s` (signal) |
| `docker rm` | Remove container | `-f` (force), `-v` (volumes) |
| `docker pause` | Pause container | - |
| `docker unpause` | Unpause container | - |

## Container Inspection Commands

| Command | Description | Common Flags |
|---------|-------------|--------------|
| `docker ps` | List containers | `-a` (all), `-q` (quiet) |
| `docker logs` | View container logs | `-f` (follow), `--tail N` |
| `docker inspect` | Detailed info | `-f` (format) |
| `docker top` | Running processes | - |
| `docker stats` | Resource usage | `--no-stream` |
| `docker diff` | Changed files | - |
| `docker port` | Port mappings | - |

## Container Interaction Commands

| Command | Description | Common Flags |
|---------|-------------|--------------|
| `docker exec` | Run command in container | `-it`, `-d`, `-e` |
| `docker attach` | Attach to container | `--no-stdin` |
| `docker cp` | Copy files | - |
| `docker export` | Export filesystem | `-o` (output file) |

## Image Commands

| Command | Description | Common Flags |
|---------|-------------|--------------|
| `docker build` | Build image | `-t`, `-f`, `--build-arg` |
| `docker images` | List images | `-a`, `-q`, `--filter` |
| `docker pull` | Pull from registry | `--platform` |
| `docker push` | Push to registry | - |
| `docker tag` | Tag image | - |
| `docker rmi` | Remove image | `-f` (force) |
| `docker save` | Save to tar | `-o` (output) |
| `docker load` | Load from tar | `-i` (input) |
| `docker history` | Image history | `--no-trunc` |

## Network Commands

| Command | Description |
|---------|-------------|
| `docker network create` | Create network |
| `docker network ls` | List networks |
| `docker network inspect` | Network details |
| `docker network connect` | Connect container |
| `docker network disconnect` | Disconnect container |
| `docker network rm` | Remove network |

## Volume Commands

| Command | Description |
|---------|-------------|
| `docker volume create` | Create volume |
| `docker volume ls` | List volumes |
| `docker volume inspect` | Volume details |
| `docker volume rm` | Remove volume |
| `docker volume prune` | Remove unused |

## System Commands

| Command | Description |
|---------|-------------|
| `docker system df` | Disk usage |
| `docker system prune` | Remove unused data |
| `docker system info` | System information |
| `docker version` | Version info |

## Common Flag Patterns

### Port Mapping (-p)
```bash
-p 8080:80          # host:container
-p 127.0.0.1:8080:80  # specific interface
-p 8080-8090:80-90    # port range
```

### Volume Mounting (-v)
```bash
-v /host/path:/container/path      # bind mount
-v volume-name:/container/path     # named volume
-v /container/path                 # anonymous volume
-v /host/path:/container/path:ro   # read-only
```

### Environment Variables (-e)
```bash
-e VAR=value              # single variable
-e VAR                    # from host environment
--env-file .env           # from file
```

### Resource Limits
```bash
--memory="512m"           # memory limit
--cpus="1.5"              # CPU limit
--memory-swap="1g"        # swap limit
```
