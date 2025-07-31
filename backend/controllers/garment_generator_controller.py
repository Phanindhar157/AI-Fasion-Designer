from models import GarmentGenerationRequest, GarmentDesign
from ai_models.garment_generation_model import generate_garment_designs
from typing import List

class GarmentGeneratorController:
    @staticmethod
    def generate_garments(request: GarmentGenerationRequest) -> List[GarmentDesign]:
        """
        Generate garment designs based on a text prompt
        """
        try:
            # Call the AI model to generate designs
            designs = generate_garment_designs(request.prompt, request.style)
            return designs
        except Exception as e:
            raise Exception(f"Error generating garment designs: {str(e)}")
    
    @staticmethod
    def get_styles() -> List[str]:
        """
        Get available design styles
        """
        return ["realistic", "sketch", "flat-design"]