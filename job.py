import os
import subprocess
from datetime import datetime

# --- Configuration ---
log_dir = "/opt/test"
log_filename = "app_log.txt"
remote_host = "13.204.233.48"  # replace with your host
remote_user = "ec2-user"
remote_dir = "/home/ec2-user"

# --- Ensure the log directory exists ---
os.makedirs(log_dir, exist_ok=True)

# --- Create log file with timestamp ---
log_path = os.path.join(log_dir, log_filename)
with open(log_path, "a") as log_file:
    log_file.write(f"{datetime.now().isoformat()} - Log entry created\n")

print(f"Log file created: {log_path}")

# --- SCP the log file to remote host ---
scp_command = f"scp {log_path} {remote_user}@{remote_host}:{remote_dir}"
try:
    subprocess.run(scp_command, shell=True, check=True)
    print(f"Successfully copied log file to {remote_host}:{remote_dir}")
except subprocess.CalledProcessError as e:
    print(f"Failed to copy file: {e}")
