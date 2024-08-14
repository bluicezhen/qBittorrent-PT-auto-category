# qBittorrent-PT-auto-category

[qBittorrent-PT-auto-category](https://github.com/bluicezhen/qBittorrent-PT-auto-category) is a plugin for qBittorrent that automatically assigns categories to PT (Private Tracker) tasks. It is recommended to run this plugin using Docker. 

## Features

- Automatically categorize PT tasks in qBittorrent.
- Easy to deploy using Docker.

## Prerequisites

- Docker installed on your system.
- qBittorrent Web UI enabled and accessible.

## Getting Started

### Docker Compose

To get started with Docker Compose, create a `docker-compose.yml` file with the following content:

```yaml
version: '3.7'
services:
  qbittorrent-pt-auto-category:
    image: bluicezhen/qbittorrent-pt-auto-category:latest
    container_name: qbittorrent-pt-auto-category
    restart: unless-stopped
    environment:
      QB_URL: https://example.com
      QB_VERIFY: 'false'
      QB_USER: admin
      QB_PASS: 123456
```

Replace the environment variables with your qBittorrent settings:

- `QB_URL`: The URL of your qBittorrent Web UI.
- `QB_VERIFY`: Set to `'false'` if you don't want to verify SSL certificates.
- `QB_USER`: Your qBittorrent Web UI username.
- `QB_PASS`: Your qBittorrent Web UI password.

### Running the Container

Navigate to the directory containing your `docker-compose.yml` file and run the following command:

```sh
docker-compose up -d
```

This command will pull the Docker image and start the container in detached mode.

### Stopping the Container

To stop the container, run:

```sh
docker-compose down
```

## Environment Variables

- `QB_URL`: URL of the qBittorrent Web UI (e.g., `https://example.com`).
- `QB_VERIFY`: Whether to verify SSL certificates (`true` or `'false'`).
- `QB_USER`: Username for the qBittorrent Web UI.
- `QB_PASS`: Password for the qBittorrent Web UI.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/bluicezhen/qBittorrent-PT-auto-category).

---

Thank you for using qBittorrent-PT-auto-category!
