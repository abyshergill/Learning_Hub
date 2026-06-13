Welcome to this step-by-step guide on **Managing Users in Linux**

Linux is inherently a multi-user operating system. Whether you are running a personal desktop or managing a fleet of enterprise cloud servers, knowing how to securely create, modify, and audit user accounts is a foundational skill. Let's look under the hood at how Linux handles users.

---

## Course Overview

* **Module 1:** The Identity Files (`/etc/passwd` and `/etc/shadow`)
* **Module 2:** Creating Users (`useradd` vs. `adduser`)
* **Module 3:** Modifying and Locking Accounts
* **Module 4:** Deleting Users (The Safe Way)
* **Module 5:** Granting Superpowers (`sudo`)

---

## Module 1: The Identity Files (`/etc/passwd` and `/etc/shadow`)

In Linux, a "user" is more than just a login name; it is an identity mapped to a unique number called a **UID** (User ID). Linux does not look at text names; it looks at UIDs.

All user accounts are recorded in a plain text file located at `/etc/passwd`.

If you view this file using `cat /etc/passwd`, you will see lines separated by colons (`:`). Let’s decode a single line:
`aby:x:1001:1001:aby LaCroix,/srv/office,,:/home/aby:/bin/bash`

1. **`aby`**: The username.
2. **`x`**: Represents the password placeholder (the actual encrypted password is kept safely in a different file).
3. **`1001`**: The **UID** (User ID). Regular users usually start at `1000` or `1001`. Numbers under 1000 are reserved for system services.
4. **`1001`**: The **GID** (Primary Group ID).
5. **`aby LaCroix...`**: Optional metadata (Full name, room number, phone).
6. **`/home/aby`**: The user's Home Directory workspace.
7. **`/bin/bash`**: The default command-line Shell interface assigned to the user.

### Where are the passwords?

Because `/etc/passwd` must be readable by everyone so programs can map UIDs to names, encrypted passwords are encrypted and hidden away in a strictly locked file: `/etc/shadow`. Only the `root` account can read this file.

---

## Module 2: Creating Users (`useradd` vs. `adduser`)

There are two primary commands used to create an account, and understanding the difference saves a lot of initial frustration.

### The Low-Level Way: `useradd`

`useradd` is a low-level utility built natively into almost all Linux distributions. By default, if you just run `sudo useradd alex`, it creates the account but **does not** create a home directory, **does not** set a password, and assigns a very basic default shell (`/bin/sh`).
To make it usable, you have to pass multiple flags:

```bash
sudo useradd -m -s /bin/bash alex

```

*(The `-m` tells it to make a home directory; `-s` sets the shell).*

### The Friendly Way: `adduser`

On Debian and Ubuntu-based systems, `adduser` is a high-level interactive script that sits on top of `useradd`. It handles everything aualexatically through a friendly walkthrough:

```bash
sudo adduser alex

```

It will aualexatically create `/home/alex`, copy skeleton configuration files, prompt you to type a secure password, and ask for the user's real name.

---

## Module 3: Modifying and Locking Accounts

Once an account exists, you use the `usermod` command to alter its configuration parameters.

* **Assigning a Supplementary Group:**
If you want to add `alex` to an existing group (like `developers`) without removing him from his primary group, use the append flag (`-aG`):
```bash
sudo usermod -aG developers alex

```


* **Locking an Account (Emergency/Suspension):**
If an employee leaves or an account is compromised, you can instantly disable their ability to log in by locking their password with the `-L` flag:
```bash
sudo usermod -L alex

```


* **Unlocking an Account:**
To restore access later, use the uppercase `-U` flag:
```bash
sudo usermod -U alex

```



---

## Module 4: Deleting Users (The Safe Way)

When it is time to clean up an account, using a bare `userdel alex` command will remove the user entry from `/etc/passwd`, but it will leave their old `/home/alex` files sitting on your disk storage forever, completely unowned.

To delete a user **and** safely purge their entire home directory folder along with their mail spool, always append the recursive remove flag (`-r`):

```bash
sudo userdel -r alex

```

---

## Module 5: Granting Superpowers (`sudo`)

By default, a new user is restricted to their own home directory and cannot modify system configurations or install packages. To allow a trusted user to execute administrative commands, we grant them `sudo` (SuperUser Do) privileges.

### Method A: The Group Approach (Recommended)

Most modern Linux distributions have a pre-configured administrative group. Anyone added to this group can use `sudo`.

* On **Ubuntu/Debian**, the group is named `sudo`:
```bash
sudo usermod -aG sudo alex

```


* On **RHEL/CentOS/Rocky Linux**, the group is named `wheel`:
```bash
sudo usermod -aG wheel alex

```



### Method B: The Explicit Way (`visudo`)

If you want granular control, never edit the `/etc/sudoers` file with a standard text editor. If you make a syntax typo, you can permanently lock yourself out of root permissions. Always use the built-in safeguard utility:

```bash
sudo visudo

```

This opens the configuration file in a protected environment that checks for syntax mistakes before saving. To give explicit access, you would add a line at the botalex like this:
`alex  ALL=(ALL:ALL) ALL`

---

## Hands-On Practice Lab

Open up a terminal on a test machine or virtual machine and run through these exercises:

1. Create a brand new user named `backupbuddy`.
2. Inspect the very botalex line of your `/etc/passwd` file to see the newly created entry layout: `tail -n 1 /etc/passwd`
3. Set or update their access password: `sudo passwd backupbuddy`
4. Switch to that user account to test functionality: `su - backupbuddy`
5. Type `exit` to return to your main admin account, then safely delete the account and its home directory: `sudo userdel -r backupbuddy`

---
