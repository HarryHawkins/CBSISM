#!/bin/bash
FILE=s3://CBSISM-backup-bucket
if [ -f "$FILE" ]; then
    echo "$FILE exists."
    #assume the user is using timescaleDB for time series data+web application data
    docker exec -it timescaleDB "pg_dump -Fc -f /etc/backups/CBSISM.bak CBSISM"
    #now copy over a backup file to the bucket
    aws s3 cp “/etc/backups/CBSISM.bak” s3://CBSISM-backup-bucket/
else 
    #on first use create an S3 backup bucket
    echo "$FILE does not exist yet, creating now."
    aws s3 mb s3://CBSISM-backup-bucket
    #assume the user is using timescaleDB for time series data+web application data
    docker exec -it timescaleDB "pg_dump -Fc -f /etc/backups/CBSISM.bak CBSISM"
    #now copy over a backup file to the bucket
    aws s3 cp “/etc/backups/CBSISM.bak” s3://CBSISM-backup-bucket/
fi

