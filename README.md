# InfraWatchLite

InfraWatchLite is a simple, lightweight system monitoring tool designed for Linux systems. Its functions include to log CPU, memory, and disk usage to a log file. It raises warnings when system resource usage exceeds predefined thresholds.

## Installation

1. Clone the repository or download the files.
2. Navigate to the project folder and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python3 infrawatchlite.py
```

Logs will be generated in `logs/monitor.log`.

## Configuration

Edit the `config.json` file to change thresholds and monitoring interval.
