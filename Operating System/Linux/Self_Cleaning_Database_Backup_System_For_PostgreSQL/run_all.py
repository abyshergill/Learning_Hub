#============================================================================
#
# This script simply triggers the backup and cleanup scripts in order.
#
#============================================================================

#!/bin/bash
# Get the directory where this script is located
SCRIPT_DIR=$(dirname "$0")

echo "=== Starting Database Maintenance ==="

# 1. Run the backup script
bash "$SCRIPT_DIR/backup.sh"

# 2. Run the cleanup script
bash "$SCRIPT_DIR/cleanup.sh"

echo "=== Maintenance Complete ==="