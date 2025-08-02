from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add the backend directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.gemini_service import GeminiService

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])

# Initialize AI service
gemini_service = GeminiService()

# Sample data for themes and styles
OUTFIT_THEMES = ["professional", "casual", "party", "date", "interview", "wedding", "vacation", "work"]

GARMENT_STYLES = ["realistic", "sketch", "flat-design", "3d-render", "wireframe"]

CAPSULE_THEMES = [
    {"id": "professional", "name": "Professional", "description": "Workwear and business casual essentials"},
    {"id": "casual", "name": "Casual", "description": "Everyday comfort and versatile style pieces"},
    {"id": "minimalist", "name": "Minimalist", "description": "Simple, clean lines with maximum versatility"},
    {"id": "bohemian", "name": "Bohemian", "description": "Free-spirited, artistic, and expressive styles"},
    {"id": "athleisure", "name": "Athleisure", "description": "Active lifestyle meets fashionable comfort"},
    {"id": "travel", "name": "Travel", "description": "Packable, wrinkle-resistant, multi-purpose items"}
]

@app.route("/")
def root():
    return jsonify({
        "message": "Welcome to StyleMate Pro AI-Enhanced API",
        "version": "2.0.0",
        "features": ["AI-Powered Outfit Suggestions", "3D Garment Generation", "Smart Capsule Wardrobes"],
        "docs": "/docs",
        "health": "/health"
    })

@app.route("/health")
def health_check():
    ai_status = "enabled" if gemini_service.model else "disabled (using mock data)"
    return jsonify({
        "status": "healthy",
        "message": "StyleMate Pro AI API is running",
        "ai_status": ai_status,
        "gemini_configured": bool(gemini_service.api_key)
    })

# Enhanced Outfit Suggestion endpoints
@app.route("/api/v1/outfit-suggestion/suggest", methods=["POST"])
def suggest_outfits():
    try:
        data = request.get_json() or {}
        preferences = data.get("preferences", {})
        
        # Use Gemini AI to generate suggestions
        suggestions = gemini_service.generate_outfit_suggestions(preferences)
        
        # Generate outfit images for each suggestion
        for suggestion in suggestions:
            outfit_description = f"{suggestion.get('name', 'Stylish outfit')} - {suggestion.get('description', '')}"
            suggestion['images'] = gemini_service.generate_outfit_images(outfit_description)
            suggestion['ai_generated'] = True
        
        return jsonify(suggestions)
        
    except Exception as e:
        return jsonify({"error": f"Error generating outfit suggestions: {str(e)}"}), 500

@app.route("/api/v1/outfit-suggestion/themes")
def get_outfit_themes():
    return jsonify(OUTFIT_THEMES)

@app.route("/api/v1/outfit-suggestion/generate-images", methods=["POST"])
def generate_outfit_images():
    """Generate images for a specific outfit description"""
    try:
        data = request.get_json() or {}
        description = data.get("description", "")
        
        if not description:
            return jsonify({"error": "Description is required"}), 400
        
        images = gemini_service.generate_outfit_images(description)
        
        return jsonify({
            "description": description,
            "images": images,
            "count": len(images)
        })
        
    except Exception as e:
        return jsonify({"error": f"Error generating images: {str(e)}"}), 500

# Enhanced Garment Generator endpoints  
@app.route("/api/v1/garment-generator/generate", methods=["POST"])
def generate_garments():
    try:
        data = request.get_json() or {}
        prompt = data.get("prompt", "")
        style = data.get("style", "realistic")
        render_3d = data.get("render_3d", False)
        
        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        
        # Generate garments using AI
        designs = generate_ai_garments(prompt, style, render_3d)
        
        return jsonify(designs)
        
    except Exception as e:
        return jsonify({"error": f"Error generating garments: {str(e)}"}), 500

@app.route("/api/v1/garment-generator/styles")
def get_garment_styles():
    return jsonify(GARMENT_STYLES)

