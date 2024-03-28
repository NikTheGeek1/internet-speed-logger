# Internet Speed Logger

## Overview

This Python script is designed to log the internet connection's upload and download speeds at regular intervals. It runs for a specified duration and records the speeds every 30 minutes.

## Features

- Logs internet download and upload speeds.
- Records data every 30 minutes.
- Saves the data in a CSV format with timestamps for each entry.

## Requirements

- Python 3
- `speedtest-cli` package

## Installation

1. Ensure Python 3 is installed on your system.
2. Install the `speedtest-cli` package using pip:
   ```bash
   pip install speedtest-cli
   ```

## Usage

To run the script, execute:

```bash
python speed_logger.py
```

The script will start logging the internet speed every 30 minutes into a file named `internet_speed.csv`.

## Output Format

The output CSV file will have the following columns:

- Timestamp (in ISO format)
- Download Speed (in bits per second)
- Upload Speed (in bits per second)

## Note

The script is intended for short-term monitoring and will run for the duration for which it is started. For long-term monitoring, a more robust solution like a daemon or a service is recommended.