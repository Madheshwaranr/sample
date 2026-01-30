import os
import subprocess
from datetime import datetime

# --- Configuration ---
log_dir = "/opt/test"
log_filename = "app_log.txt"
remote_host = "13.204.233.48"  # Splunk forwarder IP
remote_user = "ec2-user"
remote_dir = "/home/ec2-user/"  # target path on remote host
ssh_key_path = "/opt/secret/id_rsa"  # path to your private key
  
# --- Ensure local log directory exists ---
os.makedirs(log_dir, exist_ok=True)
 
# --- Create a log file with timestamp ---
log_path = os.path.join(log_dir, log_filename)
with open(log_path, "a") as log_file:
    log_file.write(f"{datetime.now().isoformat()} - Log entry created\n")

print(f"Log file created: {log_path}")

# --- SCP the log file to the remote host ---
scp_command = [
    "scp",
    "-i", ssh_key_path,
    log_path,
    f"{remote_user}@{remote_host}:{remote_dir}"
]

try:
    subprocess.run(scp_command, check=True)
    print(f"Successfully copied log file to {remote_host}:{remote_dir}")
except subprocess.CalledProcessError as e:
    print(f"Failed to copy file: {e}")
