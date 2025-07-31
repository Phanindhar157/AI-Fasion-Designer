from models import CapsuleTheme, WardrobeItem, CapsuleOutfit
from ai_models.capsule_generation_model import generate_capsule_wardrobe
from typing import List, Tuple, Dict

class CapsuleGeneratorController:
    @staticmethod
    def get_themes() -> List[CapsuleTheme]:
        """
        Get available capsule wardrobe themes
        """
        themes = [
            CapsuleTheme(id="professional", name="Professional", description="Workwear and business casual"),
            CapsuleTheme(id="casual", name="Casual", description="Everyday comfort and style"),
            CapsuleTheme(id="minimalist", name="Minimalist", description="Simple, versatile pieces"),
            CapsuleTheme(id="bohemian", name="Bohemian", description="Free-spirited and artistic"),
            CapsuleTheme(id="athleisure", name="Athleisure", description="Active lifestyle and comfort"),
            CapsuleTheme(id="travel", name="Travel", description="Packing light for trips")
        ]
        return themes
    
    @staticmethod
    def generate_capsule_wardrobe(theme: str, user_preferences: Dict) -> Tuple[List[WardrobeItem], List[CapsuleOutfit]]:
        """
        Generate a capsule wardrobe based on a theme and user preferences
        """
        try:
            # Call the AI model to generate the capsule wardrobe
            wardrobe_items, outfits = generate_capsule_wardrobe(theme, user_preferences)
            return wardrobe_items, outfits
        except Exception as e:
            raise Exception(f"Error generating capsule wardrobe: {str(e)}")