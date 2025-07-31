import React, { useState } from 'react';
import api from '../services/api';
import Loading from '../components/Loading';
import Notification from '../components/Notification';

const OutfitSuggestionPage = () => {
  const [formData, setFormData] = useState({
    gender: 'female',
    age: '',
    height: '',
    weight: '',
    skinTone: '',
    hairColor: '',
    eyeColor: '',
    preferredStyle: '',
    occasion: '',
    season: 'spring',
    budget: 'medium'
  });
  
  const [suggestions, setSuggestions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [notification, setNotification] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const preferences = {
        gender: formData.gender,
        age: parseInt(formData.age) || 0,
        height: parseInt(formData.height) || 0,
        weight: parseInt(formData.weight) || 0,
        skin_tone: formData.skinTone,
        hair_color: formData.hairColor,
        eye_color: formData.eyeColor,
        preferred_style: formData.preferredStyle,
        occasion: formData.occasion,
        season: formData.season,
        budget: formData.budget
      };
      
      const outfitSuggestions = await api.suggestOutfits(preferences);
      setSuggestions(outfitSuggestions);
      setNotification({
        type: 'success',
        message: 'Outfit suggestions generated successfully!'
      });
    } catch (error) {
      setNotification({
        type: 'error',
        message: `Failed to generate suggestions: ${error.message}`
      });
    } finally {
      setLoading(false);
    }
  };

  const handleSelectOutfit = (outfitId) => {
    setNotification({
      type: 'success',
      message: `Outfit #${outfitId} selected!`
    });
  };

  return (
    <div className="max-w-4xl mx-auto p-4">
      <h1 className="text-3xl font-bold text-center my-8">Outfit Suggestion</h1>
      
      {notification && (
        <Notification 
          type={notification.type} 
          message={notification.message}
          onClose={() => setNotification(null)}
        />
      )}
      
      <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="gender">
              Gender
            </label>
            <select
              id="gender"
              name="gender"
              value={formData.gender}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            >
              <option value="female">Female</option>
              <option value="male">Male</option>
              <option value="other">Other</option>
            </select>
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="age">
              Age
            </label>
            <input
              type="number"
              id="age"
              name="age"
              value={formData.age}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Age"
            />
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="height">
              Height (cm)
            </label>
            <input
              type="number"
              id="height"
              name="height"
              value={formData.height}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Height"
            />
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="weight">
              Weight (kg)
            </label>
            <input
              type="number"
              id="weight"
              name="weight"
              value={formData.weight}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Weight"
            />
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="skinTone">
              Skin Tone
            </label>
            <select
              id="skinTone"
              name="skinTone"
              value={formData.skinTone}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            >
              <option value="">Select Skin Tone</option>
              <option value="fair">Fair</option>
              <option value="medium">Medium</option>
              <option value="olive">Olive</option>
              <option value="brown">Brown</option>
              <option value="dark">Dark</option>
            </select>
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="hairColor">
              Hair Color
            </label>
            <select
              id="hairColor"
              name="hairColor"
              value={formData.hairColor}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            >
              <option value="">Select Hair Color</option>
              <option value="black">Black</option>
              <option value="brown">Brown</option>
              <option value="blonde">Blonde</option>
              <option value="red">Red</option>
              <option value="gray">Gray</option>
            </select>
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="eyeColor">
              Eye Color
            </label>
            <select
              id="eyeColor"
              name="eyeColor"
              value={formData.eyeColor}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            >
              <option value="">Select Eye Color</option>
              <option value="brown">Brown</option>
              <option value="blue">Blue</option>
              <option value="green">Green</option>
              <option value="hazel">Hazel</option>
              <option value="gray">Gray</option>
            </select>
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="preferredStyle">
              Preferred Style
            </label>
            <input
              type="text"
              id="preferredStyle"
              name="preferredStyle"
              value={formData.preferredStyle}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="e.g., casual, formal, bohemian"
            />
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="occasion">
              Occasion
            </label>
            <select
              id="occasion"
              name="occasion"
              value={formData.occasion}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            >
              <option value="">Select Occasion</option>
              <option value="work">Work</option>
              <option value="casual">Casual</option>
              <option value="party">Party</option>
              <option value="date">Date</option>
              <option value="wedding">Wedding</option>
              <option value="interview">Interview</option>
            </select>
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="season">
              Season
            </label>
            <select
              id="season"
              name="season"
              value={formData.season}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            >
              <option value="spring">Spring</option>
              <option value="summer">Summer</option>
              <option value="autumn">Autumn</option>
              <option value="winter">Winter</option>
            </select>
          </div>
          
          <div className="mb-4">
            <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="budget">
              Budget
            </label>
            <select
              id="budget"
              name="budget"
              value={formData.budget}
              onChange={handleChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            >
              <option value="low">Low ($0-50)</option>
              <option value="medium">Medium ($50-150)</option>
              <option value="high">High ($150+)</option>
            </select>
          </div>
        </div>
        
        <div className="flex items-center justify-between">
          <button
            type="submit"
            className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            disabled={loading}
          >
            {loading ? 'Generating...' : 'Get Suggestions'}
          </button>
        </div>
      </form>
      
      {loading && <Loading message="Generating outfit suggestions..." />}
      
      {suggestions.length > 0 && (
        <div className="mt-8">
          <h2 className="text-2xl font-bold mb-4">Your Outfit Suggestions</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {suggestions.map((suggestion) => (
              <div key={suggestion.id} className="bg-white shadow-md rounded-lg p-6">
                <h3 className="text-xl font-bold mb-4">Outfit #{suggestion.id}</h3>
                <ul className="mb-4">
                  {suggestion.items.map((item, index) => (
                    <li key={index} className="flex justify-between py-2 border-b">
                      <span>{item.name}</span>
                      <span className="text-gray-600">({item.category})</span>
                    </li>
                  ))}
                </ul>
                <div className="flex justify-between items-center mt-4">
                  <span className="font-bold">Total: ${suggestion.total_price || 'N/A'}</span>
                  <button 
                    className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
                    onClick={() => handleSelectOutfit(suggestion.id)}
                  >
                    Select Outfit
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default OutfitSuggestionPage;