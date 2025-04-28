@echo off
:: Requires admin privileges

:: shift -> ctrl -> alt -> shift, invert arrow keys, C -> D -> M -> C
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Keyboard Layout" /v "Scancode Map" /t REG_BINARY /d ^
00000000000000000B0000001D002A0038001D002A0038004BE04DE04DE04BE050E048E048E050E02E0032003200200020002E0000000000 /f

exit
