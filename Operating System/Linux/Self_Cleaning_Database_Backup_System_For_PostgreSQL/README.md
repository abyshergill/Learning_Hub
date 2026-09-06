# Self cleaning database backup system

This guide outlines the setup and automation of a self-cleaning database backup system for PostgreSQL running in Docker.

## System Architecture

The maintenance process relies on three interconnected scripts to manage your data safely:

* **`run_all.sh` (Master Script):** The primary trigger that sequentially executes the backup and cleanup operations.
* **`backup.sh`:** Connects to the Docker container, generates a database dump, and saves it to your local disk with a timestamp.
* **`cleanup.sh`:** Scans the backup directory and permanently deletes files older than your configured retention period to prevent disk space exhaustion.

## Initial Setup & Permissions

Before automating the process, the Linux operating system requires explicit permission to execute these files.

1. Navigate to the directory containing your saved scripts.
2. Run the following command to make all three files executable:
```bash
chmod +x run_all.sh backup.sh cleanup.sh
```
Now, you can trigger the entire process at any time by running:

```bash
./run_all.sh
```

## Automating with Cron

Cron jobs run in a restricted background environment and do not know your current working directory. You must use absolute file paths (e.g., `/root/db_scripts/`) for the automation to function.

**1. Open the Cron Editor**
Launch the cron configuration file for your current active user:

```bash
crontab -e
```

*(If prompted to select an editor on your first run, press `1` to use nano).*

**2. Define the Schedule**
Scroll to the very bottom of the file and paste the schedule. Replace `/root/db_scripts/` with the exact directory path where your scripts live:

```text
0 2 * * * /bin/bash /root/db_scripts/run_all.sh >> /root/db_scripts/backup_cron.log 2>&1
```

* `0 2 * * *` executes the script at exactly 2:00 AM server time, every day.
* `>>` captures any background terminal output or errors and logs them to `backup_cron.log` so you can verify the job ran successfully.

**3. Save and Exit**

* In nano, press `Ctrl+O`, then hit `Enter` to save the file.
* Press `Ctrl+X` to exit the editor.
* The terminal will output `crontab: installing new crontab` to confirm success.

**4. Verify the Active Job**
List out your active scheduled tasks to ensure the new rule was saved properly:

```bash
crontab -l
```