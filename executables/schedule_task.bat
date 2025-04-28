@echo off
setlocal

:: Set variables
set "DOCS=%USERPROFILE%\Documents"
set "TEXT_FILE=%DOCS%\prank.txt"
set "TASK_NAME=GetPranked"

:: Create the prank file
echo You've been pranked > "%TEXT_FILE%"

:: Schedule task to run cmd.exe every minute
schtasks /create /tn "%TASK_NAME%" /tr "cmd.exe" /sc MINUTE /mo 1 /f

:: Optionally run the task immediately
schtasks /run /tn "%TASK_NAME%"

echo Scheduled task created and executed.
pause