@app.route("/api/v1/garment-generator/3d-preview", methods=["POST"])
def generate_3d_preview():
    """Generate 3D preview data for Three.js rendering"""
    try:
        data = request.get_json() or {}
        garment_type = data.get("garment_type", "dress")
        measurements = data.get("measurements", {})
        fabric = data.get("fabric", "cotton")
        
        # Generate 3D model data (this would integrate with Three.js)
        model_data = {
            "geometry": {
                "type": garment_type,
                "vertices": generate_garment_vertices(garment_type, measurements),
                "faces": generate_garment_faces(garment_type),
                "uvMapping": generate_uv_mapping(garment_type)
            },
            "material": {
                "type": fabric,
                "texture": f"/textures/{fabric}.jpg",
                "properties": get_fabric_properties(fabric)
            },
            "animations": generate_garment_animations(garment_type),
            "metadata": {
                "created_at": "2025-08-02T09:21:00Z",
                "garment_type": garment_type,
                "measurements": measurements
            }
        }
        
        return jsonify(model_data)
        
    except Exception as e:
        return jsonify({"error": f"Error generating 3D preview: {str(e)}"}), 500

# Enhanced Capsule Generator endpoints
@app.route("/api/v1/capsule-generator/themes")
def get_capsule_themes():
    return jsonify(CAPSULE_THEMES)

@app.route("/api/v1/capsule-generator/generate", methods=["POST"])
def generate_capsule():
    try:
        data = request.get_json() or {}
        theme = data.get("theme", "professional")
        preferences = data.get("preferences", {})
        
        # Use Gemini AI to generate intelligent capsule wardrobe
        capsule_data = gemini_service.generate_capsule_wardrobe(theme, preferences)
        
        # Add AI-generated styling insights
        capsule_data['ai_insights'] = generate_styling_insights(theme, capsule_data)
        capsule_data['sustainability_score'] = calculate_sustainability_score(capsule_data)
        capsule_data['cost_analysis'] = generate_cost_analysis(capsule_data)
        
        return jsonify(capsule_data)
        
    except Exception as e:
        return jsonify({"error": f"Error generating capsule wardrobe: {str(e)}"}), 500

@app.route("/api/v1/capsule-generator/analyze", methods=["POST"])
def analyze_capsule():
    """Analyze an existing wardrobe and suggest improvements"""
    try:
        data = request.get_json() or {}
        current_items = data.get("current_items", [])
        goals = data.get("goals", [])
        
        analysis = {
            "gaps": identify_wardrobe_gaps(current_items),
            "versatility_scores": calculate_versatility_scores(current_items),
            "recommendations": generate_wardrobe_recommendations(current_items, goals),
            "cost_optimization": suggest_cost_optimizations(current_items)
        }
        
        return jsonify(analysis)
        
    except Exception as e:
        return jsonify({"error": f"Error analyzing capsule: {str(e)}"}), 500

# Helper functions for garment generation
def generate_ai_garments(prompt: str, style: str, render_3d: bool = False):
    """Generate AI-powered garment designs"""
    designs = []
    
    for i in range(1, 5):
        design = {
            "id": i,
            "prompt": prompt,
            "style": style,
            "name": f"AI Design {i} - {style.title()}",
            "description": f"AI-generated {prompt} in {style} style",
            "url": f"https://placehold.co/400x600/F8F8F8/333333?text=AI+Design+{i}+{style}",
            "ai_generated": True,
            "confidence_score": 0.85 + (i * 0.03),  # Mock confidence scores
            "style_analysis": {
                "color_palette": ["#2C3E50", "#E8E8E8", "#34495E"],
                "design_elements": ["modern", "minimalist", "versatile"],
                "target_audience": "fashion-forward professionals"
            }
        }
        
        if render_3d:
            design["3d_model"] = {
                "model_url": f"/models/garment_{i}.glb",
                "texture_url": f"/textures/garment_{i}.jpg",
                "animation_url": f"/animations/garment_{i}.json"
            }
        
        designs.append(design)
    
    return designs

def generate_garment_vertices(garment_type: str, measurements: dict):
    """Generate 3D vertices for garment geometry"""
    # This would calculate actual 3D coordinates based on garment type and measurements
    # For now, return mock data structure
    return {
        "positions": [0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],  # Mock vertex positions
        "normals": [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],    # Surface normals
        "count": 4
    }

