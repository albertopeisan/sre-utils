# Creating a Passwordless User for SSH (Ubuntu 24.04)

This guide explains how to create a **non-root user** that can log in using **SSH keys only** (no password).
We’ll use `admin` as the example username.

## 1. Create the user without a password

Run this as **root**:

```bash
adduser --disabled-password --gecos "" admin
```

* `--disabled-password` → no usable password is set.
* `--gecos ""` → skips interactive prompts (name, phone, etc.).
* `admin` → the username.

## 2. Give the user sudo privileges

```bash
usermod -aG sudo admin
```

This lets `admin` run `sudo` for administrative tasks.

## 3. Add an SSH key for the user

1. On your **local machine**, if you don’t already have a keypair, generate one:

   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

   This creates a private key (`~/.ssh/id_ed25519`) and a public key (`~/.ssh/id_ed25519.pub`).

2. Copy the **public key** to the server:

   ```bash
   ssh-copy-id -i ~/.ssh/id_ed25519.pub admin@<YOUR_SERVER_IP>
   ```

   Alternatively, you can manually paste your public key into:

   ```bash
   /home/admin/.ssh/authorized_keys
   ```

   Make sure permissions are correct:

   ```bash
   chown -R admin:admin /home/admin/.ssh
   chmod 700 /home/admin/.ssh
   chmod 600 /home/admin/.ssh/authorized_keys
   ```

## 4. Test login as `admin`

From your **local machine**:

```bash
ssh -i ~/.ssh/id_ed25519 admin@<YOUR_SERVER_IP>
```

If successful, you are now logged in as `admin`.

## 5. Update your SSH config (optional)

To make connecting easier, configure `~/.ssh/config` on your local machine:

```sshconfig
Host myapp-server
  HostName <YOUR_SERVER_IP>
  User admin
  IdentityFile ~/.ssh/id_ed25519
  IdentitiesOnly yes
  AddKeysToAgent yes
  UseKeychain yes
  ServerAliveInterval 30
  ServerAliveCountMax 3
```

Now you can simply connect with:

```bash
ssh myapp-server
```

You now have a passwordless, sudo-enabled user (`admin`) secured with SSH keys.
