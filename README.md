# Log Archive Tool

A Python-based command-line tool for archiving log files with timestamp-based organization and logging capabilities.

## Features

- Compresses log directories into timestamped tar.gz archives
- Creates organized archive storage directory
- Maintains audit log of all archive operations
- Error handling for invalid directories and failed operations

## Usage

```bash
python3 log_archive.py <log-directory>
```

### Example
```bash
python3 log_archive.py /var/log
python3 log_archive.py ./test_logs
```

## Output

The tool creates:
- `archives/` directory for storing compressed files
- `logs_archive_YYYYMMDD_HHMMSS.tar.gz` - timestamped archive file
- `archives/archive_log.txt` - log file tracking all archive operations

## Requirements

- Python 3.x
- Unix/Linux system with `tar` command
- Read permissions for source directory
- Write permissions for current working directory

## Installation

1. Clone this repository
2. Make the script executable (optional):
   ```bash
   chmod +x log_archive.py
   ```
3. Run with Python 3

## Archive Format

Archives follow the naming convention: `logs_archive_YYYYMMDD_HHMMSS.tar.gz`

Example: `logs_archive_20240925_154626.tar.gz`

## Log File Format

Each archive operation is logged with timestamp and source directory:
```
2024-09-25 15:46:23 - Created archive: logs_archive_20240925_154623.tar.gz from /var/log
```

## Error Handling

The tool validates input and handles common errors:
- Missing command line arguments
- Non-existent source directories  
- Failed compression operations

## DevOps Use Cases

- Automated log rotation and archival
- System maintenance and cleanup
- Backup preparation for log files
- Compliance and audit trail maintenance
