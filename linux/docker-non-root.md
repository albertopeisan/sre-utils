# Enabling Docker for Non-Root Users (Ubuntu 24.04)

This guide fixes the “permission denied while trying to connect to the Docker daemon socket” error by granting your non-root user (e.g., `admin`) access to the Docker daemon.

## 1. Ensure Docker is running

```bash
sudo systemctl status docker --no-pager
# If inactive:
sudo systemctl enable --now docker
```

## 2. Add your user to the docker group

```bash
# Create the docker group if it does not exist
sudo groupadd -f docker

# Add admin to the group
sudo usermod -aG docker admin
```

## 3. Refresh group membership

Apply the new group membership without logging out:

```bash
newgrp docker
```

Alternatively, log out and back in (reconnect your SSH session), and start a new tmux/screen session if you use one.

## 4. Verify the Docker socket ownership and permissions

```bash
ls -l /var/run/docker.sock
```

Expected output should show the group as `docker`, for example:

```
srw-rw---- 1 root docker ... /var/run/docker.sock
```

If needed, fix and restart Docker:

```bash
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock
sudo systemctl restart docker
```

## 5. Test Docker and Docker Compose without sudo

```bash
id                          # confirm you're in the docker group
docker info
docker run --rm hello-world
docker version
```

## Notes and security considerations

- Do not run `chmod 666 /var/run/docker.sock`; it exposes the daemon to all local users.
- Only trusted users should be in the `docker` group; members can effectively gain root-level access through the Docker API.
- If you installed Docker via snap previously, prefer the official packages to avoid permission quirks; mixing installations can cause socket/group inconsistencies.
- If you switch users (e.g., to `admin`) after adding the group, ensure that the session is refreshed (relogin or `newgrp docker`).