#!/bin/bash
# Docker Installation and Status Check Script
# Usage: bash docker-check.sh

echo "========================================"
echo "Docker Environment Check"
echo "========================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed"
    echo ""
    echo "Install Docker:"
    echo "  - Windows/Mac: https://www.docker.com/products/docker-desktop"
    echo "  - Linux: https://docs.docker.com/engine/install/"
    exit 1
fi

echo "✅ Docker is installed"
echo ""

# Check Docker version
echo "Docker Version:"
docker --version
echo ""

# Check if Docker daemon is running
if ! docker info &> /dev/null; then
    echo "❌ Docker daemon is not running"
    echo ""
    echo "Start Docker:"
    echo "  - Windows/Mac: Start Docker Desktop application"
    echo "  - Linux: sudo systemctl start docker"
    exit 1
fi

echo "✅ Docker daemon is running"
echo ""

# Check Docker Compose
echo "Docker Compose Version:"
if command -v docker-compose &> /dev/null; then
    docker-compose --version
elif docker compose version &> /dev/null; then
    docker compose version
else
    echo "⚠️  Docker Compose not found (optional)"
fi
echo ""

# Show system info
echo "========================================"
echo "Docker System Info"
echo "========================================"
echo ""

echo "Containers:"
docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" 2>/dev/null || echo "No containers"
echo ""

echo "Images:"
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}" 2>/dev/null | head -10
echo ""

echo "Disk Usage:"
docker system df 2>/dev/null
echo ""

echo "========================================"
echo "Check Complete"
echo "========================================"
