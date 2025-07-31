# StyleMate Pro Backend

This is the backend for StyleMate Pro, built with FastAPI.

## Features

- RESTful API with automatic documentation
- Outfit suggestion service
- Garment generation service
- Capsule wardrobe generator
- CORS support for frontend communication

## API Endpoints

### Outfit Suggestion
- `POST /api/v1/outfit-suggestion/suggest` - Generate outfit suggestions based on user preferences
- `GET /api/v1/outfit-suggestion/themes` - Get available outfit themes

### Garment Generator
- `POST /api/v1/garment-generator/generate` - Generate garment designs from text prompts
- `POST /api/v1/garment-generator/from-sketch` - Generate designs from uploaded sketches
- `GET /api/v1/garment-generator/styles` - Get available design styles

### Capsule Generator
- `GET /api/v1/capsule-generator/themes` - Get available capsule wardrobe themes
- `POST /api/v1/capsule-generator/generate` - Generate capsule wardrobe based on theme

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start the development server:
   ```
   uvicorn main:app --reload
   ```

3. Access the API documentation:
   ```
   http://localhost:8000/docs
   ```

## Technologies

- FastAPI
- Uvicorn
- Pydantic
- Python 3.8+

## Folder Structure

```
backend/
  ai_models/          # AI model implementations (mock for now)
  controllers/        # Business logic controllers
  routes/             # API route definitions
  main.py             # Main application entry point
  models.py           # Data models
  requirements.txt    # Python dependencies