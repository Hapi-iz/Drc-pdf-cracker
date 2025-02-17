@echo off
echo Installing dependencies...

:: Install Python if not present
where python >nul 2>nul
if errorlevel 1 (
    echo Python not found. Please install Python first.
    exit /b
)

:: Install required Python packages
pip install -r requirements.txt

:: Run the PDF Cracker script
python pdf_cracker.py %*

pause
