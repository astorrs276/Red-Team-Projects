@echo off
:: Requires admin privileges
:: Remaps Q→W, W→E, ..., M→Z, P→Q, L→A

:: Set the registry value directly (this is the binary representation of the remap_dict in the Python script)
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Keyboard Layout" /v "Scancode Map" /t REG_BINARY /d ^
00000000000000001C000D0000000E000F001000110012001300140015001600170018001900100011001E001F0020002100220023002400250026001E002C002D002E002F003000310032002C0000000000 /f

echo Keys remapped. Please restart your computer for changes to take effect.
pause