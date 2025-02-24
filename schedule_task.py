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


def create_quick_cmd():
    launcher_code = """
import os
os.system('start cmd /c exit')
""" # Code within the created file
    with open(os.path.join(DOCUMENTS_PATH, "quick_cmd.py"), "w") as file:
        file.write(launcher_code)
    os.system(f"python -m PyInstaller --onefile \"{os.path.join(DOCUMENTS_PATH, "quick_cmd.py")}\"") # Turns the created Python file into an executable
    # Moves the file to the documents folder
    dist_executable = Path("dist") / "quick_cmd.exe"
    destination = os.path.join(DOCUMENTS_PATH, "quick_cmd.exe")
    if dist_executable.exists():
        shutil.move(str(dist_executable), str(destination))
    else:
        pass
    # Remove created folders and files to keep things clean
    for folder in ["dist", "build"]:
        if Path(folder).exists():
            shutil.rmtree(folder)
    spec_file = Path("quick_cmd.spec")
    if spec_file.exists():
        spec_file.unlink()


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
        "/tr", f'{os.path.join(DOCUMENTS_PATH, "quick_cmd.exe")}',
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
    create_quick_cmd()
    schedule_task()