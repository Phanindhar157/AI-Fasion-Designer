from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import outfit_suggestion, garment_generator, capsule_generator

app = FastAPI(
    title="StyleMate Pro API",
    description="API for the StyleMate Pro fashion recommendation system",
    version="1.0.0"
)

# Add CORS middleware to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # React default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    outfit_suggestion.router, 
    prefix="/api/v1/outfit-suggestion", 
    tags=["outfit-suggestion"]
)
app.include_router(
    garment_generator.router, 
    prefix="/api/v1/garment-generator", 
    tags=["garment-generator"]
)
app.include_router(
    capsule_generator.router, 
    prefix="/api/v1/capsule-generator", 
    tags=["capsule-generator"]
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to StyleMate Pro API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "StyleMate Pro API is running"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)