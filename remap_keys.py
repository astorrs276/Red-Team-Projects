import winreg as reg
import sys

def set_scancode_map(remap_list):
    # Header + count (remaps + null terminator)
    total_entries = len(remap_list) + 1
    data = bytearray()

    # Header (8 bytes)
    data += b'\x00\x00\x00\x00'  # Version
    data += b'\x00\x00\x00\x00'  # Flags

    # Number of entries (4 bytes)
    data += total_entries.to_bytes(4, byteorder='little')

    # Each mapping: TO TO FROM FROM (4 bytes each)
    for from_code, to_code in remap_list:
        data += to_code.to_bytes(2, 'little')
        data += from_code.to_bytes(2, 'little')

    # Null terminator (4 bytes)
    data += b'\x00\x00\x00\x00'

    try:
        key_path = r"SYSTEM\CurrentControlSet\Control\Keyboard Layout"
        reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(reg_key, "Scancode Map", 0, reg.REG_BINARY, data)
        reg.CloseKey(reg_key)
        print("Registry updated. Restart to apply changes.")
    except PermissionError:
        print("Run as admin")
        sys.exit(1)

if __name__ == "__main__":
    # Example remap: Caps Lock (0x3A) → Left Ctrl (0x1D)
    set_scancode_map([
        (0x3A, 0x1D)
    ])
