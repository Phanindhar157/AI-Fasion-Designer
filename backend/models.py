from pydantic import BaseModel
from typing import List, Optional

class UserPreferences(BaseModel):
    gender: str
    age: int
    height: int  # in cm
    weight: int  # in kg
    skin_tone: str
    hair_color: str
    eye_color: str
    preferred_style: str
    occasion: str
    season: str
    budget: str

class OutfitItem(BaseModel):
    name: str
    category: str
    color: str
    price: Optional[float] = None

class OutfitSuggestion(BaseModel):
    id: int
    items: List[OutfitItem]
    total_price: Optional[float] = None
    description: Optional[str] = None

class GarmentGenerationRequest(BaseModel):
    prompt: str
    style: str  # realistic, sketch, flat-design

class GarmentDesign(BaseModel):
    id: int
    url: str
    prompt: str

class CapsuleTheme(BaseModel):
    id: str
    name: str
    description: str

class WardrobeItem(BaseModel):
    id: int
    name: str
    category: str
    color: str

class CapsuleOutfit(BaseModel):
    id: int
    name: str
    items: List[int]  # List of item IDs
    description: str