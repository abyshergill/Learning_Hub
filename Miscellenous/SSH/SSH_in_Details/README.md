# SSH Guide

## What is SSH?

**SSH (Secure Shell)** is a cryptographic network protocol used to securely log into and execute commands on a remote machine over an unsecured network.

---

## Step 1: Check If You Have SSH Installed

Most modern operating systems (Linux, macOS, and Windows 10/11) come with an SSH client pre-installed.

1. Open your terminal:
* **Windows:** Open **PowerShell** or **Command Prompt**.
* **macOS/Linux:** Open **Terminal**.


2. Run the command:
```bash
ssh -V

```


3. **Result:** If you see a version number (e.g., `OpenSSH_8.9p1...`), you are good to go.

---

## Step 2: Basic Connection (Password Authentication)

To connect to a remote server using a username and password:

1. Use the standard SSH syntax:
```bash
ssh username@remote_host_ip

```


*Example:*
```bash
ssh ubuntu@192.168.1.50

```


2. **First-time warning:** If connecting for the first time, you will see a host key fingerprint prompt:
```text
The authenticity of host '192.168.1.50' can't be established.
Are you sure you want to continue connecting (yes/no/[fingerprint])?

```


3. Type **`yes`** and press **Enter**.
4. Enter your remote account **password** when prompted (note: characters will not show on screen as you type).

---

## Step 3: Generate SSH Key Pairs (Recommended for Security)

Password authentication can be vulnerable to brute-force attacks. **SSH Keys** offer a safer, convenient alternative.

An SSH key pair consists of two keys:

* **Private Key:** Stored on your local machine. **Never share this!**
* **Public Key:** Placed on the remote server you want to access.

### 1. Generate the Key Pair

Run this command on your **local computer**:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"

```

*(Note: `ed25519` is modern and highly secure. If legacy support is needed, use `ssh-keygen -t rsa -b 4096`.)*

### 2. Specify Key Location & Passphrase

* **File location:** Press **Enter** to accept the default location (`~/.ssh/id_ed25519`).
* **Passphrase:** Enter a strong passphrase for extra security, or press **Enter** twice for no passphrase (convenient, but less secure).

---

## Step 4: Copy the Public Key to the Remote Server

You need to transfer your **public key** (`~/.ssh/id_ed25519.pub`) to the remote machine.

### Method A: Automatic (Linux / macOS / WSL)

Run this command from your local machine:

```bash
ssh-copy-id username@remote_host_ip

```

Enter your password once when prompted. Your key will automatically be installed.

### Method B: Manual (Windows PowerShell or Fallback)

If `ssh-copy-id` is unavailable, run this command from your local PowerShell:

```powershell
cat ~/.ssh/id_ed25519.pub | ssh username@remote_host_ip "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"

```

---

## Step 5: Test Key-Based Login

Now try logging into the server again:

```bash
ssh username@remote_host_ip

```

* **If you set a passphrase:** You will be prompted to enter your SSH key passphrase (not your user password).
* **If you didn't set a passphrase:** You will instantly log in without typing anything!

---

## Step 6: Create an SSH Config File (Shortcut Tool)

Instead of typing `ssh username@192.168.1.50 -p 2222 -i ~/.ssh/my_key` every time, you can create a config file on your local machine.

1. Open or create the config file in your local terminal:
```bash
nano ~/.ssh/config

```


2. Add your server profile:
```ini
Host myserver
    HostName 192.168.1.50
    User ubuntu
    Port 22
    IdentityFile ~/.ssh/id_ed25519

```


3. Save and exit (press `Ctrl + O`, `Enter`, then `Ctrl + X`).
4. Now, simply log in using the alias:
```bash
ssh myserver

