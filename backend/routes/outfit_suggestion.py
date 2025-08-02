from fastapi import APIRouter, HTTPException
from typing import List
from models import UserPreferences, OutfitSuggestion, OutfitRequest
from controllers.outfit_suggestion_controller import OutfitSuggestionController

router = APIRouter()

@router.post("/suggest", response_model=List[OutfitSuggestion])
async def suggest_outfits(request: OutfitRequest):
    try:
        controller = OutfitSuggestionController()
        suggestions = controller.get_outfit_suggestions(request.preferences)
        return suggestions
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating suggestions: {str(e)}")

@router.get("/themes", response_model=List[str])
async def get_themes():
    try:
        controller = OutfitSuggestionController()
        themes = controller.get_themes()
        return themes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching themes: {str(e)}")