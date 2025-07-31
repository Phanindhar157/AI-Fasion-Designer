from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from models import CapsuleTheme, WardrobeItem, CapsuleOutfit
from controllers.capsule_generator_controller import CapsuleGeneratorController

router = APIRouter()

class CapsuleRequest(BaseModel):
    theme: str
    user_preferences: Dict  # Additional user preferences

@router.get("/themes", response_model=List[CapsuleTheme])
async def get_themes():
    try:
        controller = CapsuleGeneratorController()
        themes = controller.get_themes()
        return themes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching themes: {str(e)}")

@router.post("/generate")
async def generate_capsule(request: CapsuleRequest):
    try:
        controller = CapsuleGeneratorController()
        wardrobe_items, outfits = controller.generate_capsule_wardrobe(request.theme, request.user_preferences)
        return {
            "wardrobe_items": wardrobe_items,
            "outfits": outfits
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating capsule wardrobe: {str(e)}")