```



---

## Step 7: Useful Essential SSH Commands

| Task | Command Syntax |
| --- | --- |
| **Connect using a specific port** | `ssh -p 2222 username@remote_ip` |
| **Specify a specific identity key** | `ssh -i ~/.ssh/custom_key username@remote_ip` |
| **Copy file from local to remote** | `scp local_file.txt username@remote_ip:/path/to/destination/` |
| **Copy folder from remote to local** | `scp -r username@remote_ip:/path/to/remote_folder/ ./local_folder/` |
| **Exit SSH session** | `exit` |


## When you SSH into a server for the first time and type `yes` to accept the prompt, it feels like the setup is complete. If you think like this way then you wrong

However, accepting that prompt only saves the **Server's Identity Key** onto your computer. It does **not** copy your key to the server.

Here is the exact difference between accepting that first prompt and copying your SSH key:

---

### 1. What typing `yes` actually does

When you connect for the first time, SSH shows a warning:

> *"The authenticity of host '192.168.1.50' can't be established..."*

When you type **`yes`**:

* The server sends **its** host key to **your** computer.
* Your machine saves this key into a file called `~/.ssh/known_hosts`.
* **Purpose:** This protects *you* against "Man-in-the-Middle" attacks. It makes sure that future connections are going to the exact same physical server.

---

### 2. Why you still need to copy your Public Key

Saving the server's key into `known_hosts` proves you trust the server. But **the server still doesn't know who you are**.

To log in without entering a password every single time, the server must hold your **Public Key** inside its `~/.ssh/authorized_keys` file.

* **Without copying the key (`ssh-copy-id`):** Every time you connect, the server will ask you for your account **Password**.
* **After copying the key:** The server compares your Private Key to the Public Key stored in its `authorized_keys` file, verifies your identity, and lets you in **without asking for a password**.

---

### Summary Checklist

| Action | What happens? | Result |
| --- | --- | --- |
| **Typing `yes` on 1st connect** | You save the *server's* key to your `known_hosts` file. | You trust the server. You still need a **password** to log in. |
| **Running `ssh-copy-id**` | You copy *your* public key into the server's `authorized_keys` file. | The server trusts you. You can log in **passwordlessly**. |

## How SSH public key mehanism work with your personal system and github private repo.

GitHub is just a remote server. When you run `git clone git@github.com:...`:

1. GitHub asks your computer: *"Who are you?"*
2. Your computer presents your **Private Key**.
3. GitHub checks its database for a **Public Key** that matches.
4. If it finds the key attached to your GitHub account, it grants you access to your private repository—**no password required**.

Because you can't run `ssh-copy-id` directly on GitHub's backend servers, you have to manually paste your public key into the **GitHub Web UI**.

---

### Quick Steps to Add Your SSH Key to GitHub

#### 1. Copy your Public Key to your clipboard

Open your terminal and run:

* **Windows (PowerShell):**
```powershell
cat ~/.ssh/id_ed25519.pub | clip

```


* **macOS:**
```bash
pbcopy < ~/.ssh/id_ed25519.pub

```


* **Linux:**
```bash
cat ~/.ssh/id_ed25519.pub

```


*(Then manually highlight and copy the output text starting with `ssh-ed25519...`)*

---

#### 2. Add it to GitHub

1. Log in to [GitHub](https://github.com).
2. Click your profile picture (top right) $\rightarrow$ **Settings**.
3. In the left sidebar, click **SSH and GPG keys**.
4. Click the green **New SSH key** button.
5. **Title:** Give it a clear name (e.g., `Work Laptop` or `Home PC`).
6. **Key:** Paste your copied public key into the box.
7. Click **Add SSH key**.

---

#### 3. Test your connection

Run this command in your terminal:

```bash
ssh -T git@github.com

```

* You will see the familiar first-time prompt asking if you want to trust GitHub's host key. Type **`yes`**.
* If configured correctly, GitHub will respond with:
> *"Hi username! You've successfully authenticated, but GitHub does not provide shell access."*



From then on, you can `git clone`, `git push`, and `git pull` from your private repositories seamlessly!