import os
import time

# Directory to monitor
log_dir = 'logs/'

# Function to monitor logs
def monitor_logs():
    print("Monitoring logs...")
    log_files = os.listdir(log_dir)
    for log_file in log_files:
        with open(os.path.join(log_dir, log_file), 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "ERROR" in line:
                    print(f"Alert: {line.strip()}")

if __name__ == "__main__":
    while True:
        monitor_logs()
        time.sleep(60)  # Check every minute
