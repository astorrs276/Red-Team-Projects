@echo off
:: Does not need administrator

:: Set variables
set "DOCS=%USERPROFILE%\Documents"
set "TEXT_FILE=%DOCS%\prank.txt"
set "RUN_PATH=notepad.exe %TEXT_FILE%"
set "TASK_NAME=GetPranked"

:: Create the prank file
echo You've been pranked > "%TEXT_FILE%"

:: Add to Startup (HKCU\Run and RunOnce)
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v %TASK_NAME% /d "%RUN_PATH%" /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v %TASK_NAME% /d "%RUN_PATH%" /f

exit
