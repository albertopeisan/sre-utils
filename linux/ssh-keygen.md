# Generating an SSH Key Pair (macOS & Linux)

This guide explains how to generate a secure SSH key pair on your **MacBook** or **Linux machine**. The key pair consists of a **private key** (kept safe on your computer) and a **public key** (shared with remote servers).

## 1. Generate a new SSH key pair

Run this command on your **MacBook** or **Linux machine**:

```bash
ssh-keygen -t ed25519
```

If Ed25519 is not supported on your system, use RSA as a fallback:

```bash
ssh-keygen -t rsa -b 4096
```

### Optional arguments

* `-C "comment"` → add a label (email or description).
* `-f /path/to/keyfile` → specify a custom filename for the key.
* `-N "passphrase"` → provide a passphrase during generation (not recommended to use directly on the command line, better to set interactively).

## 2. Save the key files

You will be prompted:

```
Enter file in which to save the key (/home/username/.ssh/id_ed25519):
```

Press **Enter** to accept the default, or specify a different filename if you want multiple keys.

Then you’ll be asked for a **passphrase** (recommended). This adds extra protection in case your private key is compromised.

## 3. Verify the keys

After generation, your keys will be stored in `~/.ssh/`:

* **Private key:** `~/.ssh/id_ed25519`
* **Public key:** `~/.ssh/id_ed25519.pub`

Check with:

```bash
ls -l ~/.ssh/id_ed25519*
```

## 4. Use the public key

The file `~/.ssh/id_ed25519.pub` contains your **public key**. This key can now be sent to any remote server or platform where you want to connect. Once added there, you can authenticate securely using the corresponding **private key** stored on your computer.
