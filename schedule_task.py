import os
import subprocess

FILE_PATH = os.path.join(os.path.join(os.path.expanduser("~"), "Documents"), "prank.txt")
RUN_PATH = r"notepad.exe " + FILE_PATH
TASK_NAME = "GetPranked"

def create_file():
    with open(FILE_PATH, "w") as file:
        file.write("You've been pranked")
    # print(FILE_PATH)

def schedule_task():
    interval = "MINUTE"
    repeat_interval = "1"

    command = [
        "schtasks", "/create", "/tn", TASK_NAME,
        "/tr", f'notepad.exe "{FILE_PATH}"',
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
    create_file()
    schedule_task()