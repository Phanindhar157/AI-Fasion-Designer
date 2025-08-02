from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000", "http://127.0.0.1:3000"])

# Sample data
OUTFIT_THEMES = ["professional", "casual", "party", "date", "interview", "wedding", "vacation"]

GARMENT_STYLES = ["realistic", "sketch", "flat-design"]

CAPSULE_THEMES = [
    {"id": "professional", "name": "Professional", "description": "Workwear and business casual"},
    {"id": "casual", "name": "Casual", "description": "Everyday comfort and style"},
    {"id": "minimalist", "name": "Minimalist", "description": "Simple, versatile pieces"},
    {"id": "bohemian", "name": "Bohemian", "description": "Free-spirited and artistic"},
    {"id": "athleisure", "name": "Athleisure", "description": "Active lifestyle and comfort"},
    {"id": "travel", "name": "Travel", "description": "Packing light for trips"}
]

@app.route("/")
def root():
    return jsonify({
        "message": "Welcome to StyleMate Pro API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    })

@app.route("/health")
def health_check():
    return jsonify({"status": "healthy", "message": "StyleMate Pro API is running"})

# Outfit Suggestion endpoints
@app.route("/api/v1/outfit-suggestion/suggest", methods=["POST"])
def suggest_outfits():
    data = request.get_json() or {}
    preferences = data.get("preferences", {})
    occasion = preferences.get("occasion", "")
    
    if occasion == "work":
        suggestions = [
            {
                "id": 1,
                "items": [
                    {"name": "White Button-Down Shirt", "category": "top", "color": "white", "price": 49.99},
                    {"name": "Black Blazer", "category": "outerwear", "color": "black", "price": 89.99},
                    {"name": "Black Trousers", "category": "bottom", "color": "black", "price": 65.99},
                    {"name": "Black Heels", "category": "shoes", "color": "black", "price": 89.99}
                ],
                "total_price": 295.96,
                "description": "Classic professional look for the office"
            },
            {
                "id": 2,
                "items": [
                    {"name": "Navy Blouse", "category": "top", "color": "navy", "price": 45.99},
                    {"name": "Gray Pencil Skirt", "category": "bottom", "color": "gray", "price": 55.99},
                    {"name": "Nude Pumps", "category": "shoes", "color": "nude", "price": 75.00}
                ],
                "total_price": 176.98,
                "description": "Elegant work outfit with a feminine touch"
            }
        ]
    elif occasion == "casual":
        suggestions = [
            {
                "id": 3,
                "items": [
                    {"name": "Striped T-Shirt", "category": "top", "color": "white/blue", "price": 25.99},
                    {"name": "Dark Wash Jeans", "category": "bottom", "color": "blue", "price": 79.99},
                    {"name": "White Sneakers", "category": "shoes", "color": "white", "price": 65.00}
                ],
                "total_price": 170.98,
                "description": "Comfortable and stylish for everyday wear"
            },
            {
                "id": 4,
                "items": [
                    {"name": "Floral Dress", "category": "dress", "color": "multi", "price": 59.99},
                    {"name": "Denim Jacket", "category": "outerwear", "color": "blue", "price": 49.99},
                    {"name": "Sandals", "category": "shoes", "color": "tan", "price": 45.00}
                ],
                "total_price": 154.98,
                "description": "Perfect for a casual day out"
            }
        ]
    else:
        suggestions = [
            {
                "id": 5,
                "items": [
                    {"name": "Black T-Shirt", "category": "top", "color": "black", "price": 29.99},
                    {"name": "Khaki Pants", "category": "bottom", "color": "beige", "price": 59.99},
                    {"name": "Canvas Sneakers", "category": "shoes", "color": "white", "price": 55.00}
                ],
                "total_price": 144.98,
                "description": "Versatile outfit that works for many occasions"
            }
        ]
    
    return jsonify(suggestions)

@app.route("/api/v1/outfit-suggestion/themes")
def get_outfit_themes():
    return jsonify(OUTFIT_THEMES)

# Garment Generator endpoints
@app.route("/api/v1/garment-generator/generate", methods=["POST"])
def generate_garments():
    data = request.get_json() or {}
    prompt = data.get("prompt", "")
    style = data.get("style", "realistic")
    
    # Mock generated designs
    designs = []
    for i in range(1, 5):
        designs.append({
            "id": i,
            "url": f"https://placehold.co/300x400/EEE/31343C?text=Design+{i}+{style}",
            "prompt": prompt
        })
    
    return jsonify(designs)

@app.route("/api/v1/garment-generator/styles")
def get_garment_styles():
    return jsonify(GARMENT_STYLES)

# Capsule Generator endpoints
@app.route("/api/v1/capsule-generator/themes")
def get_capsule_themes():
    return jsonify(CAPSULE_THEMES)

@app.route("/api/v1/capsule-generator/generate", methods=["POST"])
def generate_capsule():
    data = request.get_json() or {}
    theme = data.get("theme", "professional")
    
    # Mock wardrobe items
    wardrobe_items = [
        {"id": 1, "name": "White Button-Down Shirt", "category": "top", "color": "white"},
        {"id": 2, "name": "Black Blazer", "category": "outerwear", "color": "black"},
        {"id": 3, "name": "Dark Wash Jeans", "category": "bottom", "color": "blue"},
        {"id": 4, "name": "Black Trousers", "category": "bottom", "color": "black"},
        {"id": 5, "name": "Little Black Dress", "category": "dress", "color": "black"},
        {"id": 6, "name": "White Sneakers", "category": "shoes", "color": "white"},
        {"id": 7, "name": "Black Heels", "category": "shoes", "color": "black"},
        {"id": 8, "name": "Statement Necklace", "category": "accessory", "color": "gold"}
    ]
    
    # Mock outfits based on theme
    if theme == "professional":
        outfits = [
            {
                "id": 1,
                "name": "Office Ready",
                "items": [1, 2, 4, 7, 8],
                "description": "Classic professional look for the office"
            },
            {
                "id": 2,
                "name": "Business Casual",
                "items": [1, 3, 6],
                "description": "Comfortable yet stylish for business casual environments"
            }
        ]
    elif theme == "casual":
        outfits = [
            {
                "id": 3,
                "name": "Weekend Errands",
                "items": [1, 3, 6],
                "description": "Comfortable and practical for weekend tasks"
            },
            {
                "id": 4,
                "name": "Date Night",
                "items": [5, 7, 8],
                "description": "Elegant outfit for an evening out"
            }
        ]
    else:
        outfits = [
            {
                "id": 5,
                "name": "Versatile Combo",
                "items": [1, 3, 6, 8],
                "description": "Works for many occasions from casual to semi-formal"
            }
        ]
    
    return jsonify({
        "wardrobe_items": wardrobe_items,
        "outfits": outfits
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)