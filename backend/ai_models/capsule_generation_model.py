from models import WardrobeItem, CapsuleOutfit
from typing import List, Tuple

def generate_capsule_wardrobe(theme: str, user_preferences: dict) -> Tuple[List[WardrobeItem], List[CapsuleOutfit]]:
    """
    Generate a capsule wardrobe based on a theme and user preferences.
    In a real implementation, this would use an AI model.
    """
    # This is a mock implementation that returns sample data
    
    # Sample wardrobe items
    wardrobe_items = [
        WardrobeItem(id=1, name="White Button-Down Shirt", category="top", color="white"),
        WardrobeItem(id=2, name="Black Blazer", category="outerwear", color="black"),
        WardrobeItem(id=3, name="Dark Wash Jeans", category="bottom", color="blue"),
        WardrobeItem(id=4, name="Black Trousers", category="bottom", color="black"),
        WardrobeItem(id=5, name="Little Black Dress", category="dress", color="black"),
        WardrobeItem(id=6, name="White Sneakers", category="shoes", color="white"),
        WardrobeItem(id=7, name="Black Heels", category="shoes", color="black"),
        WardrobeItem(id=8, name="Statement Necklace", category="accessory", color="gold"),
        WardrobeItem(id=9, name="Tote Bag", category="accessory", color="brown"),
        WardrobeItem(id=10, name="Denim Jacket", category="outerwear", color="blue"),
        WardrobeItem(id=11, name="Striped T-Shirt", category="top", color="white/blue"),
        WardrobeItem(id=12, name="Leather Boots", category="shoes", color="brown")
    ]
    
    # Sample outfits based on theme
    if theme == "professional":
        outfits = [
            CapsuleOutfit(
                id=1,
                name="Office Ready",
                items=[1, 2, 4, 7, 8],
                description="Classic professional look for the office"
            ),
            CapsuleOutfit(
                id=2,
                name="Business Casual",
                items=[11, 3, 10, 6, 9],
                description="Comfortable yet stylish for business casual environments"
            )
        ]
    elif theme == "casual":
        outfits = [
            CapsuleOutfit(
                id=3,
                name="Weekend Errands",
                items=[11, 3, 6, 9],
                description="Comfortable and practical for weekend tasks"
            ),
            CapsuleOutfit(
                id=4,
                name="Date Night",
                items=[5, 7, 8],
                description="Elegant outfit for an evening out"
            )
        ]
    else:  # Default outfits
        outfits = [
            CapsuleOutfit(
                id=5,
                name="Versatile Combo",
                items=[1, 3, 6, 8],
                description="Works for many occasions from casual to semi-formal"
            ),
            CapsuleOutfit(
                id=6,
                name="Layered Look",
                items=[11, 10, 4, 12, 9],
                description="Great for transitional weather with layering options"
            )
        ]
    
    return wardrobe_items, outfits