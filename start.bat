@echo off
echo Starting StyleMate Pro...

echo Starting backend server...
cd backend
start "Backend Server" cmd /k uvicorn main:app --reload
cd ..

echo Starting frontend server...
cd frontend
npm start

echo Press any key to stop servers...
pause >nul