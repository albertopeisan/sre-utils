# Configuring SSH for Easy Connections (macOS & Linux)

This guide explains how to create an SSH configuration file (`~/.ssh/config`) on your local machine so you can connect to remote servers with a simple command like:

```bash
ssh myserver
```

instead of typing the full `ssh user@host -i keyfile` command every time.

## 1. Create or edit the SSH config file

Open or create the file:

```bash
nano ~/.ssh/config
```

Make sure the file has the correct permissions:

```bash
chmod 600 ~/.ssh/config
```

## 2. Define a single server

Here is an example configuration for one server:

```sshconfig
Host myserver
  HostName 192.168.1.10
  User admin
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
  ServerAliveInterval 30
  ServerAliveCountMax 3
```

* `Host` → the shortcut name you will use (`ssh myserver`).
* `HostName` → the server’s IP address or domain.
* `User` → the username on the server.
* `IdentityFile` → path to your private key.
* `IdentitiesOnly yes` → ensures only the specified key is used.
* `ServerAliveInterval` and `ServerAliveCountMax` → keep the connection alive.

## 3. Define multiple servers with different keys

You can add multiple entries in the same config file:

```sshconfig
Host webserver
  HostName 203.0.113.5
  User ubuntu
  IdentityFile ~/.ssh/webserver_key
  IdentitiesOnly yes

Host dbserver
  HostName db.example.com
  User dbadmin
  IdentityFile ~/.ssh/dbserver_key
  IdentitiesOnly yes
```

Now you can connect with:

```bash
ssh webserver
ssh dbserver
```

Each server will use its own key and settings.

## 4. Use different ports

If a server uses a custom SSH port (not 22), add:

```sshconfig
Host customserver
  HostName example.com
  User admin
  Port 2222
  IdentityFile ~/.ssh/custom_key
```

Connect with:

```bash
ssh customserver
```

## 5. Advanced example with wildcard hosts

You can also set defaults for multiple hosts:

```sshconfig
Host *.example.com
  User deploy
  IdentityFile ~/.ssh/example_key
  IdentitiesOnly yes
```

This applies to all servers ending in `.example.com`.

---

## 6. Using the configuration

Once the file is saved, you can connect simply with:

```bash
ssh myserver
```

instead of:

```bash
ssh -i ~/.ssh/id_ed25519 admin@192.168.1.10
```

---

You now have a flexible SSH configuration that simplifies connecting to single or multiple servers, each with its own key and settings.
