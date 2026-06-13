Welcome to this step-by-step guide on **Mounting Disks with systemd**,

For decades, the go-to method for mounting disks automatically at boot was editing the `/etc/fstab` file. While `fstab` works fine, it has a major drawback: a single typo can cause your entire Linux system to hang during bootup.

Enter **systemd mount units**. Because systemd manages your system's services, dependencies, and boot sequence, letting it manage your disk mounts gives you better error handling, native dependency tracking, and the ability to cleanly automount storage on demand.

---

## Course Overview

* **Module 1:** Gather Your Disk Info (`UUID`)
* **Module 2:** The Strict Naming Rule (The #1 Gotcha)
* **Module 3:** Writing Your First `.mount` Unit File
* **Module 4:** Reload, Start, and Enable
* **Module 5:** Pro-Tip: Adding On-Demand Automounting

---

## Module 1: Gather Your Disk Info (`UUID`)

Before we tell systemd what to mount, we need to uniquely identify the storage drive. While you *could* use device names like `/dev/sdb1`, these can randomly change if you plug in a new drive or swap SATA ports. We will use the **UUID** (Universally Unique Identifier), which never changes.

1. Run the `lsblk` command with the `-f` flag to list all storage blocks and their filesystems:
```bash
lsblk -f

```


2. Locate your target drive partition (e.g., `sdb1`) and copy the long string under the **UUID** column. It will look something like this: `a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6`.
3. Create the directory where you want this disk to appear (its mount point):
```bash
sudo mkdir -p /mnt/storage

```



---

## Module 2: The Strict Naming Rule (The #1 Gotcha)

> 🛑 **Warning:** systemd enforces a strict, non-negotiable rule when it names a mount unit file. **The filename of your unit must exactly match the path of your mount point, replacing slashes with dashes.**

If you ignore this rule, systemd will refuse to load the file, and your disk will not mount.

### Naming Examples:

* If your mount point is `/mnt/storage`, your filename **must** be: `mnt-storage.mount`
* If your mount point is `/media/backup/data`, your filename **must** be: `media-backup-data.mount`
* If your mount point is right at the root `/storage`, your filename **must** be: `storage.mount`

Since we are mounting to `/mnt/storage`, we will name our configuration file `mnt-storage.mount`.

---

## Module 3: Writing Your First `.mount` Unit File

All custom systemd service and unit files live inside `/etc/systemd/system/`. Let's create our file using a text editor like `nano`:

```bash
sudo nano /etc/systemd/system/mnt-storage.mount

```

Paste the following template into the file, making sure to replace the `What` value with your actual disk UUID, and `Type` with your drive's filesystem (usually `ext4`, `xfs`, or `btrfs`):

```ini
[Unit]
Description=Mount Custom External Storage Drive
After=network.target

[Mount]
What=/dev/disk/by-uuid/a1b2c3d4-e5f6-7a8b-9c0d-e1f2a3b4c5d6
Where=/mnt/storage
Type=ext4
Options=defaults

[Install]
WantedBy=multi-user.target

```

### Breakdown of the Configuration:

* **`After=network.target`**: Ensures the system boots up stable basic services before trying to hook up this storage device.
* **`What=`**: Tells systemd exactly which hardware partition to look for via its immutable UUID path.
* **`Where=`**: Specifies the target folder location. *Remember, this must perfectly match the filename structure.*
* **`Type=`**: Defines the filesystem format.
* **`Options=defaults`**: Uses standard Linux mounting options (read/write access, async execution, etc.).

Save and close the file (in nano, press `Ctrl+O`, then `Enter`, then `Ctrl+X`).

---

## Module 4: Reload, Start, and Enable

Whenever you add or change anything inside `/etc/systemd/system/`, you must tell systemd to refresh its internal index database.

1. Reload the systemd daemon layout:
```bash
sudo systemctl daemon-reload

```


2. Trigger the mount immediately to test your configuration file:
```bash
sudo systemctl start mnt-storage.mount

```


3. Verify that the disk successfully mounted by checking its directory size or listing its contents:
```bash
df -h /mnt/storage

```


4. If everything looks good, configure the disk to mount automatically every time your system turns on:
```bash
sudo systemctl enable mnt-storage.mount

```



---

## Module 5: Pro-Tip: Adding On-Demand Automounting

One of the coolest features Jay often highlights on *Learn Linux TV* is systemd's ability to handle **Automounting**.

If you have an external USB hard drive or a network share, you might not want your Linux system waiting around for it during a cold boot. Instead, you can configure systemd to leave the drive asleep, and **instantly mount it the exact second a user or application tries to open the `/mnt/storage` folder.**

To set this up, we create an `.automount` unit file right alongside our original file. It must follow the exact same naming convention:

```bash
sudo nano /etc/systemd/system/mnt-storage.automount

```

Paste the following configuration inside it:

```ini
[Unit]
Description=Automount Custom External Storage On-Demand

[Automount]
Where=/mnt/storage

[Install]
WantedBy=multi-user.target

```

### Final Activation Steps:

Since the `.automount` unit will now look after the folder and wake up the drive automatically, we need to **disable** the regular boot mount service and **enable** the automount unit instead:

```bash
# Disable the static boot mount
sudo systemctl disable mnt-storage.mount

# Enable and start the smart automount engine
sudo systemctl enable mnt-storage.automount
sudo systemctl start mnt-storage.automount

```

Now, reboot your machine. If you run `df -h`, you will notice your drive isn't mounted yet. But the moment you run `cd /mnt/storage` or open it in a file manager, systemd will quietly snap into action, mount the hardware partition instantly behind the scenes, and drop you straight into your files!