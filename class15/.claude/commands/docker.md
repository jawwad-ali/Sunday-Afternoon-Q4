---
description: Execute Docker commands - build images, run containers, manage containers, view logs, and handle Docker Compose
allowed-tools: Bash(docker:*), Bash(docker-compose:*), Read, Glob, Grep, Write
argument-hint: <command> [options]
---

You are a Docker operations expert. Handle all Docker-related tasks for this project.

## User Request
$ARGUMENTS

## Skill Resources

For detailed reference, consult these skill files:
- **@.claude/skills/docker/SKILL.md** - Main skill documentation
- **@.claude/skills/docker/references/docker-commands.md** - Complete CLI reference
- **@.claude/skills/docker/references/docker-compose.md** - Compose configuration guide
- **@.claude/skills/docker/examples/Dockerfile.example** - Sample Dockerfile
- **@.claude/skills/docker/examples/docker-compose.example.yml** - Sample Compose file

## Quick Reference

### Build & Run
```bash
docker build -t <name>:<tag> .
docker run -d -p <host>:<container> --name <name> <image>
```

### Container Management
```bash
docker ps [-a]                    # List containers
docker stop/start/restart <id>    # Lifecycle
docker rm [-f] <id>               # Remove
docker logs [-f] <id>             # View logs
docker exec -it <id> /bin/sh      # Shell access
```

### Image Management
```bash
docker images                     # List
docker pull/push <image>          # Registry
docker rmi <image>                # Remove
```

### Docker Compose
```bash
docker-compose up [-d] [--build]  # Start
docker-compose down [-v]          # Stop
docker-compose logs [-f]          # Logs
docker-compose ps                 # Status
```

### Cleanup
```bash
docker system prune [-a]          # Clean all
docker volume/network prune       # Specific cleanup
```

## Instructions

1. First, verify Docker is running: `docker info`
2. Check for existing Dockerfile/docker-compose.yml if needed
3. Execute the appropriate Docker command(s)
4. Provide clear output and explain what was done
5. For errors, explain the issue and suggest fixes

## Creating Docker Files

If user needs a Dockerfile or docker-compose.yml:
1. Read the example files from the skill
2. Customize based on project requirements (Next.js project detected)
3. Write the file to the project root

## Important Notes
- Use meaningful container/image names
- Always use specific tags (avoid `latest` in production)
- Be careful with destructive operations (rm, prune)
- For long-running containers, use detached mode (-d)
