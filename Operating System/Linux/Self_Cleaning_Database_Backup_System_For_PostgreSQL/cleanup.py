#===================================================================================================
#
# This uses the Linux `find` command to locate and delete files older than your specified timeframe.
#
#===================================================================================================

#!/bin/bash

# --- Configuration ---
BACKUP_DIR="/root/db_backups"  # Must match the directory in backup.sh
DAYS_TO_KEEP=7                 # Delete backups older than this many days
# ---------------------

echo "Checking for backups older than $DAYS_TO_KEEP days..."

# Find and delete old .sql backup files
find "$BACKUP_DIR" -type f -name "*_backup.sql" -mtime +$DAYS_TO_KEEP -exec rm -f {} \;

echo "Cleanup finished."
