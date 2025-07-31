from models import UserPreferences, OutfitSuggestion, OutfitItem
from typing import List

def generate_outfit_suggestions(preferences: UserPreferences) -> List[OutfitSuggestion]:
    """
    Generate outfit suggestions based on user preferences.
    In a real implementation, this would use an AI model.
    """
    # This is a mock implementation that returns sample data
    # based on the user's preferences
    
    suggestions = []
    
    # Create some sample outfits based on occasion
    if preferences.occasion == "work":
        suggestions.append(OutfitSuggestion(
            id=1,
            items=[
                OutfitItem(name="White Button-Down Shirt", category="top", color="white"),
                OutfitItem(name="Black Blazer", category="outerwear", color="black"),
                OutfitItem(name="Black Trousers", category="bottom", color="black"),
                OutfitItem(name="Black Heels", category="shoes", color="black", price=89.99)
            ],
            total_price=179.97,
            description="Classic professional look for the office"
        ))
        
        suggestions.append(OutfitSuggestion(
            id=2,
            items=[
                OutfitItem(name="Navy Blouse", category="top", color="navy"),
                OutfitItem(name="Gray Pencil Skirt", category="bottom", color="gray"),
                OutfitItem(name="Nude Pumps", category="shoes", color="nude", price=75.00)
            ],
            total_price=150.00,
            description="Elegant work outfit with a feminine touch"
        ))
    
    elif preferences.occasion == "casual":
        suggestions.append(OutfitSuggestion(
            id=3,
            items=[
                OutfitItem(name="Striped T-Shirt", category="top", color="white/blue"),
                OutfitItem(name="Dark Wash Jeans", category="bottom", color="blue"),
                OutfitItem(name="White Sneakers", category="shoes", color="white", price=65.00)
            ],
            total_price=85.00,
            description="Comfortable and stylish for everyday wear"
        ))
        
        suggestions.append(OutfitSuggestion(
            id=4,
            items=[
                OutfitItem(name="Floral Dress", category="dress", color="multi"),
                OutfitItem(name="Denim Jacket", category="outerwear", color="blue"),
                OutfitItem(name="Sandals", category="shoes", color="tan", price=45.00)
            ],
            total_price=95.00,
            description="Perfect for a casual day out"
        ))
    
    else:  # Default suggestions
        suggestions.append(OutfitSuggestion(
            id=5,
            items=[
                OutfitItem(name="Black T-Shirt", category="top", color="black"),
                OutfitItem(name="Khaki Pants", category="bottom", color="beige"),
                OutfitItem(name="Canvas Sneakers", category="shoes", color="white", price=55.00)
            ],
            total_price=110.00,
            description="Versatile outfit that works for many occasions"
        ))
    
    return suggestions