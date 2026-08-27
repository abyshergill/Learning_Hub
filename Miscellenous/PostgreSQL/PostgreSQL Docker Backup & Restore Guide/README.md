## PostgreSQL Docker Backup & Restore Guide

Backing up your PostgreSQL database is a great safety net before updating code or modifying containers. Since you are using Docker, the process is quick and straightforward.

---

### Step 1: Backup Your Database

Run the following command in your terminal to dump all database tables into a single backup file on your server.

> *Make sure to replace `your_db_container_name`, `your_db_user`, and `your_db_name` with your actual values.*

```bash
docker exec -t your_db_container_name pg_dump -U your_db_user your_db_name > backup.sql

```

* **How it works:** It connects to your running container, extracts the database contents, and saves them into a `backup.sql` file in your current directory.

**Pro Tip:** Include the current date in your filename to prevent overwriting older backups:

```bash
docker exec -t your_db_container_name pg_dump -U your_db_user your_db_name > backup_$(date +%Y%m%d).sql

```

---

### Step 2: Restore Your Database

If something breaks and you need to recover your data from a backup file, run:

```bash
docker exec -i your_db_container_name psql -U your_db_user -d your_db_name < backup.sql

```

---

### Recommended Safe Update Workflow

Combining your repository cloning method with a quick safety backup gives you total peace of mind. Follow this routine for smooth updates:

1. **Back up your database:**
```bash
docker exec -t your_db_container_name pg_dump -U your_db_user your_db_name > safety_backup.sql

```


2. **Update your code:** Stop your containers, remove the old repository folder, and re-clone your updated code from GitHub.
3. **Restart your containers:** Run `docker compose up -d` to bring everything back online.

If you want to automate this process so you don't have to manually type out terminal commands every time, you can drop a simple automation script onto your server or set up a dedicated backup sidecar container.

Here are two great ways to take it a step further:

---


### A Simple Automated Bash Script

You can save this script as `backup-db.sh` on your server. It automatically generates a timestamped backup, saves it to a designated folder, and **deletes backups older than 7 days** so your server doesn't run out of disk space.

```bash
#!/bin/bash

# Configuration
CONTAINER_NAME="your_db_container_name"
DB_USER="your_db_user"
DB_NAME="your_db_name"
BACKUP_DIR="/home/your_user/backups"
DAYS_TO_KEEP=7

# Create backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# Generate backup file with current date
BACKUP_FILE="$BACKUP_DIR/db_backup_$(date +%Y%m%d_%H%M%S).sql"

echo "Starting backup for $DB_NAME..."
docker exec -t "$CONTAINER_NAME" pg_dump -U "$DB_USER" "$DB_NAME" > "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "Backup successfully saved to $BACKUP_FILE"
else
    echo "Backup failed!" >&2
    exit 1
fi

# Clean up backups older than X days
find "$BACKUP_DIR" -name "db_backup_*.sql" -type f -mtime +$DAYS_TO_KEEP -delete
echo "Cleaned up backups older than $DAYS_TO_KEEP days."

```

#### Automate it with Cron:

You can make this run automatically (e.g., every day at 2:00 AM) by opening your crontab:

```bash
crontab -e
```

And adding this line:

```cron
0 2 * * * /bin/bash /home/your_user/backups/backup-db.sh >/dev/null 2>&1
```