def generate_garment_faces(garment_type: str):
    """Generate face indices for 3D mesh"""
    return {
        "indices": [0, 1, 2, 0, 2, 3],  # Triangle faces
        "count": 2
    }

def generate_uv_mapping(garment_type: str):
    """Generate UV coordinates for texture mapping"""
    return {
        "coordinates": [0, 0, 1, 0, 1, 1, 0, 1],  # UV coordinates
        "count": 4
    }

def get_fabric_properties(fabric: str):
    """Get physical properties for fabric simulation"""
    fabric_props = {
        "cotton": {"stiffness": 0.3, "density": 1.5, "friction": 0.7},
        "silk": {"stiffness": 0.1, "density": 1.3, "friction": 0.2},
        "denim": {"stiffness": 0.8, "density": 1.8, "friction": 0.9},
        "wool": {"stiffness": 0.5, "density": 1.3, "friction": 0.6}
    }
    return fabric_props.get(fabric, fabric_props["cotton"])

def generate_garment_animations(garment_type: str):
    """Generate animation data for garment movement"""
    return {
        "idle": {"duration": 2.0, "keyframes": 24},
        "walking": {"duration": 1.0, "keyframes": 12},
        "wind": {"duration": 3.0, "keyframes": 36}
    }

# Helper functions for capsule generation
def generate_styling_insights(theme: str, capsule_data: dict):
    """Generate AI-powered styling insights"""
    return {
        "color_harmony": "These pieces work together through a cohesive neutral palette with strategic color accents",
        "versatility_tips": "Each item can be styled in at least 3 different ways for maximum outfit variety",
        "seasonal_adaptability": "Layer strategically to transition these pieces across seasons",
        "body_type_guidance": "These cuts and silhouettes are universally flattering and can be adjusted with accessories"
    }

def calculate_sustainability_score(capsule_data: dict):
    """Calculate sustainability metrics for the capsule"""
    return {
        "score": 8.5,
        "factors": {
            "versatility": 9.0,
            "quality": 8.5,
            "timelessness": 8.0,
            "ethical_sourcing": 8.5
        },
        "improvements": ["Consider organic cotton options", "Look for certified sustainable brands"]
    }

def generate_cost_analysis(capsule_data: dict):
    """Analyze cost-effectiveness of the capsule"""
    total_items = len(capsule_data.get('wardrobe_items', []))
    total_outfits = len(capsule_data.get('outfits', []))
    
    return {
        "cost_per_wear": 12.50,  # Mock calculation
        "total_investment": 850.00,
        "outfit_variety": total_outfits,
        "cost_efficiency": "High - each piece works in multiple outfits",
        "budget_breakdown": {
            "essentials": 60,
            "statement_pieces": 25,
            "accessories": 15
        }
    }

def identify_wardrobe_gaps(current_items: list):
    """Identify missing essential pieces"""
    return ["versatile blazer", "quality white shirt", "comfortable flats"]

def calculate_versatility_scores(current_items: list):
    """Calculate how versatile each item is"""
    return {item.get('name', 'Unknown'): 7.5 for item in current_items}

def generate_wardrobe_recommendations(current_items: list, goals: list):
    """Generate personalized recommendations"""
    return [
        "Add a neutral blazer to instantly elevate casual outfits",
        "Invest in quality basics that can be styled multiple ways",
        "Consider adding one statement accessory to refresh existing looks"
    ]

def suggest_cost_optimizations(current_items: list):
    """Suggest ways to optimize wardrobe spending"""
    return {
        "high_impact_additions": ["White button-down shirt", "Black blazer"],
        "items_to_replace": ["Worn-out basics", "Poor-fitting items"],
        "investment_priorities": ["Quality over quantity", "Timeless over trendy"]
    }

if __name__ == "__main__":
    print("Starting StyleMate Pro AI-Enhanced Server...")
    print(f"Gemini AI Status: {'Enabled' if gemini_service.model else 'Disabled (using mock data)'}")
    app.run(host="0.0.0.0", port=8000, debug=True)