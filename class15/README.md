# Class Notes

Q) Why Bind Mountings?
- Applications running inside docker containers are isolated/soundproof

- Bind mounts means "Sync Connection"

## To run a Container from Image:
- docker run -d -p 3000:3000 --name my-container <image-name>

- -d - detached
- -p - port
- --name: Name of docker container
- <image-name>: Name of the image


Q) What is Detached Mode?
When you run a container with detached mode (-d) it only returns a container-id.

- Name of the file to work with volumes:
- docker-compose.yml
- docker-compose.yaml
  - Watch Mode
  - to enable watch mode: press
    "w"


Q) What does watch mode do?
  - sync - Syncs changes from ./app and ./public folders to the container without
  rebuilding

  - rebuild - Rebuilds the container when package.json changes (new dependencies)

  - command: npm run dev - Overrides the Dockerfile to run in dev mode (required for hot
  reload)

===
 - To run with watch mode:
 - docker compose watch

 - Or run detached:
 - docker compose watch -d


## Watch Mode:

    develop:
      watch:
        - action: sync
          path: ./app # Local app directory
          target: /app/app
Summary for watch mode:
1) Create a docker-compose.yaml file to enable watch mode.
2) sync your Machine(Laptop) app and public directory with docker app and public directory.
3) Run command docker-compose up.
4) Docker compose itself creates a new image
