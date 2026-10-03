# Server

How the production server was set up, so it can be rebuilt from scratch.

## Overview

- **Host:** Hetzner Cloud, smallest shared-vCPU x86 plan, Debian 13, hostname `web1`. No Hetzner backups: the site is rebuilt from git.
- **Domain:** `aiwhistleblowing.org`, with WHOIS privacy on.
- **DNS:** `A` and `AAAA` records for `@` and `www`, pointing to the server's IPv4 address and the `::1` address in its IPv6 `/64`.
- **Hetzner Cloud Firewall:** inbound TCP 22, 80 and 443 only.

## SSH key

A dedicated key, used for nothing else:

```sh
ssh-keygen -t ed25519 -f ~/.ssh/wbtracker_ed25519 -C "wbtracker"
```

The public key was added to the server when it was created, so root never had a password.

Local `~/.ssh/config`:

```
Host wbtracker
    HostName <server IPv4>
    User admin
    IdentityFile ~/.ssh/wbtracker_ed25519
    IdentitiesOnly yes
```

## Hardening

Run as root, in this order: confirm that `admin` can log in and use sudo before turning off root login.

1. Update packages:

   ```sh
   apt-get update && apt-get upgrade -y
   ```

2. Create an `admin` user with key-only login and sudo:

   ```sh
   adduser --disabled-password --gecos "" admin
   usermod -aG sudo admin
   echo "admin ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/90-admin
   chmod 440 /etc/sudoers.d/90-admin
   visudo -cf /etc/sudoers.d/90-admin
   install -d -m 700 -o admin -g admin /home/admin/.ssh
   install -m 600 -o admin -g admin /root/.ssh/authorized_keys /home/admin/.ssh/authorized_keys
   ```

   Sudo needs no password because `admin` has none: login is by SSH key only.

3. Check from the local machine: `ssh wbtracker 'whoami; sudo -n whoami'` should print `admin` then `root`.

4. Turn off root and password logins:

   ```sh
   printf "PermitRootLogin no\nPasswordAuthentication no\nKbdInteractiveAuthentication no\n" \
     > /etc/ssh/sshd_config.d/00-hardening.conf
   sshd -t && systemctl reload ssh
   ```

   sshd uses the first value it reads for each setting, and reads the files in `sshd_config.d/` in name order. The `00-` prefix makes these settings win over any later drop-in, such as one added by cloud-init.

5. Check:

   ```sh
   sshd -T | grep -E "^(permitrootlogin|passwordauthentication|kbdinteractiveauthentication) "
   ```

   All three should be `no`. From the local machine, `ssh -o User=root wbtracker` should fail with `Permission denied (publickey)`.

## Automatic security updates

Hetzner's Debian image already installs and enables `unattended-upgrades`, which applies Debian security updates every day. Check with:

```sh
cat /etc/apt/apt.conf.d/20auto-upgrades   # both values "1"
systemctl is-enabled unattended-upgrades  # enabled
```
