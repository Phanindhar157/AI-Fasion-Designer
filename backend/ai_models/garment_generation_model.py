from models import GarmentDesign
from typing import List

def generate_garment_designs(prompt: str, style: str) -> List[GarmentDesign]:
    """
    Generate garment designs based on a text prompt.
    In a real implementation, this would use an AI model.
    """
    # This is a mock implementation that returns sample data
    
    designs = []
    
    # Generate 4 sample designs
    for i in range(1, 5):
        designs.append(GarmentDesign(
            id=i,
            url=f"https://placehold.co/300x400/EEE/31343C?text=Design+{i}",
            prompt=prompt
        ))
    
    return designs