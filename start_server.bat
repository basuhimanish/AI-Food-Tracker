@echo off
echo Starting AI Food Tracker Server...
set DATABASE_URL=
cd /d "%~dp0"
call venv\Scripts\activate.bat
uvicorn app.main:app --reload
pause
