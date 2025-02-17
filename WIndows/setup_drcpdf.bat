@echo off
setlocal enabledelayedexpansion

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python from https://www.python.org/downloads/ and add it to PATH.
    pause
    exit /b
)

echo Python is installed.

:: Check if pip is installed
python -m ensurepip --default-pip >nul 2>nul
if %errorlevel% neq 0 (
    echo Pip is not installed. Attempting to install it...
    python -m ensurepip --user
)

:: Upgrade pip
python -m pip install --upgrade pip

:: Install dependencies
echo Installing dependencies...
python -m pip install -r requirements.txt

:: Run the script
echo Running PDF Cracker...
python pdf_cracker.py %*

pause
