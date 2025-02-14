import winreg as reg
import os

def add_to_startup():
    key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    value_name = "OpenTesterFile"
    file_path = r"notepad.exe C:\Users\CatGa\Downloads\tester.txt"  # Opens a file with Notepad - can run any exeecutable (I think)
    
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE) as reg_key:
            reg.SetValueEx(reg_key, value_name, 0, reg.REG_SZ, file_path)
        # print("Autorun registry key added successfully!")
    except PermissionError:
        # print("Error: Please run this script as Administrator.")
        pass

if __name__ == "__main__":
    add_to_startup()