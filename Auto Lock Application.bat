@echo off
REM Change directory to where the Python script is located
cd /d C:\Users\mrmat\AppData\Local\Programs\Python\Python312

REM Open a new command prompt window, change directory, and run the Python script
start cmd.exe /k "python autoLock.py"

REM Pause to see the output in the current window (optional)
pause
