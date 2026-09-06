#======================================================================================================
#
# This uses Docker to execute `pg_dump` inside your container and saves it directly to your VPS drive.
#
#======================================================================================================

#!/bin/bash

# --- Configuration ---

BACKUP_DIR="/root/db_backups"           # Where to save the files on your VPS
CONTAINER_NAME="my_postgres_container"  # Name of your docker container
DB_USER="postgres"                      # Your database username
DB_NAME="my_database"                   # The database you want to backup

# ---------------------

# Ensure the backup directory exists
mkdir -p "$BACKUP_DIR"

# Create the date_time_database_backup filename
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/${TIMESTAMP}_${DB_NAME}_backup.sql"

echo "Backing up database '$DB_NAME'..."

# Run pg_dump inside the container and pipe the output to our backup file
docker exec $CONTAINER_NAME pg_dump -U $DB_USER $DB_NAME > "$BACKUP_FILE"

# Check if the command succeeded
if [ $? -eq 0 ]; then
    echo "Success: Backup saved to $BACKUP_FILE"
else
    echo "Error: Backup failed!"
    rm -f "$BACKUP_FILE" # Delete the empty/corrupted file
    exit 1
fi