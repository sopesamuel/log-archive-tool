#!/usr/bin/env python3

import subprocess
import sys
import os
from datetime import datetime

# Check if user provided a directory
if len(sys.argv) != 2:
    print("Usage: python3 log_archive.py <directory>")
    sys.exit(1)

# Get the directory from command line
log_dir = sys.argv[1]

# Check if directory exists
if not os.path.exists(log_dir):
    print(f"Error: Directory '{log_dir}' does not exist!")
    sys.exit(1)

# Create timestamp for archive name
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
archive_name = f"logs_archive_{timestamp}.tar.gz"

print(f"✅ Directory found: {log_dir}")
print(f"📦 Archive will be named: {archive_name}")
print(f"⏰ Timestamp: {timestamp}")

# Create archives directory
archive_dir = "archives"
if not os.path.exists(archive_dir):
    os.makedirs(archive_dir)
    print(f"📁 Created archives directory: {archive_dir}")

# Put archive in the archives folder
archive_path = os.path.join(archive_dir, archive_name)

# Actually create the archive
print("🔄 Creating archive...")
try:
    subprocess.run(['tar', '-czf', archive_path, '-C', log_dir, '.'], check=True)
    print(f"✅ Archive created: {archive_name}")
    
    # Log the successful creation
    log_file = os.path.join(archive_dir, "archive_log.txt")
    with open(log_file, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Created archive: {archive_name} from {log_dir}\n")
    print(f"📝 Logged to: {log_file}")
    
except subprocess.CalledProcessError:
    print("❌ Failed to create archive")
    sys.exit(1)
