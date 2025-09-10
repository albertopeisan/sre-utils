# Linux file and directory permissions

This document provides examples of how to manage permissions for users and groups on Linux. Use `chmod`, `chown`, and `chgrp` to control access.

## Permission numbers (octal notation)

Permissions are represented by three numbers: **owner**, **group**, and **others**.  
Each number is the sum of:
- **4** = read (r)
- **2** = write (w)
- **1** = execute (x)

Examples:
- **7** = 4+2+1 = read, write, execute (rwx)
- **6** = 4+2 = read, write (rw-)
- **5** = 4+1 = read, execute (r-x)
- **4** = read only (r--)
- **0** = no permissions (---)

Common modes:
- **755** = owner rwx, group r-x, others r-x  
- **700** = owner rwx, group ---, others ---  
- **644** = owner rw-, group r--, others r--

## Ownership

Each file or directory has:
- **Owner** (a user)
- **Group**
- **Permissions** (read, write, execute) for owner, group, and others

Check ownership and permissions:
```bash
ls -l /opt/example
````

## Giving a user ownership (full control)

Make a specific user the owner of a directory:

```bash
sudo chown -R alice:alice /opt/example
```

Now `alice` can read, write, and delete inside `/opt/example`.

## Read-only permissions

Allow everyone to read but not write:

```bash
sudo chmod -R 755 /opt/example
```

* Owner: read/write/execute
* Group: read/execute
* Others: read/execute

Remove write access for all but owner:

```bash
sudo chmod -R 744 /opt/example
```

## Write permissions for a group

Give a group write access:

```bash
sudo chgrp -R developers /opt/example
sudo chmod -R 775 /opt/example
```

* Owner: full access
* Group (`developers`): full access
* Others: read/execute only

Add a user to the group:

```bash
sudo usermod -aG developers bob
```

## Read-only for a group

```bash
sudo chgrp -R auditors /opt/example
sudo chmod -R 754 /opt/example
```

* Group members can read/execute but not write.

## Restricting access completely

Only the owner can read/write:

```bash
sudo chmod -R 700 /opt/example
```

## Useful patterns

### Shared project directory

Create a group for a project:

```bash
sudo groupadd projectx
sudo chown -R root:projectx /opt/example
sudo chmod -R 2775 /opt/example
```

Add users to `projectx`:

```bash
sudo usermod -aG projectx alice
sudo usermod -aG projectx bob
```

The `2` in `2775` (setgid bit) ensures new files inherit the group.

### Temporary read/write

Grant a single user write access via ACL:

```bash
sudo setfacl -m u:alice:rwx /opt/example
```

Revoke later:

```bash
sudo setfacl -x u:alice /opt/example
```

## Quick reference

* `chmod` — change permissions (numbers: 7=rwx, 6=rw-, 5=r-x, 4=r--)
* `chown` — change owner
* `chgrp` — change group
* `setfacl` — fine-grained access control
