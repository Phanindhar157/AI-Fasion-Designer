#!/bin/bash

# Script to start both frontend and backend servers

echo "Starting StyleMate Pro..."

# Start backend server in the background
echo "Starting backend server..."
cd backend
uvicorn main:app --reload &
BACKEND_PID=$!
cd ..

# Start frontend server
echo "Starting frontend server..."
cd frontend
npm start

# Kill backend server when frontend is stopped
kill $BACKEND_PID