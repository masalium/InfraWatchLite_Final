import psutil
import time
import json
import logging
from datetime import datetime


class SystemMonitor:
    def __init__(self, config_path='config.json', log_path='logs/monitor.log'):
        self.config = self.load_config(config_path)
        self.interval = self.config.get('interval', 5)
        self.thresholds = self.config.get('thresholds', {})
        self.setup_logging(log_path)

    def load_config(self, path):
        """Load monitoring thresholds and interval from a JSON config file."""
        try:
            with open(path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Config file {path} not found. Using default settings.")
            return {
                'interval': 5,
                'thresholds': {
                    'cpu': 80,
                    'memory': 80,
                    'disk': 80
                }
            }

    def setup_logging(self, log_file):
        """Initialize logging configuration."""
        logging.basicConfig(
            filename=log_file,
            filemode='a',
            format='%(asctime)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )

    def log_warning(self, metric, value, threshold):
        """Log a warning message if a resource exceeds its threshold."""
        message = f"{metric.upper()} usage is high: {value}% (threshold: {threshold}%)"
        print(message)
        logging.warning(message)

    def check_metrics(self):
        """Monitor system metrics and log warnings if thresholds are exceeded."""
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        if cpu > self.thresholds.get('cpu', 80):
            self.log_warning('cpu', cpu, self.thresholds.get('cpu'))
        if memory > self.thresholds.get('memory', 80):
            self.log_warning('memory', memory, self.thresholds.get('memory'))
        if disk > self.thresholds.get('disk', 80):
            self.log_warning('disk', disk, self.thresholds.get('disk'))

    def start(self):
        """Start the continuous monitoring process."""
        print("Monitoring started. Press Ctrl+C to stop.")
        try:
            while True:
                self.check_metrics()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("Monitoring stopped.")


if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.start()
