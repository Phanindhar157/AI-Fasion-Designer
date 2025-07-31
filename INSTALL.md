# StyleMate Pro Installation Guide

This guide will help you set up and run StyleMate Pro on your local machine.

## Prerequisites

- Node.js (v14 or higher)
- Python (v3.8 or higher)
- pip (Python package installer)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd stylemate-pro
```

### 2. Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install the required Node.js packages:

```bash
npm install
```

### 3. Backend Setup

Navigate to the backend directory:

```bash
cd ../backend
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Root Directory Setup (for testing)

Navigate to the root directory:

```bash
cd ..
```

Install the testing requirements:

```bash
pip install -r requirements.txt
```

## Running the Application

### Option 1: Manual Start

1. Start the backend server:

```bash
cd backend
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`

2. In a new terminal, start the frontend:

```bash
cd frontend
npm start
```

The frontend will be available at `http://localhost:3000`

### Option 2: Automated Start

Use the provided start scripts:

**Windows:**
```bash
start.bat
```

**Mac/Linux:**
```bash
./start.sh
```

## Testing the Connection

To verify that both frontend and backend are running correctly:

```bash
python test_connection.py
```

## API Documentation

Once the backend is running, you can access the interactive API documentation at:
```
http://localhost:8000/docs
```

## Troubleshooting

### Frontend Issues

- If you see "localhost refused to connect", make sure the frontend server is running
- If styles aren't loading, try clearing your browser cache
- If you get dependency errors, try running `npm install` again

### Backend Issues

- If you see "ModuleNotFoundError", make sure you've installed the requirements
- If you get port conflicts, you can specify a different port:
  ```bash
  uvicorn main:app --reload --port 8001
  ```
- If you get CORS errors, check that the frontend URL matches the CORS settings in `main.py`

### Common Solutions

1. **Port already in use**: Change the port in the start commands
2. **Permission denied**: Try running the commands with administrator privileges
3. **Dependencies not found**: Make sure you're in the correct directory when running install commands

## Development

### Folder Structure

- `frontend/` - React application
- `backend/` - FastAPI application
- `data/` - Sample data and datasets
- `figma/` - Design files and mockups

### Making Changes

1. Frontend changes should be made in the `frontend/src` directory
2. Backend changes should be made in the `backend` directory
3. Always restart the respective server after making changes

## Support

For additional help, please open an issue on the repository.