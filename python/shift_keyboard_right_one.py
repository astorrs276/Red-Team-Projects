import winreg as reg
import ctypes
import sys

# Standard and extended scan codes
scancode_dict = {'ESC': 0x01,'1': 0x02,'2': 0x03,'3': 0x04,'4': 0x05,'5': 0x06,'6': 0x07,'7': 0x08,'8': 0x09,'9': 0x0A,'0': 0x0B,'-': 0x0C,'=': 0x0D,'BACKSPACE': 0x0E,'TAB': 0x0F,'Q': 0x10,'W': 0x11,'E': 0x12,'R': 0x13,'T': 0x14,'Y': 0x15,'U': 0x16,'I': 0x17,'O': 0x18,'P': 0x19,'[': 0x1A,']': 0x1B,'ENTER': 0x1C,'LEFT_CTRL': 0x1D,'A': 0x1E,'S': 0x1F,'D': 0x20,'F': 0x21,'G': 0x22,'H': 0x23,'J': 0x24,'K': 0x25,'L': 0x26,';': 0x27,"'": 0x28,'`': 0x29,'LEFT_SHIFT': 0x2A,'\\': 0x2B,'Z': 0x2C,'X': 0x2D,'C': 0x2E,'V': 0x2F,'B': 0x30,'N': 0x31,'M': 0x32,',': 0x33,'.': 0x34,'/': 0x35,'RIGHT_SHIFT': 0x36,'KP_*': 0x37,'LEFT_ALT': 0x38,'SPACE': 0x39,'CAPS_LOCK': 0x3A,'F1': 0x3B,'F2': 0x3C,'F3': 0x3D,'F4': 0x3E,'F5': 0x3F,'F6': 0x40,'F7': 0x41,'F8': 0x42,'F9': 0x43,'F10': 0x44,'NUM_LOCK': 0x45,'SCROLL_LOCK': 0x46,'KP_7': 0x47,'KP_8': 0x48,'KP_9': 0x49,'KP_-': 0x4A,'KP_4': 0x4B,'KP_5': 0x4C,'KP_6': 0x4D,'KP_+': 0x4E,'KP_1': 0x4F,'KP_2': 0x50,'KP_3': 0x51,'KP_0': 0x52,'KP_.': 0x53,'F11': 0x57,'F12': 0x58,'LEFT_ARROW': 0xE04B,'RIGHT_ARROW': 0xE04D,'UP_ARROW': 0xE048,'DOWN_ARROW': 0xE050,}

def encode_entry(to_code, from_code):
    """Encode 4 bytes: TO_LO, TO_HI, FROM_LO, FROM_HI"""
    to_lo = to_code & 0xFF
    to_hi = (to_code >> 8) & 0xFF
    from_lo = from_code & 0xFF
    from_hi = (from_code >> 8) & 0xFF
    return bytes([to_lo, to_hi, from_lo, from_hi])

def set_scancode_map(remap_dict):
    data = bytearray()

    # Header: version + flags
    data += b'\x00\x00\x00\x00'
    data += b'\x00\x00\x00\x00'

    # Number of entries = number of remaps + 1 (null terminator)
    entry_count = len(remap_dict) + 1
    data += entry_count.to_bytes(4, 'little')

    for from_key, to_key in remap_dict.items():
        from_code = scancode_dict.get(from_key.upper())
        to_code = scancode_dict.get(to_key.upper())

        if from_code is None or to_code is None:
            print(f"[!] Unknown key in remap: {from_key} or {to_key}")
            continue

        data += encode_entry(to_code, from_code)

    # Null terminator
    data += b'\x00\x00\x00\x00'

    try:
        key_path = r"SYSTEM\CurrentControlSet\Control\Keyboard Layout"
        reg_key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, key_path, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(reg_key, "Scancode Map", 0, reg.REG_BINARY, data)
        reg.CloseKey(reg_key)
        print("Success. Restart for changes.")
    except PermissionError:
        print("Run as admin.")
        sys.exit(1)

if __name__ == "__main__":
    remap_dict = {
        "Q":"W",
        "W":"E",
        "E":"R",
        "R":"T",
        "T":"Y",
        "Y":"U",
        "U":"I",
        "I":"O",
        "O":"P",
        "P":"Q",
        "A":"S",
        "S":"D",
        "D":"F",
        "F":"G",
        "G":"H",
        "H":"J",
        "J":"K",
        "K":"L",
        "L":"A",
        "Z":"X",
        "X":"C",
        "C":"V",
        "V":"B",
        "B":"N",
        "N":"M",
        "M":"Z"
    }

    set_scancode_map(remap_dict)
