import os
import subprocess
import create_file

def schedule_task():
    task_name = "OpenPrankFile"
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    file_path = os.path.join(documents_path, "prank.txt")
    interval = "MINUTE"
    repeat_interval = "10"

    command = [
        "schtasks", "/create", "/tn", task_name,
        "/tr", f'notepad.exe "{file_path}"',
        "/sc", interval, "/mo", repeat_interval,
        "/f"  # Force update if task already exists
    ]

    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        pass

if __name__ == "__main__":
    # create_file()
    schedule_task()