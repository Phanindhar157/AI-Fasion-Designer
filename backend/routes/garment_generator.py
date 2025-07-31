from fastapi import APIRouter, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List
from models import GarmentGenerationRequest, GarmentDesign
from controllers.garment_generator_controller import GarmentGeneratorController

router = APIRouter()

@router.post("/generate", response_model=List[GarmentDesign])
async def generate_garments(request: GarmentGenerationRequest):
    try:
        controller = GarmentGeneratorController()
        designs = controller.generate_garments(request)
        return designs
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating designs: {str(e)}")

@router.post("/from-sketch")
async def generate_from_sketch(file: UploadFile = File(...)):
    try:
        # In a real implementation, this would process the uploaded sketch
        # and generate a garment design based on it
        return {
            "message": "Sketch received successfully",
            "design_id": "sketch_" + str(hash(file.filename)) % 10000
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing sketch: {str(e)}")

@router.get("/styles", response_model=List[str])
async def get_styles():
    try:
        controller = GarmentGeneratorController()
        styles = controller.get_styles()
        return styles
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching styles: {str(e)}")