from models import UserPreferences, OutfitSuggestion
from ai_models.outfit_suggestion_model import generate_outfit_suggestions
from typing import List

class OutfitSuggestionController:
    @staticmethod
    def get_outfit_suggestions(preferences: UserPreferences) -> List[OutfitSuggestion]:
        """
        Get outfit suggestions based on user preferences
        """
        try:
            # Call the AI model to generate suggestions
            suggestions = generate_outfit_suggestions(preferences)
            return suggestions
        except Exception as e:
            raise Exception(f"Error generating outfit suggestions: {str(e)}")
    
    @staticmethod
    def get_themes() -> List[str]:
        """
        Get available outfit themes
        """
        return ["professional", "casual", "party", "date", "interview", "wedding", "vacation"]