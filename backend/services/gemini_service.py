import google.generativeai as genai
import os
import json
import requests
from typing import Dict, List, Any
from dotenv import load_dotenv

load_dotenv()

class GeminiService:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
            print("Warning: GEMINI_API_KEY not found. Using mock responses.")

    def generate_outfit_suggestions(self, preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate outfit suggestions using Gemini AI"""
        if not self.model:
            return self._mock_outfit_suggestions(preferences)
        
        try:
            # Create a detailed prompt for outfit suggestions
            prompt = self._create_outfit_prompt(preferences)
            
            response = self.model.generate_content(prompt)
            
            # Parse the AI response and structure it
            return self._parse_outfit_response(response.text, preferences)
            
        except Exception as e:
            print(f"Error generating outfit suggestions: {e}")
            return self._mock_outfit_suggestions(preferences)

    def generate_outfit_images(self, outfit_description: str) -> List[str]:
        """Generate outfit images using AI (placeholder - would use image generation API)"""
        # Note: Gemini Pro doesn't generate images directly
        # This would typically use DALL-E, Midjourney, or Stable Diffusion API
        # For now, return placeholder images with descriptive text
        
        image_urls = []
        for i in range(3):
            # Create descriptive placeholder URLs
            encoded_desc = outfit_description.replace(' ', '+')
            url = f"https://placehold.co/400x600/E8E8E8/333333?text={encoded_desc}+Style+{i+1}"
            image_urls.append(url)
        
        return image_urls

    def generate_capsule_wardrobe(self, theme: str, preferences: Dict[str, Any] = None) -> Dict[str, Any]:
        """Generate AI-powered capsule wardrobe suggestions"""
        if not self.model:
            return self._mock_capsule_wardrobe(theme)
        
        try:
            prompt = self._create_capsule_prompt(theme, preferences)
            
            response = self.model.generate_content(prompt)
            
            return self._parse_capsule_response(response.text, theme)
            
        except Exception as e:
            print(f"Error generating capsule wardrobe: {e}")
            return self._mock_capsule_wardrobe(theme)

    def _create_outfit_prompt(self, preferences: Dict[str, Any]) -> str:
        """Create a detailed prompt for outfit suggestions"""
        occasion = preferences.get('occasion', 'casual')
        season = preferences.get('season', 'spring')
        budget = preferences.get('budget', 'medium')
        style = preferences.get('preferred_style', 'casual')
        gender = preferences.get('gender', 'female')
        
        prompt = f"""
        As a professional fashion stylist, create 3 complete outfit suggestions for a {gender} with the following preferences:
        
        - Occasion: {occasion}
        - Season: {season}
        - Budget: {budget} ($50-150 for low, $150-300 for medium, $300+ for high)
        - Style preference: {style}
        
        For each outfit, provide:
        1. A complete list of clothing items with specific names
        2. Color recommendations that work well together
        3. Estimated price for each item
        4. Brief styling description
        5. Why this outfit works for the occasion
        
        Format the response as JSON with this structure:
        {{
            "outfits": [
                {{
                    "id": 1,
                    "name": "Outfit Name",
                    "items": [
                        {{"name": "Item Name", "category": "top/bottom/shoes/accessory", "color": "color", "price": 0.00}}
                    ],
                    "total_price": 0.00,
                    "description": "Description of the outfit and styling tips",
                    "occasion_fit": "Why this works for {occasion}"
                }}
            ]
        }}
        """
        
        return prompt

    def _create_capsule_prompt(self, theme: str, preferences: Dict[str, Any] = None) -> str:
        """Create prompt for capsule wardrobe generation"""
        prompt = f"""
        As a fashion expert, create a comprehensive {theme} capsule wardrobe with the following requirements:
        
        1. Select 12-15 essential pieces that work together
        2. Create at least 6 different complete outfit combinations
        3. Focus on versatility and mix-and-match potential
        4. Consider the {theme} lifestyle and needs
        
        Provide the response in JSON format:
        {{
            "theme": "{theme}",
            "wardrobe_items": [
                {{"id": 1, "name": "Item Name", "category": "category", "color": "color", "versatility_score": 9, "essential_reason": "Why this item is essential"}}
            ],
            "outfits": [
                {{
                    "id": 1,
                    "name": "Outfit Name",
                    "items": [1, 2, 3],
                    "description": "When and how to wear this combination",
                    "occasions": ["occasion1", "occasion2"]
                }}
            ],
            "styling_tips": ["tip1", "tip2", "tip3"]
        }}
        """
        
        return prompt

    def _parse_outfit_response(self, response_text: str, preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Parse AI response and structure outfit data"""
        try:
            # Try to extract JSON from the response
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            
            if start_idx != -1 and end_idx != -1:
                json_str = response_text[start_idx:end_idx]
                parsed_data = json.loads(json_str)
                return parsed_data.get('outfits', [])
            else:
                # If JSON parsing fails, create structured response from text
                return self._extract_outfits_from_text(response_text, preferences)
                
        except Exception as e:
            print(f"Error parsing outfit response: {e}")
            return self._mock_outfit_suggestions(preferences)

    def _parse_capsule_response(self, response_text: str, theme: str) -> Dict[str, Any]:
        """Parse AI response for capsule wardrobe"""
        try:
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1
            
            if start_idx != -1 and end_idx != -1:
                json_str = response_text[start_idx:end_idx]
                return json.loads(json_str)
            else:
                return self._mock_capsule_wardrobe(theme)
                
        except Exception as e:
            print(f"Error parsing capsule response: {e}")
            return self._mock_capsule_wardrobe(theme)

    def _extract_outfits_from_text(self, text: str, preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract outfit information from unstructured text response"""
        # This is a fallback method to extract outfit info from text
        # Implementation would parse the text for outfit details
        return self._mock_outfit_suggestions(preferences)

    def _mock_outfit_suggestions(self, preferences: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Fallback mock suggestions when AI is unavailable"""
        occasion = preferences.get('occasion', 'casual')
        
        if occasion == 'work' or occasion == 'professional':
            return [
                {
                    "id": 1,
                    "name": "Professional Power Look",
                    "items": [
                        {"name": "White Button-Down Shirt", "category": "top", "color": "white", "price": 59.99},
                        {"name": "Navy Blazer", "category": "outerwear", "color": "navy", "price": 129.99},
                        {"name": "Black Trousers", "category": "bottom", "color": "black", "price": 79.99},
                        {"name": "Black Leather Heels", "category": "shoes", "color": "black", "price": 99.99}
                    ],
                    "total_price": 369.96,
                    "description": "A timeless professional look that commands respect and confidence in the workplace.",
                    "occasion_fit": "Perfect for important meetings, presentations, and formal office environments."
                }
            ]
        
        return [
            {
                "id": 1,
                "name": "Casual Chic",
                "items": [
                    {"name": "Striped Cotton T-Shirt", "category": "top", "color": "white/navy", "price": 29.99},
                    {"name": "Dark Wash Jeans", "category": "bottom", "color": "indigo", "price": 89.99},
                    {"name": "White Sneakers", "category": "shoes", "color": "white", "price": 79.99}
                ],
                "total_price": 199.97,
                "description": "Effortlessly stylish for everyday activities and casual outings.",
                "occasion_fit": "Great for weekend errands, casual meet-ups, and relaxed social events."
            }
        ]

    def _mock_capsule_wardrobe(self, theme: str) -> Dict[str, Any]:
        """Fallback mock capsule wardrobe"""
        if theme == 'professional':
            return {
                "theme": "Professional",
                "wardrobe_items": [
                    {"id": 1, "name": "White Button-Down Shirt", "category": "top", "color": "white", "versatility_score": 10, "essential_reason": "Works with everything, perfect base layer"},
                    {"id": 2, "name": "Black Blazer", "category": "outerwear", "color": "black", "versatility_score": 9, "essential_reason": "Instantly elevates any outfit"},
                    {"id": 3, "name": "Dark Wash Jeans", "category": "bottom", "color": "indigo", "versatility_score": 8, "essential_reason": "Versatile for business casual days"},
                    {"id": 4, "name": "Black Trousers", "category": "bottom", "color": "black", "versatility_score": 9, "essential_reason": "Essential for formal meetings"}
                ],
                "outfits": [
                    {
                        "id": 1,
                        "name": "Executive Meeting",
                        "items": [1, 2, 4],
                        "description": "Professional and authoritative for important business meetings",
                        "occasions": ["meetings", "presentations", "client calls"]
                    }
                ],
                "styling_tips": [
                    "Invest in quality fabrics that hold their shape",
                    "Neutral colors create more outfit combinations",
                    "Proper fit is more important than trends"
                ]
            }
        
        return {
            "theme": theme.title(),
            "wardrobe_items": [],
            "outfits": [],
            "styling_tips": []
        }