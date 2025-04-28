@echo off
setlocal

:: Target registry key
set "KEY=HKLM\SYSTEM\CurrentControlSet\Control\Keyboard Layout"

:: Compose the binary value:
:: Header (8 bytes) + Count (4 bytes) + 10 remaps (40 bytes) + Null terminator (4 bytes)
:: Count: 0B 00 00 00 = 11 (10 remaps + null)

reg add "%KEY%" /v "Scancode Map" /t REG_BINARY /d 00000000000000000B0000002A001D001D00380038002A004BE04DE04B004DE050E048E048E050E032002E00200032002E00200000000000 /f

echo Keys remapped in registry.
echo Please restart your computer for the changes to take effect.
pause
