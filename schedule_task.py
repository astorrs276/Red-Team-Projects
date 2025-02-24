import os
import subprocess
import shutil
from pathlib import Path

DOCUMENTS_PATH = os.path.join(os.path.expanduser("~"), "Documents")
TEXT_FILE_PATH = os.path.join(DOCUMENTS_PATH, "prank.txt")
RUN_PATH = r"notepad.exe " + TEXT_FILE_PATH
TASK_NAME = "GetPranked"

def create_text_file():
    with open(TEXT_FILE_PATH, "w") as file:
        file.write("You've been pranked")


def schedule_task():
    interval = "MINUTE"
    repeat_interval = "1"

    # Open text file
    '''
    command = [
        "schtasks", "/create", "/tn", TASK_NAME,
        "/tr", f'notepad.exe "{TEXT_FILE_PATH}"',
        "/sc", interval, "/mo", repeat_interval,
        # "/rl", "HIGHEST",  # Run with elevated privileges (only works if run as administrator)
        "/f"  # Force update if task already exists
    ]
    '''

    # Run executable
    command = [
        "schtasks", "/create", "/tn", TASK_NAME,
        "/tr", f'cmd.exe',
        "/sc", interval, "/mo", repeat_interval,
        # "/rl", "HIGHEST",  # Run with elevated privileges (only works if run as administrator)
        "/f"  # Force update if task already exists
    ]

    run_command = [
        "schtasks", "/run", "/tn", TASK_NAME
    ]

    try:
        subprocess.run(command, check=True, shell=True)
        subprocess.run(run_command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        pass

if __name__ == "__main__":
    # create_text_file()
    schedule_task()