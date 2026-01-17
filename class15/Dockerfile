# Development Dockerfile for Next.js
FROM node:20-alpine

WORKDIR /app

# Install dependencies first (better caching)
COPY package*.json ./
RUN npm install

# Copy project files
COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev"]
