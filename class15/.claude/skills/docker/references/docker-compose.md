# Docker Compose Reference

## File Structure

Docker Compose uses YAML files (typically `docker-compose.yml` or `compose.yml`).

## Version and Services

```yaml
version: "3.9"  # Optional in newer versions

services:
  service-name:
    # Service configuration
```

## Service Configuration Options

### Image and Build

```yaml
services:
  app:
    # Use existing image
    image: node:20-alpine

    # Or build from Dockerfile
    build:
      context: .
      dockerfile: Dockerfile
      args:
        NODE_ENV: production
      target: production  # Multi-stage target
```

### Ports

```yaml
services:
  web:
    ports:
      - "3000:3000"           # host:container
      - "127.0.0.1:8080:80"   # specific interface
      - "8080-8090:80-90"     # range
```

### Volumes

```yaml
services:
  app:
    volumes:
      - ./src:/app/src              # bind mount
      - node_modules:/app/node_modules  # named volume
      - /app/temp                   # anonymous volume

volumes:
  node_modules:  # declare named volume
```

### Environment Variables

```yaml
services:
  app:
    environment:
      - NODE_ENV=production
      - DATABASE_URL=postgres://...

    # Or from file
    env_file:
      - .env
      - .env.local
```

### Dependencies

```yaml
services:
  app:
    depends_on:
      - db
      - redis

    # With health check condition
    depends_on:
      db:
        condition: service_healthy
```

### Networks

```yaml
services:
  app:
    networks:
      - frontend
      - backend

networks:
  frontend:
  backend:
    driver: bridge
```

### Health Checks

```yaml
services:
  app:
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
```

### Resource Limits

```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

### Restart Policy

```yaml
services:
  app:
    restart: "no"           # default
    restart: always         # always restart
    restart: on-failure     # only on failure
    restart: unless-stopped # unless manually stopped
```

### Command and Entrypoint

```yaml
services:
  app:
    command: npm run start
    entrypoint: /app/entrypoint.sh
    working_dir: /app
```

## Docker Compose CLI Commands

| Command | Description |
|---------|-------------|
| `docker-compose up` | Create and start |
| `docker-compose up -d` | Detached mode |
| `docker-compose up --build` | Rebuild images |
| `docker-compose down` | Stop and remove |
| `docker-compose down -v` | Also remove volumes |
| `docker-compose ps` | List containers |
| `docker-compose logs` | View logs |
| `docker-compose logs -f` | Follow logs |
| `docker-compose exec <svc> <cmd>` | Execute command |
| `docker-compose build` | Build images |
| `docker-compose pull` | Pull images |
| `docker-compose restart` | Restart services |
| `docker-compose stop` | Stop services |
| `docker-compose start` | Start services |
| `docker-compose config` | Validate and view |

## Multiple Compose Files

```bash
# Override with multiple files
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up

# Use different project name
docker-compose -p myproject up
```

## Profiles

```yaml
services:
  app:
    profiles: []  # always started

  debug:
    profiles: ["debug"]  # only with --profile debug
```

```bash
docker-compose --profile debug up
```
