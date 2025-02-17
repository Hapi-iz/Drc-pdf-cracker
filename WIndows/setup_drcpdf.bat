@echo off
setlocal

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo 🔴 Python not found. Please install Python manually from:
    echo    https://www.python.org/downloads/
    echo After installation, restart this setup.
    echo.
    echo 🔄 Waiting for you to install Python... Press any key once done.
    pause >nul
    goto :RETRY
)

:RETRY
:: Re-check if Python is installed after user presses a key
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ Python is still not installed. Please install it and try again.
    echo Press any key to check again...
    pause >nul
    goto :RETRY
)

:: Install required dependencies
echo 🔄 Installing dependencies...
pip install -r requirements.txt

:: Run the cracker
echo 🚀 Running DRC PDF Cracker...
python drcpdf.py %*

:: Keep CMD open
echo.
echo ✅ Setup complete! Press any key to exit...
pause >nul
