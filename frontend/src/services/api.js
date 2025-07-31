const API_BASE_URL = 'http://localhost:8000/api/v1';

class ApiService {
  async suggestOutfits(preferences) {
    const response = await fetch(`${API_BASE_URL}/outfit-suggestion/suggest`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ preferences }),
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  }
  
  async getOutfitThemes() {
    const response = await fetch(`${API_BASE_URL}/outfit-suggestion/themes`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  }
  
  async generateGarments(prompt, style) {
    const response = await fetch(`${API_BASE_URL}/garment-generator/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt, style }),
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  }
  
  async getGarmentStyles() {
    const response = await fetch(`${API_BASE_URL}/garment-generator/styles`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  }
  
  async getCapsuleThemes() {
    const response = await fetch(`${API_BASE_URL}/capsule-generator/themes`);
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  }
  
  async generateCapsule(theme, userPreferences) {
    const response = await fetch(`${API_BASE_URL}/capsule-generator/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ theme, user_preferences: userPreferences }),
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  }
}

export default new ApiService();