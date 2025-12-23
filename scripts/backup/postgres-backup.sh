#!/bin/bash

# PostgreSQL backup script for meditation app
# Usage: ./postgres-backup.sh [environment]

set -euo pipefail

ENVIRONMENT=${1:-production}
BACKUP_DIR="/backups/postgres"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="meditation_db_${ENVIRONMENT}_${TIMESTAMP}.sql.gz"
RETENTION_DAYS=30

# Database connection settings
DB_HOST="${DB_HOST:-localhost}"
DB_PORT="${DB_PORT:-5432}"
DB_NAME="${DB_NAME:-meditation_db}"
DB_USER="${DB_USER:-meditation_user}"

# S3 settings for backup storage
S3_BUCKET="${S3_BUCKET:-meditation-app-backups}"
S3_PREFIX="postgres/${ENVIRONMENT}"

echo "Starting PostgreSQL backup for ${ENVIRONMENT} environment..."

# Create backup directory
mkdir -p "${BACKUP_DIR}"

# Create database backup
echo "Creating database dump..."
pg_dump -h "${DB_HOST}" -p "${DB_PORT}" -U "${DB_USER}" -d "${DB_NAME}" \
    --no-password --verbose --clean --no-owner --no-privileges \
    | gzip > "${BACKUP_DIR}/${BACKUP_FILE}"

if [ $? -eq 0 ]; then
    echo "Database backup created successfully: ${BACKUP_FILE}"
    
    # Upload to S3
    echo "Uploading backup to S3..."
    aws s3 cp "${BACKUP_DIR}/${BACKUP_FILE}" "s3://${S3_BUCKET}/${S3_PREFIX}/${BACKUP_FILE}"
    
    if [ $? -eq 0 ]; then
        echo "Backup uploaded to S3 successfully"
        
        # Remove local backup file
        rm "${BACKUP_DIR}/${BACKUP_FILE}"
        echo "Local backup file removed"
        
        # Clean up old backups from S3
        echo "Cleaning up old backups (older than ${RETENTION_DAYS} days)..."
        aws s3 ls "s3://${S3_BUCKET}/${S3_PREFIX}/" | \
        while read -r line; do
            createDate=$(echo $line | awk '{print $1" "$2}')
            createDate=$(date -d "$createDate" +%s)
            olderThan=$(date -d "${RETENTION_DAYS} days ago" +%s)
            if [[ $createDate -lt $olderThan ]]; then
                fileName=$(echo $line | awk '{print $4}')
                if [[ $fileName != "" ]]; then
                    aws s3 rm "s3://${S3_BUCKET}/${S3_PREFIX}/${fileName}"
                    echo "Deleted old backup: ${fileName}"
                fi
            fi
        done
        
    else
        echo "Error uploading backup to S3"
        exit 1
    fi
else
    echo "Error creating database backup"
    exit 1
fi

echo "PostgreSQL backup completed successfully!"