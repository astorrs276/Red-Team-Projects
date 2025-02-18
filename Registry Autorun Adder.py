import winreg as reg
import os

def create_file():
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    file_path = os.path.join(documents_path, "prank.txt")
    with open(file_path, "w") as file:
        file.write("You've been pranked")

def add_to_startup():
    key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
    value_name = "GetPranked"
    documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    text_file_path = os.path.join(documents_path, "prank.txt")
    file_path = r"notepad.exe " + text_file_path  # Opens a file with Notepad - can run any executable (I think)
    
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE) as reg_key:
            reg.SetValueEx(reg_key, value_name, 0, reg.REG_SZ, file_path)
        # print("Autorun registry key added successfully!")
    except PermissionError:
        # print("Error: Please run this script as Administrator.")
        pass

if __name__ == "__main__":
    create_file()
    add_to_startup()