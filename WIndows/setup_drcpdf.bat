@echo off
setlocal enabledelayedexpansion

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo 🔴 Python not found. Installing Python...
    powershell -Command "Start-Process 'https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe' -ArgumentList '/quiet InstallAllUsers=1 PrependPath=1' -Wait"
    echo ✅ Python installed! Restarting setup...
    
    :: Refresh environment variables to recognize Python without requiring a restart
    set "Path=%Path%;C:\Program Files\Python310\Scripts\;C:\Program Files\Python310\"

    :: Check again if Python is installed
    where python >nul 2>nul
    if %errorlevel% neq 0 (
        echo ❌ Failed to detect Python after installation. Please restart your computer and try again.
        exit /b
    )
)

:: Install required dependencies
echo 🔄 Installing dependencies...
pip install -r requirements.txt

:: Run the cracker
echo 🚀 Running DRC PDF Cracker...
python drcpdf.py %*

endlocal
