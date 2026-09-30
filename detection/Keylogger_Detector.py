import psutil

def detect_keylogger():
    # List of suspicious process names that could belong to keyloggers
    suspicious_processes = ['keylogger','logkeys','xinput']

    # Iterate through all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            # Check if the process name matches any of the suspicious names
            process_name = proc.info['name'].lower()
            if any(suspicious_name in process_name for suspicious_name in suspicious_processes):
                print(f"Suspicious process detected: {proc.info['name']} (PID: {proc.info['pid']})")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

# Run the detector
if __name__ == "__main__":
    print("Starting keylogger detection...")
    detect_keylogger()
    print("Detection completed.")
